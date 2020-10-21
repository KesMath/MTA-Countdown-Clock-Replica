#!/bin/bash

#TODO: export permanently
export PYTHONPATH=$PYTHONPATH:$(pwd)
echo "pythonpath altered"  $PYTHONPATH


# INSTALL DEPENDENCIES:
echo "installing header files needed for cryptography lib ..."
sudo apt-get install build-essential libssl-dev libffi-dev python3-dev # REFERENCE: https://cryptography.io/en/latest/installation/
echo "header files installed!"


cd MTA-Countdown-Clock-Replica
echo "installing python libaries..."
pip3 install -r requirements.txt
echo "python libs installed!"


# CREATE PRIVATE KEY FILE:
# source ./setup.sh
# fetch API_KEY from mta site and generate private key file - {can encapsulate into this setup.sh file and before running app,
# consider py_api_connect.py file to test validation before adding encrypted string to config/mta_config.ini and creating keyfile}

#RUN CMD:
# cd mta 
# python3 mta_api_parser.py
