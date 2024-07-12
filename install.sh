#!/bin/bash

# Verify if Python 3 is installed
if ! command -v python3 &> /dev/null
then
	echo "Installing Python 3..."
	sudo apt-get update
	sudo apt-get install python3
else
	echo "Python 3 is already installed."
fi

# Verify if pip for Python 3 is installed
if ! command -v pip3 &> /dev/null
then
	echo "pip for Python 3 is not installed. Installing..."
	sudo apt-get install python3-pip
else
	echo "pip for Python 3 is already installed."
fi

# Change the script permissions
chmod +x pyt

# Create a symbolic link to the script
echo "Creating a symbolic link to the script..."
if [ -L /usr/local/bin/pyt ]
then
    echo "The script is already linked."
else
    sudo ln -s $(pwd)/pyt /usr/local/bin/pyt
    echo "The script was successfully linked."
fi