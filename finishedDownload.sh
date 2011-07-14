#!/bin/bash

# directorys
downloadDir="/Users/velrok/Downloads/transmission/finished"
workingDir="/Users/velrok/Downloads/transmission/workingDir"
logDir="/Users/velrok/Downloads/transmission"
destinationDir="/Users/velrok/Movies/Serien"

logFile="$logDir/finishedDownloadScript.log"
errorsFile="$logDir/finishedDownloadScript.errors"

growlIcon="Python"
growlTitle=$0

echo "removing erros file"
rm $errorsFile

echo "creating log file: $logFile"
date > $logFile

echo "creating working Dir: $workingDir"
mkdir $workingDir
cd $workingDir

echo "creating hard links"
pwd
ls $downloadDir | xargs -I {} ln $downloadDir/{} 2>> $errorsFile

echo "renaming files"
growlnotify -a $growlIcon -m "renaming files" $growlTitle
tvnamer $workingDir 2>> $errorsFile

echo "moving episodes"
growlnotify -a $growlIcon -m "moving episodes" $growlTitle
moveEpisodes.py $workingDir $destinationDir  2>> $errorsFile

echo "cleaning working dir"
rm -rf $workingDir

echo "all DONE"
growlnotify -a $growlIcon -m "all done" $growlTitle

if [ -e $errorsFile ]
then
	cat $errorsFile | growlnotify -a $growlIcon "$growlTitle Errors"
fi