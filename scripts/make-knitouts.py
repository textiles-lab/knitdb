#!/usr/bin/env python3

import os
import subprocess

charts_dir = '../charts'
knitouts_dir = '../knitouts'

to_process = []

for dir_name, subdir_list, file_list in os.walk(charts_dir):
	for f in file_list:
		if f[-6:] == '.chart':
			to_process.append(dir_name + '/' + f)


to_process.sort()
print("Will create " + str(len(to_process)) + " knitout files from charts.")

i = 0
for chart_file in to_process:
	i += 1
	knitout_file = knitouts_dir + chart_file[len(charts_dir):-6] + ".knitout"
	print("[" + str(i) + "/" + str(len(to_process)) + "]: " + chart_file + " -> " + knitout_file)
	subprocess.run(["../../knitdb_tomachine/chartToDat.js", chart_file, knitout_file], check=True)
