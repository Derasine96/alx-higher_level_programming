#!/bin/bash
#Bash script displays the size of the body of the response of a URL
curl -s "$1" | wc -c
