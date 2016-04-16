#!/bin/bash

CLARIFAI_APP_ID=ZlPXlWOOYAC68cPqR58knrfLnJHYNGw3ej5A7u1N
CLARIFAI_APP_SECRET=RNnRgitRS4PaNkomMFjzX7QhU8OM1n_6rkYSdmV0
SCRIPT_PATH="python_scripts/parse.py" 
PYTHON="/usr/bin/python"

curl -X POST "https://api.clarifai.com/v1/token/" \
    -d "client_id=$CLARIFAI_APP_ID" \
    -d "client_secret=$CLARIFAI_APP_SECRET" \
    -d "grant_type=client_credentials"


curl "https://api.clarifai.com/v1/tag/" \
    -F "encoded_data=@$1" \
    -H "Authorization: Bearer kCin7h1ljGOaoOrlYBs4MN4qqLloJ4" > json_files/foo.json

$PYTHON $SCRIPT_PATH
exit 0

