#!/bin/bash
export PYTHONPATH=$PYTHONPATH:$(pwd)
echo "pythonpath altered"
echo $PYTHONPATH

#TODO: add pip install -r requirements.txt iff pip is installed on machine




#Compatible: Python version x.y is compatible with w.z if x == w and y >= z
#Potentially compatible: Python version x.y is potentially compatible to version w.z if x == w and y < z



#SETUP CMDS:
#cd MTA-Countdown-Clock-Replica
# source ./setup.sh
# fetch API_KEY and generate private key file 
# python3 mta/mta_api_parser.py
