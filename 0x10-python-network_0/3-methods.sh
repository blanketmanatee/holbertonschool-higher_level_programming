#!/bin/bash
# takes in url and displays all HTTP methods server accepts
curl -sI "$1" | grep "Allow" | cut -d " " -f 2- 
