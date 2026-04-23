#!/bin/bash

#Change working folder
cd "$(dirname "$0")"

#Add: (local:remote)
curl -s -X DELETE -H "Content-Type: application/json" -d "@json/state.delete.json" http://localhost:3000/states/delete/1
curl http://localhost:3000/states/