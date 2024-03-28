


TABLE_NAME_SNP_ANNOTATION	= "snp_annotation"
TABLE_NAME_REFERENCES		= "snp_references"
TABLE_NAME_NODES			= "nodes"
TABLE_NAME_TREE				= "tree"
TABLE_NAME_RANKS			= "rank"
TABLE_NAME_GENOMES			= "genomes"

TABLES = [TABLE_NAME_SNP_ANNOTATION, TABLE_NAME_REFERENCES, TABLE_NAME_NODES, TABLE_NAME_TREE, TABLE_NAME_RANKS, TABLE_NAME_GENOMES]

SNP_COLUMN_NODE_ID,			SNP_COLUMN_NODE_ID_TYPE				= "node_id",		("INTEGER",					)
SNP_COLUMN_SNP_ID,			SNP_COLUMN_SNP_ID_TYPE				= "snp_id",			("VARCHAR(6)", "PRIMARY KEY")
SNP_COLUMN_POSITION,		SNP_COLUMN_POSITION_TYPE			= "position",		("INTEGER",					)
SNP_COLUMN_ANCESTRAL,		SNP_COLUMN_ANCESTRAL_TYPE			= "ancestral_base",	("VARCHAR(1)",				)
SNP_COLUMN_DERIVED,			SNP_COLUMN_DERIVED_TYPE				= "derived_base",	("VARCHAR(1)",				)
SNP_COLUMN_REFERENCE,		SNP_COLUMN_REFERENCE_TYPE			= "reference",		("VARCHAR(20)",				)
SNP_COLUMN_DATE,			SNP_COLUMN_DATE_TYPE				= "date",			("DATETIME",				)
SNP_COLUMN_GENOME_ID,		SNP_COLUMN_GENOME_ID_TYPE			= "genome_i",		("INTEGER",					)

REFERENCE_COLUMN_GENOME_ID,	REFERENCE_COLUMN_GENOME_ID_TYPE		= "id",				("INTEGER", "PRIMARY KEY"	)
REFERENCE_COLUMN_GENOME,	REFERENCE_COLUMN_GENOME_TYPE		= "genome",			("VARCHAR(6)",				)
REFERENCE_COLUMN_STRAIN,	REFERENCE_COLUMN_STRAIN_TYPE		= "strain",			("VARCHAR(200)",			)
REFERENCE_COLUMN_GENBANK,	REFERENCE_COLUMN_GENBANK_TYPE		= "genbank_id",		("VARCHAR(20)",				)
REFERENCE_COLUMN_REFSEQ,	REFERENCE_COLUMN_REFSEQ_TYPE		= "refseq_id",		("VARCHAR(20)",				)
REFERENCE_COLUMN_ASSEMBLY,	REFERENCE_COLUMN_ASSEMBLY_TYPE		= "assembly_name",	("VARCHAR(200)",			)

NODE_COLUMN_ID,				NODE_COLUMN_ID_TYPE					= "id",				("INTEGER","PRIMARY KEY"	)
NODE_COLUMN_NAME,			NODE_COLUMN_NAME_TYPE				= "name",			("TEXT","NOT NULL"			)

TREE_COLUMN_PARENT,			TREE_COLUMN_PARENT_TYPE				= "parent",			("INTEGER", "NOT NULL"		)
TREE_COLUMN_CHILD,			TREE_COLUMN_CHILD_TYPE				= "child",			("INTEGER",					)
TREE_COLUMN_RANK,			TREE_COLUMN_RANK_TYPE				= "rank_i",			("INTEGER",					)

RANKS_COLUMN_ID,			RANKS_COLUMN_ID_TYPE				= "rank_i",			("INTEGER", "PRIMARY KEY"	)
RANKS_COLUMN_RANK,			RANKS_COLUMN_RANK_TYPE				= "rank",			("VARCHAR(15)",				)

GENOMES_COLUMN_ID,			GENOMES_COLUMN_ID_TYPE				= "id",				("INTEGER", "NOT NULL"		)
GENOMES_COLUMN_NAME,		GENOMES_COLUMN_NAME_TYPE			= "genome",			("TEXT", "NOT NULL"			)