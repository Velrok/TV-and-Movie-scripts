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
mkdir $workingDir 2>> $logFile
cd $workingDir

echo "creating hard links"
ls $downloadDir | xargs -I {} ln $downloadDir/{} 2>> $logFile

echo "renaming files"
tvnamer $workingDir 2>> $logFile

echo "moving episodes"
moveEpisodes.py $workingDir $destinationDir 2>> $logFile

echo "all DONE"