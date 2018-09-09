#!/bin/sh


echo '#####################'
echo 'INSTALL NEEDED LIBRARY'
echo '#####################'


# check if is python 3 
echo '1) Check python version ... '
echo ''
python_version=$(python -V 2>&1 | cut -d':' -f 1  | cut -d'.' -f 1)

echo 'Python version: ' $python_version
if [ "$python_version" = "Python 3" ] ; then 
	echo "you are using python3"
else
	echo "please download/run this APP in python3"
	exit 1 
fi 

echo ''
# install library 
echo '2) Install library ... '
echo ''
pip install flask spotipy pandas 







