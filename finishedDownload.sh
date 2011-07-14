#!/bin/bash

# directorys
downloadDir="/Users/velrok/Downloads/transmission/finished"
workingDir="/Users/velrok/Downloads/transmission/workingDir"
logDir="/Users/velrok/Downloads/transmission"
destinationDir="/Users/velrok/Movies/Serien"

logFile="$logDir/finishedDownloadScript.log"

echo "creating log file: $logFile"
date > $logFile

echo "creating working Dir: $workingDir"
mkdir $workingDir
cd $workingDir

echo "creating hard links"
pwd
ls $downloadDir | xargs -I {} ln $downloadDir/{} 2>> /dev/null

echo "renaming files"
tvnamer $workingDir

echo "moving episodes"
moveEpisodes.py $workingDir $destinationDir

echo "cleaning working dir"
rm -rf $workingDir

echo "all DONE"