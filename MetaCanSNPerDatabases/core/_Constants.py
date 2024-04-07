


TABLE_NAME_SNP_ANNOTATION	= "snp_annotation"
TABLE_NAME_REFERENCES		= "snp_references"
TABLE_NAME_TREE				= "tree"
TABLE_NAME_CHROMOSOMES		= "chromosomes"

TABLES = [TABLE_NAME_SNP_ANNOTATION, TABLE_NAME_REFERENCES, TABLE_NAME_TREE, TABLE_NAME_CHROMOSOMES]

COLUMN_PARENT				= "parent"
COLUMN_GENOTYPE				= "name"
COLUMN_NODE_ID				= "node_id"
COLUMN_POSITION				= "position"
COLUMN_ANCESTRAL			= "ancestral_base"
COLUMN_DERIVED				= "derived_base"
COLUMN_REFERENCE			= "reference"
COLUMN_DATE					= "date"
COLUMN_CHROMOSOME_ID		= "chromosome_id"
COLUMN_CHROMOSOME			= "chromosome"
COLUMN_GENOME_ID			= "genome_id"
COLUMN_GENOME				= "genome"
COLUMN_STRAIN				= "strain"
COLUMN_GENBANK				= "genbank_id"
COLUMN_REFSEQ				= "refseq_id"
COLUMN_ASSEMBLY				= "assembly_name"

TREE_COLUMN_TYPES = {
    COLUMN_PARENT				: ("INTEGER", "NOT NULL"	),
	COLUMN_NODE_ID				: ("INTEGER", "UNIQUE"		),
	COLUMN_GENOTYPE				: ("TEXT", "NOT NULL"		)
}

SNP_COLUMN_TYPES = {
    COLUMN_NODE_ID				: ("INTEGER",			),
	COLUMN_POSITION				: ("INTEGER", "UNIQUE"	),
	COLUMN_ANCESTRAL			: ("VARCHAR(1)",		),
	COLUMN_DERIVED				: ("VARCHAR(1)",		),
	COLUMN_REFERENCE			: ("VARCHAR(20)",		),
	COLUMN_DATE					: ("DATETIME",			),
	COLUMN_CHROMOSOME_ID		: ("INTEGER",			)
}

CHROMOSOMES_COLUMN_TYPES = {
	COLUMN_CHROMOSOME_ID		: ("INTEGER", "UNIQUE"			),
	COLUMN_CHROMOSOME			: ("VARCHAR(30)", "NOT NULL"	),
	COLUMN_GENOME_ID			: ("INTEGER", "NOT NULL"		)
}

REFERENCES_COLUMN_TYPES = {
    COLUMN_GENOME_ID			: ("INTEGER", "UNIQUE"		),
	COLUMN_GENOME				: ("VARCHAR(30)",			),
	COLUMN_STRAIN				: ("VARCHAR(30)",			),
	COLUMN_GENBANK				: ("VARCHAR(30)", "UNIQUE"	),
	COLUMN_REFSEQ				: ("VARCHAR(30)", "UNIQUE"	),
	COLUMN_ASSEMBLY				: ("VARCHAR(30)", "UNIQUE"	)
}

TYPE_LOOKUP = {
	TABLE_NAME_TREE : TREE_COLUMN_TYPES,
	TABLE_NAME_SNP_ANNOTATION : SNP_COLUMN_TYPES,
	TABLE_NAME_CHROMOSOMES : CHROMOSOMES_COLUMN_TYPES,
	TABLE_NAME_REFERENCES : REFERENCES_COLUMN_TYPES
}

SNP_APPEND = [
    f"PRIMARY KEY ({COLUMN_CHROMOSOME_ID}, {COLUMN_POSITION}, {COLUMN_NODE_ID})",
	f"FOREIGN KEY ({COLUMN_CHROMOSOME_ID}) REFERENCES {TABLE_NAME_CHROMOSOMES} ({COLUMN_CHROMOSOME_ID})",
    f"FOREIGN KEY ({COLUMN_NODE_ID}) REFERENCES {TABLE_NAME_TREE} ({COLUMN_NODE_ID})"
]
REFERENCE_APPEND = []
TREE_APPEND = [
    f"PRIMARY KEY {COLUMN_NODE_ID}",
	f"UNIQUE ({COLUMN_PARENT}, {COLUMN_NODE_ID})"
]
CHROMOSOMES_APPEND = [
	f"PRIMARY KEY ({COLUMN_CHROMOSOME_ID}, {COLUMN_GENOME_ID})",
	f"FOREIGN KEY ({COLUMN_GENOME_ID}) REFERENCES {TABLE_NAME_REFERENCES} ({COLUMN_GENOME_ID})"
	]

# INDEX = (NAME, COLUMN_1, COLUMN_2, ..., COLUMN_N)
SNP_INDEXES = [
	(f"{TABLE_NAME_SNP_ANNOTATION}By{COLUMN_POSITION.capitalize()}",		COLUMN_POSITION),
	(f"{TABLE_NAME_SNP_ANNOTATION}By{COLUMN_CHROMOSOME_ID.capitalize()}",	COLUMN_CHROMOSOME_ID),
	(f"{TABLE_NAME_SNP_ANNOTATION}By{COLUMN_NODE_ID.capitalize()}",			COLUMN_NODE_ID)
]
REFERENCE_INDEXES = [
	(f"{TABLE_NAME_REFERENCES}By{COLUMN_GENOME.capitalize()}",				COLUMN_GENOME),
	(f"{TABLE_NAME_REFERENCES}By{COLUMN_ASSEMBLY.capitalize()}",			COLUMN_ASSEMBLY),
]
TREE_INDEXES = [
	(f"{TABLE_NAME_TREE}By{COLUMN_PARENT.capitalize()}",					COLUMN_PARENT),
	(f"{TABLE_NAME_TREE}By{COLUMN_NODE_ID.capitalize()}",					COLUMN_NODE_ID),
]
CHROMOSOMES_INDEXES = [
	(f"{TABLE_NAME_CHROMOSOMES}By{COLUMN_CHROMOSOME_ID.capitalize()}",		COLUMN_CHROMOSOME_ID),
	(f"{TABLE_NAME_CHROMOSOMES}By{COLUMN_CHROMOSOME.capitalize()}",			COLUMN_CHROMOSOME),
	(f"{TABLE_NAME_CHROMOSOMES}By{COLUMN_GENOME_ID.capitalize()}",			COLUMN_GENOME_ID)
]