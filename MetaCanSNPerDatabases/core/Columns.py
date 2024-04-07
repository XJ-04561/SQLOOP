
from MetaCanSNPerDatabases.core._Constants import *
from MetaCanSNPerDatabases.Globals import *


class Column:
	
	name : str
	databaseName : str
	
	def __init__(self, name : str, databaseName : str):
		self.name = name
		self.databaseName = databaseName
	
	def __repr__(self):
		return self.name
		
	def __str__(self):
		return self.databaseName
	
	def __hash__(self):
		return self.name.__hash__()
	
	def __neg__(self):
		return Column(self.name, f"{self.databaseName} ASC")

ALL				= Column("ALL", "*")
Parent			= Column("Parent", COLUMN_PARENT)
NodeID			= Column("NodeID", COLUMN_NODE_ID)
GenoType		= Column("GenoType", COLUMN_GENOTYPE)
Position		= Column("Position", COLUMN_POSITION)
Ancestral		= Column("Ancestral", COLUMN_ANCESTRAL)
Derived			= Column("Derived", COLUMN_DERIVED)
SNPReference	= Column("SNPReference", COLUMN_REFERENCE)
Date			= Column("Date", COLUMN_DATE)
ChromID			= Column("ChromID", COLUMN_CHROMOSOME_ID)
Chromosome		= Column("Chromosome", COLUMN_CHROMOSOME)
GenomeID		= Column("GenomeID", COLUMN_GENOME_ID)
Genome			= Column("Genome", COLUMN_GENOME)
Strain			= Column("Strain", COLUMN_STRAIN)
GenbankID		= Column("GenbankID", COLUMN_GENBANK)
RefseqID		= Column("RefseqID", COLUMN_REFSEQ)
Assembly		= Column("Assembly", COLUMN_ASSEMBLY)

class TreeColumns: pass
class SNPColumns: pass
class ChromosomesColumns: pass
class ReferencesColumns: pass
TreeColumns			= Literal[Parent, NodeID, GenoType] # type: ignore
SNPColumns			= Literal[NodeID, Position, Ancestral, Derived, SNPReference, Date, ChromID] # type: ignore
ChromosomesColumns	= Literal[ChromID, Chromosome, GenomeID] # type: ignore
ReferencesColumns	= Literal[GenomeID, Genome, Strain, GenbankID, RefseqID, Assembly] # type: ignore

COLUMN_LOOKUP = {
	"ALL"			: ALL,
	"Parent"		: Parent,
	"NodeID"		: NodeID,
	"GenoType"		: GenoType,
	"Position"		: Position,
	"Ancestral"		: Ancestral,
	"Derived"		: Derived,
	"SNPReference"	: SNPReference,
	"Date"			: Date,
	"ChromID"		: ChromID,
	"Chromosome"	: Chromosome,
	"GenomeID"		: GenomeID,
	"Genome"		: Genome,
	"Strain"		: Strain,
	"GenbankID"		: GenbankID,
	"RefseqID"		: RefseqID,
	"Assembly"		: Assembly
}

"""

LOOKUP : dict[str,dict[Column, str]] = {
	TABLE_NAME_TREE : {
		ALL			: "*",
		Parent		: COLUMN_PARENT,
		NodeID		: COLUMN_NODE_ID,
		NodeID		: COLUMN_NODE_ID,
		GenoType	: COLUMN_NAME
	},
	TABLE_NAME_SNP_ANNOTATION : {
		ALL				: "*",
		NodeID			: COLUMN_NODE_ID,
		Position		: COLUMN_POSITION,
		Ancestral		: COLUMN_ANCESTRAL,
		Derived			: COLUMN_DERIVED,
		SNPReference	: COLUMN_REFERENCE,
		Date			: COLUMN_DATE,
		ChromID			: COLUMN_CHROMOSOME_ID
	},
	TABLE_NAME_CHROMOSOMES : {
		ALL			: "*",
		ChromID		: COLUMN_ID,
		Chromosome	: COLUMN_NAME,
		GenomeID	: COLUMN_GENOME_ID
	},
	TABLE_NAME_REFERENCES : {
		ALL			: "*",
		GenomeID	: COLUMN_GENOME_ID,
		Genome		: COLUMN_GENOME,
		Strain		: COLUMN_STRAIN,
		GenbankID	: COLUMN_GENBANK,
		RefseqID	: COLUMN_REFSEQ,
		Assembly	: COLUMN_ASSEMBLY
	}
}

UNIQUES = set(LOOKUP[TABLE_NAME_REFERENCES]).difference(LOOKUP[TABLE_NAME_CHROMOSOMES], LOOKUP[TABLE_NAME_SNP_ANNOTATION], LOOKUP[TABLE_NAME_TREE])
UNIQUELOOKUP = {
	col : [table for table in LOOKUP if col in LOOKUP[table]][0] for col in UNIQUES
}
COMMONS = set(LOOKUP[TABLE_NAME_REFERENCES]).intersection(LOOKUP[TABLE_NAME_CHROMOSOMES], LOOKUP[TABLE_NAME_SNP_ANNOTATION], LOOKUP[TABLE_NAME_TREE])
COMMONLOOKUP = {
	col : {table for table in LOOKUP if col in LOOKUP[table]} for col in COMMONS
}
"""

RELATIONS : dict[tuple[str,str],Column] = {
	#	FROM			->			TO
	(TABLE_NAME_TREE, TABLE_NAME_SNP_ANNOTATION) : NodeID,
	(TABLE_NAME_SNP_ANNOTATION, TABLE_NAME_TREE) : NodeID,
	
	(TABLE_NAME_CHROMOSOMES, TABLE_NAME_SNP_ANNOTATION) : ChromID,
	(TABLE_NAME_SNP_ANNOTATION, TABLE_NAME_CHROMOSOMES) : ChromID,
	
	(TABLE_NAME_REFERENCES, TABLE_NAME_CHROMOSOMES) : GenomeID,
	(TABLE_NAME_CHROMOSOMES, TABLE_NAME_REFERENCES) : GenomeID,
	
	(TABLE_NAME_REFERENCES, TABLE_NAME_SNP_ANNOTATION) : GenomeID,
	(TABLE_NAME_SNP_ANNOTATION, TABLE_NAME_REFERENCES) : ChromID,
}

RELATIONSHIPS : dict[str,dict[Column, str]]= {
	TABLE_NAME_TREE : {
		Position		: TABLE_NAME_SNP_ANNOTATION,
		Ancestral		: TABLE_NAME_SNP_ANNOTATION,
		Derived			: TABLE_NAME_SNP_ANNOTATION,
		SNPReference	: TABLE_NAME_SNP_ANNOTATION,
		Date			: TABLE_NAME_SNP_ANNOTATION,
		ChromID			: TABLE_NAME_SNP_ANNOTATION,
		
		Chromosome		: TABLE_NAME_SNP_ANNOTATION,
		GenomeID		: TABLE_NAME_SNP_ANNOTATION,

			Genome		: TABLE_NAME_SNP_ANNOTATION,
			Strain		: TABLE_NAME_SNP_ANNOTATION,
			GenbankID	: TABLE_NAME_SNP_ANNOTATION,
			RefseqID	: TABLE_NAME_SNP_ANNOTATION,
			Assembly	: TABLE_NAME_SNP_ANNOTATION
	},
	TABLE_NAME_SNP_ANNOTATION : {
		GenoType		: TABLE_NAME_TREE,
		Parent			: TABLE_NAME_TREE,
		NodeID			: TABLE_NAME_TREE,
		
		Chromosome		: TABLE_NAME_CHROMOSOMES,
		GenomeID		: TABLE_NAME_CHROMOSOMES,
		
		Genome			: TABLE_NAME_CHROMOSOMES,
		Strain			: TABLE_NAME_CHROMOSOMES,
		GenbankID		: TABLE_NAME_CHROMOSOMES,
		RefseqID		: TABLE_NAME_CHROMOSOMES,
		Assembly		: TABLE_NAME_CHROMOSOMES,
	},
	TABLE_NAME_CHROMOSOMES : {
		NodeID			: TABLE_NAME_SNP_ANNOTATION,
		Position		: TABLE_NAME_SNP_ANNOTATION,
		Ancestral		: TABLE_NAME_SNP_ANNOTATION,
		Derived			: TABLE_NAME_SNP_ANNOTATION,
		SNPReference	: TABLE_NAME_SNP_ANNOTATION,
		Date			: TABLE_NAME_SNP_ANNOTATION,
		
		Genome		: TABLE_NAME_REFERENCES,
		Strain		: TABLE_NAME_REFERENCES,
		GenbankID	: TABLE_NAME_REFERENCES,
		RefseqID	: TABLE_NAME_REFERENCES,
		Assembly	: TABLE_NAME_REFERENCES
	},
	TABLE_NAME_REFERENCES : {
		ChromID			: TABLE_NAME_CHROMOSOMES,
		Chromosome		: TABLE_NAME_CHROMOSOMES,
		
		NodeID			: TABLE_NAME_CHROMOSOMES,
		Position		: TABLE_NAME_CHROMOSOMES,
		Ancestral		: TABLE_NAME_CHROMOSOMES,
		Derived			: TABLE_NAME_CHROMOSOMES,
		SNPReference	: TABLE_NAME_CHROMOSOMES,
		Date			: TABLE_NAME_CHROMOSOMES,
		GenoType		: TABLE_NAME_CHROMOSOMES,
		Parent		: TABLE_NAME_CHROMOSOMES,
		NodeID		: TABLE_NAME_CHROMOSOMES,
	}
}