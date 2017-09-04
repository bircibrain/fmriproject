#!/bin/bash
#the number of iterations
N=10
echo "" > results.txt
echo "iter stimEff contrastEff seed" > results.txt

#portable method of getting a random number
for i in $(seq 1 $N); do
seed=`cat /dev/random|head -c 256|cksum |awk '{print $1}'`

#generate many random sequences with 6 conditions, 500 s long runs, TR=2s:
#1 - action leg words, 2 - action hand words, 3 - action face words, 4 - hash marks (baseline), 5 - fillers, 6 - null events
RSFgen \
-nt 500 -num_stimts 6 \
-nreps 1 40		\
-nreps 2 40 	\
-nreps 3 40		\
-nreps 4 120	\
-nreps 5 120 	\
-nreps 6 40 	\
-seed ${seed} 	\
-prefix rsf_${i}_


#convert binary files to timing in seconds, this will be a local timing file, where each run starts at t=0
make_stim_times.py -files rsf_${i}_*.1D -prefix stim.${i} -nt 500 -tr 2 -nruns 1

#evaluate the efficiency of the design
3dDeconvolve \
-nodata 500 2 \
-polort 3 \
 -num_stimts 6 \
 -stim_times 1 stim.${i}.01.1D 'GAM' \
 -stim_label 1 'LW' \
 -stim_times 2 stim.${i}.02.1D 'GAM' \
 -stim_label 2 'HW' \
 -stim_times 3 stim.${i}.03.1D 'GAM' \
 -stim_label 3 'FW' \
 -stim_times 4 stim.${i}.04.1D 'GAM' \
 -stim_label 4 'HASH' \
 -stim_times 5 stim.${i}.05.1D 'GAM' \
 -stim_label 5 'FIL' \
 -stim_times 6 stim.${i}.06.1D 'GAM' \
 -stim_label 6 'NULL' \
 -gltsym "SYM: 0.33*LW 0.33*HW 0.33*FW -1.0*HASH" > efficiency.${i}.txt

eff=`./efficiency_parser.py efficiency.${i}.txt`

echo "$i $eff $seed" >> results.txt
#end loop
done

