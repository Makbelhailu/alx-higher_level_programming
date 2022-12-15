#!/bin/bash
#make arequest and count line
curl -s "$1" | wc -c
