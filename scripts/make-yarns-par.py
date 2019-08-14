#!/usr/bin/env python3

import os
import subprocess
import threading
import queue

smobjs_dir = '../smobjs'
yarns_dir = '../yarns'

to_process = []

for dir_name, subdir_list, file_list in os.walk(smobjs_dir):
	for f in file_list:
		if f[-6:] == '.smobj':
			to_process.append(dir_name + '/' + f)


to_process.sort()
print("Will create " + str(len(to_process)) + " yarns files from smobjs.")

queue = queue.Queue()

def worker():
	print("hello from worker thread")
	while True:
		try:
			index_path = queue.get(block=False)
		except:
			break
		i = index_path[0]
		smobj_file = index_path[1]
		yarns_file = yarns_dir + smobj_file[len(smobjs_dir):-6] + ".yarns"
		#if os.path.exists(yarns_file) and os.path.getmtime(yarns_file) >= os.path.getmtime(smobj_file):
		#	skipped += 1
		#	continue
		
		print("[" + str(i) + "/" + str(len(to_process)) + "]: " + smobj_file + " -> " + yarns_file)
		subprocess.run(["../../smobj/utilities/smobj-to-yarns", smobj_file, "../../smobj/faces/knitout.sf", yarns_file], check=True)
		queue.task_done()

i = 0
for smobj_file in to_process:
	i += 1
	queue.put((i, smobj_file))

count = os.cpu_count()
print("Spawning " + str(count) + " workers.")
for w in range(0, count):
	threading.Thread(target=worker).start()

queue.join()
print("Done.")
