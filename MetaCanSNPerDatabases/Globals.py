

from functools import cached_property, cache
import sqlite3, hashlib, re, os, logging, shutil, sys
from typing import Generator, Callable, Iterable, Self, Literal, LiteralString, Any, TextIO, BinaryIO, Never, Iterator, TypeVar, Type, get_args, get_origin
import typing

from PseudoPathy import Path, DirectoryPath, FilePath, PathGroup, PathLibrary, PathList
from PseudoPathy.Library import CommonGroups
from PseudoPathy.PathShortHands import *

from MetaCanSNPerDatabases.Exceptions import *

def isType(value, typed):
	try:
		return isinstance(value, typed)
	except TypeError:
		try:
			assert isinstance(value, get_origin(typed))
			subTypes = get_args(typed)
			if len(subTypes) == 0:
				return True
			elif len(subTypes) == 1:
				return all(isType(v, subTypes[0]) for v in value)
			elif isinstance(subTypes[0], int) and len(value) == subTypes[0]:
				return all(isType(v, t) for v,t in zip(value, subTypes[1:]))
			elif len(subTypes) == len(value):
				return all(isType(v, subTyped) for v, subTyped in zip(value, subTypes))
		except:
			pass
	finally:
		return False

class Overload:

	_funcs : list[tuple[dict[int|str,Type],Callable]]
	__name__ : str

	def __init__(self, func : Callable):
		self._funcs = []
		self.__name__ = func.__code__.co_name
		self.add(func)

	def __call__(self, *args : tuple[Any], **kwargs : dict[str,Any]):
		
		for annotation, func in self._funcs:
			if func.__code__.co_posonlyargcount != len(args):
				continue
			elif any(not isType(arg, annotation[name]) for name, arg in zip(func.__code__.co_varnames, args)):
				continue
			elif any(not isType(kwargs[name], annotation[name]) for name in kwargs):
				continue
			else:
				return func(*args, **kwargs)
		raise NotImplemented(f"No definition satisfies {self.__name__}({', '.join([', '.join(map(str,args)), ', '.join(map('='.join, args.items()))])})")
	
	def __repr__(self):
		return f"<Overloaded function '{self.__name__}'>"
	
	def add(self, func : Callable):
		try:
			assert isinstance(func, Callable)
			self._funcs.append((func.__annotations__, func))
		except AssertionError:
			raise TypeError(f"Only `Callable` objects are overloadable. {func!r} is not an instance of `Callable`")
		return self

class Mode: pass
class ReadMode: pass
class WriteMode: pass
class Direction: pass
class Nucleotides: pass

Mode        = Literal["r", "w"]
ReadMode    = Literal["r"]
WriteMode   = Literal["w"]
Direction   = Literal["DESC","ASC"]
Nucleotides = Literal["A", "T", "C", "G", "N"]

formatPattern = re.compile(r"[{](.*?)[}]")

LOGGER = logging.Logger("MetaCanSNPerDatabases", level=logging.WARNING)

LOGGER_FILEHANDLER = logging.FileHandler("MetaCanSNPerDatabases.log")
LOGGER_FILEHANDLER.setFormatter(logging.Formatter("[%(name)s] %(asctime)s - %(levelname)s: %(message)s"))
LOGGER.addHandler(LOGGER_FILEHANDLER)

DATABASE_VERSIONS : dict[str,int] = {
	"7630f33662e27489b7bb7b3b121ca4ff" : 1, # Legacy CanSNPer
	"175c47f1ad61ec81a7d11d8a8e1887ff" : 2  # MetaCanSNPer Alpha version
}
LEGACY_VERSION = 0
CURRENT_VERSION = 2
CURRENT_TABLES_HASH = ""
CURRENT_INDEXES_HASH = ""
STRICT : bool = False
SOFTWARE_NAME = "MetaCanSNPer"

SOURCES = [
	"https://github.com/XJ-04561/MetaCanSNPer-data/raw/master/database/{databaseName}", # MetaCanSNPer
	"https://github.com/FOI-Bioinformatics/CanSNPer2-data/raw/master/database/{databaseName}" # Legacy CanSNPer
]

SOURCED = {"refseq":"F", "genbank": "A"}
NCBI_FTP_LINK = "ftp://ftp.ncbi.nlm.nih.gov/genomes/all/GC{source}/{n1}/{n2}/{n3}/{genome_id}_{assembly}/{genome_id}_{assembly}_genomic.fna.gz"