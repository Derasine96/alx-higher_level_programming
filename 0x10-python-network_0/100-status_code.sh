#!/bin/bash
#Send a request to the URL and display the status code of the response
curl -s -o /dev/null -w "%{http_code}" "$1"
