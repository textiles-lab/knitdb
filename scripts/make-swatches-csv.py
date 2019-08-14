import os
import csv
import subprocess

# This script will download
#
#


#based on: https://realpython.com/python-csv/#parsing-csv-files-with-pythons-built-in-csv-library

out_file = open('../swatches.csv', 'wb')

headers = [
	'datID',
	'datPos',
	'patternName',
	'simpleName',
	'Source',
	'Second Measurement?',
	'Mass (g)',
	'Relaxed Width (mm)',
	'Relaxed Height (mm)',
	'Stretched Width (mm)',
	'Stretched Height (mm)',
	'Note',
#	'Chart File',
#	'Knitout File',
#	'Relaxed Photo Raw File',
#	'Stretched Light Photo Raw File',
#	'Stretched Dark Photo Raw File'
]

CRLF = '\r\n'

header_index = dict()
for i in range(0, len(headers)):
	header_index[headers[i]] = i

out_file.write(('"' + '","'.join(headers) + '"' + CRLF).encode('utf8'))

patterns = set()
names = set()

with open('Swatch Log - Reorganized.csv', 'r') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')
	line_count = 0
	for row in csv_reader:
		line_count += 1
		if line_count <= 8: continue

		out_row = [""] * len(headers)
			
		datID = row[1]
		datPos = row[2]
		patternName = row[3]
		weight = row[5]
		widthRelaxed = row[6]
		heightRelaxed = row[7]
		widthStretched = row[8]
		heightStretched = row[9]
		note = row[10]
		source = row[13]

		if widthRelaxed == "" or widthStretched == "": continue

		out_row = [""] * len(headers)

		#simplify pattern name:
		simpleName = patternName

		#remove everything after '_' (looks like: [0-9a-f]{40}?_out.chart)
		simpleName = simpleName[0:simpleName.find('_')]

		#these would be nice, but it's hard/impossible to rename google drive files from the command line...
		##remove spaces:
		#simpleName = simpleName.replace(' ','')

		#remove the single non-low-ASCII character in the data set:
		simpleName = simpleName.replace('Ñ','a')
		simpleName.encode('ascii') #just check that this works

		def quote(s):
			if s == "": return s
			ret = s.replace('"', '""')
			return '"' + ret + '"'

		out_row[header_index['datID']] = datID
		out_row[header_index['datPos']] = datPos
		out_row[header_index['patternName']] = quote(patternName)
		out_row[header_index['Source']] = source
		if datID == "" and datPos == "":
			out_row[header_index['Second Measurement?']] = "yes"
			is_second = True
		else:
			assert(not (patternName in patterns))
			patterns.add(patternName)
			assert(not (simpleName in names))
			names.add(simpleName)
			out_row[header_index['simpleName']] = quote(datID + "_" + datPos + "_" + simpleName)
		#	out_row[header_index['Chart File']] = quote("charts/" + simpleName + ".chart")
		#	out_row[header_index['Knitout File']] = quote("knitouts/" + simpleName + ".knitout")
		#	out_row[header_index['Relaxed Photo Raw File']] = quote("photos/relaxed/" + simpleName + ".NEF")
		#	out_row[header_index['Stretched Light Photo Raw File']] = quote("photos/stretched/" + simpleName + "_light.NEF")
		#	out_row[header_index['Stretched Dark Photo Raw File']] = quote("photos/stretched/" + simpleName + "_dark.NEF")

		out_row[header_index['Mass (g)']] = weight
		out_row[header_index['Relaxed Width (mm)']] = widthRelaxed
		out_row[header_index['Relaxed Height (mm)']] = heightRelaxed
		out_row[header_index['Stretched Width (mm)']] = widthStretched
		out_row[header_index['Stretched Height (mm)']] = heightStretched


		out_row[header_index['Note']] = quote(note)

		out_file.write((','.join(out_row) + CRLF).encode('utf8'))

out_file.close()

print("Wrote " + str(len(patterns)) + " patterns to '../swatches.csv'.")
