#!/usr/bin/env python3

import os
import subprocess

smobjs_dir = '../smobjs'
yarns_dir = '../yarns'

to_process = []

for dir_name, subdir_list, file_list in os.walk(smobjs_dir):
	for f in file_list:
		if f[-6:] == '.smobj':
			to_process.append(dir_name + '/' + f)


to_process.sort()
print("Will create " + str(len(to_process)) + " yarns files from smobjs.")

skipped = 0
i = 0
for smobj_file in to_process:
	i += 1
	yarns_file = yarns_dir + smobj_file[len(smobjs_dir):-6] + ".yarns"
	if os.path.exists(yarns_file) and os.path.getmtime(yarns_file) >= os.path.getmtime(smobj_file):
		skipped += 1
		continue
	print("[" + str(i) + "/" + str(len(to_process)) + "]: " + smobj_file + " -> " + yarns_file)
	subprocess.run(["../../smobj/utilities/smobj-to-yarns", smobj_file, "../../smobj/faces/knitout.sf", yarns_file], check=True)

if skipped != 0:
	print("NOTE: skipped " + str(skipped) + " files because yarns file existed and was newer than smobj file.")
