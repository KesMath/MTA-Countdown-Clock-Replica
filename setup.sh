#!/bin/bash
echo "altering pythonpath..."
export PYTHONPATH=$PYTHONPATH:$(pwd):$(pwd)/venv/lib/python3.7/site-packages/
echo "pythonpath altered"


#TODO: get this shell script to run

# given that this project was written using python 3.7.1,
# research to assure that any higher version is backwards compatible
# and able to run this version!

# also place version case on mta_api_parser.py 
# i.e. if python --version >=3.7.1 then continue to run
