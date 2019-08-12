import os
import csv
import subprocess

#based on: https://realpython.com/python-csv/#parsing-csv-files-with-pythons-built-in-csv-library

names = set()

with open('swatches.csv') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')
	line_count = 0
	for row in csv_reader:
		if line_count >= 8:
			datID = row[1]
			datPos = row[2]
			patternName = row[3]
			weight = row[5]
			widthRelaxed = row[6]
			heightRelaxed = row[7]
			widthStretched = row[8]
			heightStretched = row[9]
			if widthRelaxed != "" and widthStretched != "":
				#print(patternName + " " + weight + " " + widthRelaxed + " " + heightRelaxed + " " + widthStretched + " " + heightStretched)
				if patternName in names:
					print("Duplicate name: " + patternName)
				names.add(patternName)

		line_count += 1

print("Have " + str(len(names)) + " names.")

paths = dict()

ignored = set()

for name in names:
	paths[name] = list()

#based on: https://www.pythoncentral.io/how-to-traverse-a-directory-tree-in-python-guide-to-os-walk/

def getCharts(root):
	for dir_name, subdir_list, file_list in os.walk(root):
		for f in file_list:
			if f in paths:
				paths[f].append(dir_name + '/' + f)
			else:
				ignored.add(f)

getCharts('src-older')
getCharts('src-newer')

no_paths = 0
one_path = 0
many_paths = 0
for l in paths.values():
	if len(l) == 0:
		no_paths += 1
	elif len(l) == 1:
		one_path += 1
	else:
		many_paths += 1

print("Ignored " + str(len(ignored)) + " names.")
print("Have " + str(no_paths) + " charts with no paths, " + str(one_path) + " with one path, and " + str(many_paths) + " with more than one path.")


for kv in paths.items():
	chart = kv[0]
	paths = kv[1]
	if len(paths) == 0:
		print("WARNING: '" + chart + "' not found in *any* charts folder.")
		next
	if len(paths) > 1:
		sums = set()
		for path in paths:
			out = subprocess.run(["sha256sum",path],capture_output=True).stdout
			s = out.split(b' ')[0].decode('utf8')
			sums.add(s)
		if len(sums) > 1:
			print("NOTE: '" + chart + "' has " + str(len(sums)) + " versions:\n" + "\n".join(paths))
		paths = [paths.pop()] #use last path
	assert(len(paths) == 1)
	subprocess.run(["cp",paths[0],'combined/'])
