#!/bin/bash
#Write a Bash script that takes in a URL and
curl -siLX OPTIONS "$1" | grep "Allow" | cut -d " " -f2-
