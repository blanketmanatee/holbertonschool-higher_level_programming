#!/bin/bash
# takes in URL sends a POST request and displays body
curl -s -X POST -d "emacs-hr@holbertonschool.com&subject=I will always be here for PLD" "$!"
