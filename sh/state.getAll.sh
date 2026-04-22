#!/bin/bash

#Change working folder
cd "$(dirname "$0")"

# Add: (local:remote)
curl http://localhost:3000/states/
