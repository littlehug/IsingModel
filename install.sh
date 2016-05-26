#!/usr/bin/env bash

# Update the apt-get first
echo "Begin to do \"apt-get update\" to make sure you can install scipy..."
read -p "Want to update? [Y/n]" -n1 key

if [ "${key}" == "n"] || [ "${key}" == "N" ]; then
	
elif ["${key}" == "y"] || [ "${key}" == "Y"]; then
	echo "sudo apt-get update"
	sudo apt-get update
else
	echo "Your input is wrong"
	exit 0
fi

# Basic python model
echo "sudo apt-get install python-pip python-numpy python-scipy"
sudo apt-get install python-pip python-numpy python-scipy

# Upgrade numpy version
if [ $? == 1 ]; then
	exit
fi
echo "pip --version"
read -p "is your pip version 2.7? [Y/n]" key
[ "${key}" == "y" -o "${key}" == "Y" ] && echo "sudo pip install numpy --upgrade" && sudo pip install numpy --upgrade && echo "Finish!"
[ "${key}" == "n" -o "${key}" == "N" ] && echo "please install pip as 2.7 version" && exit 0

