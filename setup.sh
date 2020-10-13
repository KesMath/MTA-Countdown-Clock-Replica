#!/bin/bash
export PYTHONPATH=$PYTHONPATH:$(pwd)
echo "pythonpath altered"  $PYTHONPATH


# SETUP CMD :
# sudo apt-get install build-essential libssl-dev libffi-dev python3-dev (for dependency header files needed for cryptography lib)
# REFERENCE: https://cryptography.io/en/latest/installation/
# cd MTA-Countdown-Clock-Replica
# pip3 install -r requirements.txt


# source ./setup.sh
# fetch API_KEY from mta site and generate private key file - {can encapsulate into this setup.sh file and before running app,
# consider py_api_connect.py file to test validation before adding encrpyted string to config/mta_config.ini and creating keyfile}

#RUN CMD:
# cd mta 
# python3 mta_api_parser.py
