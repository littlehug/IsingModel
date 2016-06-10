#!/usr/bin/env bash

# Update the apt-get first
echo "Begin to do \"apt-get update\" to make sure you can install scipy..."
read -p "Want to update? [Y/n] " -n1 key
echo ""
if [ "${key}" == "n" ] || [ "${key}" == "N" ]; then
	echo "Nothing to update"
elif [ "${key}" == "y" ] || [ "${key}" == "Y" ]; then
	echo "sudo apt-get update"
	sudo apt-get update
else
	echo "Your input is wrong"
	exit 0
fi

# Basic python model
echo ""
if [$? == 1]; then
	exit 0
fi

echo "sudo apt-get install python-pip python-numpy python-scipy python-matplotlib"
sudo apt-get install python-pip python-numpy python-scipy python-matplotlib

# Upgrade numpy version
echo ""
if [ $? == 1 ]; then
	exit 0
fi

echo "pip --version"
pip --version
read -p "Please see above, is your pip version 2.7? [Y/n] " -n1 key
echo ""

[ "${key}" == "y" -o "${key}" == "Y" ] && echo "sudo pip install numpy --upgrade" && sudo pip install numpy --upgrade && echo "Finish!"
[ "${key}" == "n" -o "${key}" == "N" ] && echo "sudo pip2 install numpy --upgrade" && sudo pip2 install numpy --upgrade && echo "Finish!"

