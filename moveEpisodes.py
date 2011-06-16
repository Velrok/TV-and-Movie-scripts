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
	
# get source file or directory from argument 1
src = sys.argv[1]
# get destination directory from argument 2
dest = sys.argv[2]

# tvnamer default pattern
pattern = '([\w ]*) - \[(\d+)x(\d+)\] (.*)'
reg_ex = re.compile(pattern)


def move(filename):
	"""
	Moves the given filename into the destination dir. Creating subdirectorys for
	series name and season.
	"""
	m = re.search(reg_ex, filename)
	name = m.group(1)	# get series name
	season = "Season"
	season += m.group(2) # get season number
	
	destination_directory = os.path.join(dest, name, season)	#create desination path
	target = os.path.join(destination_directory, filename)		#create target filename
	src_file = os.path.join(src, filename)										#get source filename
	
	# if destination dir doesn't exist create it
	if(not os.path.exists(destination_directory)):
		os.makedirs(destination_directory)
	#os.link(src_file,target)
	
	shutil.move(src_file, target)		# move the file
	
## end of move function


if(os.path.isfile(src)):
	# source is a single file get and move it
	filename = os.path.basename(src)
	move(filename)
	
elif(os.path.isdir(src)):
	# source is a directoy, look for all none hidden files and move them one by one
	dir_list = os.listdir(src)
	for f in dir_list:
		if f[0] == '.':
			continue # skip hidden files
		else:
			move(f)