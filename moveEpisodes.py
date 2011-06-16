#!/usr/bin/python
import re
import sys
import os.path
import os
import shutil
	
if( len(sys.argv) == 1 or '-h' in sys.argv or '--help' in sys.argv):
	print """Usage: moveEpisodes.py <src_dir / src_file> <dest_dir>
	
This script moves all files in src_dir into subfolders of dest_dir, creating 
a subfolder for each Season. Season01, Season02 ...

Requirements:
	This scripts requires the series to be named following this pattern:
	<series name> - [<season number>x<episode number>] - <some string>
		
Options:
	-h --help	Prints this help message.
"""
	sys.exit()
	
	
src = sys.argv[1]
dest = sys.argv[2]

pattern = '([\w ]*) - \[(\d+)x(\d+)\] (.*)'
reg_ex = re.compile(pattern)

def move(filename):
#	print src_file
	m = re.search(reg_ex, filename)
	name = m.group(1)
	season = "Season"
	season += m.group(2)
	
	destination_directory = os.path.join(dest, name, season)
	target = os.path.join(destination_directory, filename)
	src_file = os.path.join(src, filename)
	
	if(not os.path.exists(destination_directory)):
		os.makedirs(destination_directory)
	#os.link(src_file,target)
	shutil.move(src_file, target)


if(os.path.isfile(src)):
	filename = os.path.basename(src)
	
elif(os.path.isdir(src)):
	dir_list = os.listdir(src)
	for f in dir_list:
		if f[0] == '.':
			continue # skip hidden files
		else:
			move(f)