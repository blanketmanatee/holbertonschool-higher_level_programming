#!/bin/bash
# takes in URL sends a request to url displays size of body as response
curl -s "$1" | wc -c
