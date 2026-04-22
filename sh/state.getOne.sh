#!/bin/bash

#Change working folder
cd "$(dirname "$0")"

#Run the command
#curl -s -X POST -H "Content-Type: application/json" -d "@json/state.json" http://localhost:3000/states/id/2
curl http://localhost:3000/states/id/$1
