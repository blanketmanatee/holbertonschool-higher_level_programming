#!/bin/bash
# sends a DELETE request to url passed as first arg and displays body response
curl -sX DELETE "$1"
