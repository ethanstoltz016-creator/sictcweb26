#!/bin/bash

#Change working folder
cd "$(dirname "$0")"

#Run the command
curl -s -X POST -H "Content-Type: application/json" -d "@json/state.json" http://localhost:3000/states/add
curl http://10.60.4.42:3000/states/
curl http://localhost:3000/states/
#curl -s -X POST -H "Content-Type: application/json" -d "@json/state.json" http://10.60.4.42:3000/states/add