

from SQLOOP._core.Aggregates import *
from SQLOOP._core.Databases import *
from SQLOOP._core.Exceptions import *
from SQLOOP._core.Expressions import *
from SQLOOP._core.Functions import *
from SQLOOP._core.Schema import *
from SQLOOP._core.Structures import *
from SQLOOP._core.Tree import *
from SQLOOP._core.Types import *
from SQLOOP._core.Words import *

# from SQLOOP._core.Structures import *
# from SQLOOP._core.Schema import *
# from SQLOOP._core.Aggregates import *
# from SQLOOP._core.Words import *
# from SQLOOP._core.Tree import *
# from SQLOOP._core.Functions import *
# from SQLOOP._core.Exceptions import *
# from SQLOOP._core.Databases import *

def newColumn(name : str|Column, table : type[Table]=None):
	return SQLStructure(name if isinstance(name, str) else str(name), (LinkedColumn,), {}, table=table)

def createTempTable() -> type[Table]:
	class TempTable(Table):
		
		__sql_name__ = f"TempTable_{random.randint(0, 1<<32)}"
	return TempTable