

from MetaCanSNPer.modules.Databases import *


def runTest():
	mode = input("Create or read from database? [w/r]: ").strip()

	match mode:
		case "r":
			database = openDatabase(input("Database path: ").strip(), "r")

			print(database.SNPTable)
			print(database.ReferenceTable)
			print(database.NodeTable)
			print(database.TreeTable)
			print(database.RankTable)
			print(database.GenomesTable)
		case "w":
			database = openDatabase(input("Database path: ").strip(), "w")

			print(database.SNPTable)
			print(database.ReferenceTable)
			print(database.NodeTable)
			print(database.TreeTable)
			print(database.RankTable)
			print(database.GenomesTable)

			database.commit()
	print("Test complete!")
