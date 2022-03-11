#!/bin/bash

pycheck(){
if pip list | grep "$1" 1> /dev/null ; then
    echo "'$ pip $1' found, skipping installing..."
else
    echo "'$ pip $1' not found, installing $1..."
    pip install $1
fi
}

if command -v "pip" 1> /dev/null ; then
    echo "'$ pip' found, skipping installing..."
else
    echo "'$ pip' not found, installing pip..."
    sudo apt install pip
fi

pycheck "pygame"
pycheck "sys"
pycheck "random2"
sudo apt-get install python3-tk
sudo apt-get install python-tk
