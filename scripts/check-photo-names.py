import os
import csv
import subprocess
import re

#based on: https://realpython.com/python-csv/#parsing-csv-files-with-pythons-built-in-csv-library

names = set()

relaxed_names = set()
stretched_names = set()

with open('../swatches.csv') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')
	headers = next(csv_reader)
	for row in csv_reader:
		datID = row[0]
		datPos = row[1]
		patternName = row[2]
		isSecond = row[4]

		if isSecond == "yes":
			continue

		simpleName = patternName[0:patternName.find('_')]

		assert(not ('_' in simpleName))

		if simpleName in names:
			print("Duplicate name: " + simpleName)
		names.add(simpleName)

		relaxed_names.add(datID + "_" + datPos + "_" + simpleName + "")
		stretched_names.add(datID + "_" + datPos + "_" + simpleName + "_light")
		stretched_names.add(datID + "_" + datPos + "_" + simpleName + "_dark")

print("Have " + str(len(names)) + " names.")

relaxed_found = set()

print("------ relaxed ------")

with open('relaxed.list') as list_file:
	for line in list_file:
		line = re.split(r'\s+', line)
		name = ' '.join(line[1:-6])

		if name[-4:] != ".NEF":
			print("Skipping non-NEF: '" + name + "'")
			next
		name = name[0:-4]

		base = name.split('.')
		ext = ''
		if len(base) == 1:
			base = base[0]
		elif len(base) == 2:
			ext = base[1]
			base = base[0]
		else:
			print(name)
			assert(len(base) <= 2)

		if base in relaxed_names:
			if name in relaxed_found:
				print("Duplicated relaxed image: " + name)
			relaxed_found.add(name)
			if ext == 'A':
				relaxed_found.add(base)
		elif base[0:4] == "DSC_":
			pass #ignore camera-named images
		else:
			print("Name not found: " + name)

missing = []
for name in relaxed_names:
	if not name in relaxed_found:
		missing.append(name)

missing.sort()
print("Missing " + str(len(missing)) + ":\n " + "\n ".join(missing))


print("------ stretched ------")

stretched_found = set()

with open('stretched.list') as list_file:
	for line in list_file:
		line = re.split(r'\s+', line)
		name = ' '.join(line[1:-6])

		#can't figure out how to make gdrive not do this so, since this is the longest name:
		if name == "13_1_045DoubleInter...dLattice_light.NEF":
			name = "13_1_045DoubleInterlacedLattice_light.NEF"

		if name[-4:] != ".NEF":
			print("Skipping non-NEF: '" + name + "'")
			next
		name = name[0:-4]

		base = name.split('.')
		ext = ''
		if len(base) == 1:
			base = base[0]
		elif len(base) == 2:
			ext = base[1]
			base = base[0]
		else:
			print(name)
			assert(len(base) <= 2)

		if base in stretched_names:
			if name in stretched_found:
				print("Duplicated stretched image: " + name)
			stretched_found.add(name)
			if ext == 'A':
				stretched_found.add(base)
		elif base[0:4] == "DSC_":
			pass #ignore camera-named images
		else:
			print("Name not found: " + name)

missing = []
for name in stretched_names:
	if not name in stretched_found:
		missing.append(name)

missing.sort()
print("Missing " + str(len(missing)) + ":\n " + "\n ".join(missing))

