#!/bin/bash

chmod +x ./optimize.sh
chmod +x ./efficiency_parser.py

# $1 number of iteration
# $2 number of time points (in seconds)
# $3 TR
# $4 number of blocks for each type
# $5 the length of block for each type (in seconds)
./optimize.sh 10 504 2  2 42
./optimize.sh 10 504 2  3 28
./optimize.sh 10 504 2  4 21
