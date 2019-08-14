#!/usr/bin/env python3

import os
import subprocess
import threading
import queue

knitouts_dir = '../knitouts'
smobjs_dir = '../smobjs'

to_process = []

for dir_name, subdir_list, file_list in os.walk(knitouts_dir):
	for f in file_list:
		if f[-8:] == '.knitout':
			to_process.append(dir_name + '/' + f)


to_process.sort()
print("Will create " + str(len(to_process)) + " smobj files from knitouts.")

queue = queue.Queue()

def worker():
	print("hello from worker thread")
	while True:
		try:
			index_path = queue.get(block=False)
		except:
			break
		i = index_path[0]
		knitout_file = index_path[1]

		smobj_file = smobjs_dir + knitout_file[len(knitouts_dir):-8] + ".smobj"
		print("[" + str(i) + "/" + str(len(to_process)) + "]: " + knitout_file + " -> " + smobj_file)
		subprocess.run(["../../smobj/utilities/knitout-to-smobj", "--compact", "--", knitout_file, smobj_file], check=True)

		queue.task_done()


i = 0
for knitout_file in to_process:
	i += 1
	queue.put((i, knitout_file))

count = os.cpu_count()
print("Spawning " + str(count) + " workers.")
for w in range(0, count):
	threading.Thread(target=worker).start()

queue.join()
print("Done.")
