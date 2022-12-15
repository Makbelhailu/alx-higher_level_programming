#!/bin/bash
#makes a request to 0.0.0.0:5000/catch_me that causes some message
curl -sL -X PUT -H "Origin: HolbertonSchool" 0.0.0.0:5000/catch_me
