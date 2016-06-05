#!/usr/bin/python

import sys
from random import randint

PRINT_LATEX = True

disease_list = [ "Arthrose", "Bronchitis", "Demenz", "Epilepsie", "Gicht", "Hepatitis", "Masern", "Osteoporose", "Diabetes"]

female_firstname_list = ["Mia", "Emma", "Hanna", "Sofia", "Anna", "Emilia"]
male_firstname_list = ["Ben", "Jonas", "Leon", "Elias", "Finn", "Noah"]

lastname_list = ["Müller", "Schmidt", "Schneider", "Fischer", "Weber", "Meyer", "Wagner", "Becker", "Schulz", "Hoffmann", "Schäfer", "Koch"]

if (len(sys.argv) != 2) :
	print("Please pass the number of rows to be generated as an argument")
	quit()
else :
	table_entries = int(sys.argv[1])

result = []
for i in range(0, table_entries):
	disease = disease_list[randint(0, len(disease_list) - 1)]
	lastname = lastname_list[randint(0, len(lastname_list) - 1)]
	if (i < (table_entries / 2)) :
		firstname = female_firstname_list[randint(0, len(female_firstname_list) - 1)]
	else :
		firstname = male_firstname_list[randint(0, len(male_firstname_list) - 1)]
	postal_code = "2" + str(2) + str(randint(0, 9)) + str(randint(0, 9)) + str(randint(0, 9)) 
	date_of_birth = "" + str(randint(1, 28)) + "." + str(randint(1, 12)) + "." + str(randint(1920, 1999))
	
	result.append((firstname + " " + lastname, str(0 if (i < (table_entries / 2)) else 1), postal_code, date_of_birth, disease))

for i in range(0, len(result)) :
	print(str(i) + " " + str(result[i]))
print("")

if (PRINT_LATEX) : 
	output = ""
	output += """\\begin{tabular}{|l|c|c|r|l|}
\\hline \\textbf{Identifier} & \\multicolumn{3}{c|}{\\textbf{Nicht-sensibel}} & \\textbf{Sensibel} \\\\ 
\\hline \\textbf{Name} & \\textbf{Geschlecht} & \\textbf{PLZ} & \\textbf{Geburtsdatum} & \\textbf{Erkrankung} \\\\
\\hline """
	for tuple in result :
		output += "\hline " + tuple[0] + " & " + ("w" if (tuple[1] == "0") else "m") + " & " + tuple[2] + " & " + tuple[3] + " & " + tuple[4] + " \\\\ \n"
	output += """\hline 
\end{tabular}"""
	f = open('patient_table.tex', 'w')
	f.write(output)
	f.close()