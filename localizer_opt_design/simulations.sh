#!/bin/bash

chmod +x ./optimize.sh
chmod +x ./efficiency_parser.py

# $1 number of iteration
# $2 number of volumes
# $3 TR
# $4 number of blocks for each type
# $5 the length of block for each type (in second)
./optimize.sh 10 252 2 1  84
./optimize.sh 10 252 2 2  42
./optimize.sh 10 252 2 3  28
./optimize.sh 10 252 2 4  21
./optimize.sh 10 252 2 6  14
./optimize.sh 10 252 2 7  12
./optimize.sh 10 252 2 8  10.5
./optimize.sh 10 252 2 12 7