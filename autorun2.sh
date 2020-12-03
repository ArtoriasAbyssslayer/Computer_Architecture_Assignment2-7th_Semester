#!/bin/bash
ls -la
#runs a benchmark on gem5      
printf 'Starting benchmark specbzip \n'
./build/ARM/gem5.opt -d spec_results/specbzip1 configs/example/se.py --cpu-type=MinorCPU --cpu-clock=1Ghz --caches --l2cache -c spec_cpu2006/401.bzip2/src/specbzip -o "spec_cpu2006/401.bzip2/data/input.program 10" -I 100000000
#second benchmark on gem5 arm
echo "Starting benchmark specmcf"
./build/ARM/gem5.opt -d spec_results/specmcf1 configs/example/se.py --cpu-type=MinorCPU --cpu-clock=1Ghz --caches --l2cache -c spec_cpu2006/429.mcf/src/specmcf -o "spec_cpu2006/429.mcf/data/inp.in" -I 100000000 
#3rd simulation 456.hmmer
echo "Starting benchmark spechmmer"
./build/ARM/gem5.opt -d spec_results/spechmmer1 configs/example/se.py --cpu-type=MinorCPU --cpu-clock=1Ghz --caches --l2cache -c spec_cpu2006/456.hmmer/src/spechmmer -o "--fixed 0 --mean 325 --num 45000 --sd 200 --seed 0 spec_cpu2006/456.hmmer/data/bombesin.hmm" -I 100000000
#4th sjeng 
echo "Starting benchmark specsjeng"
./build/ARM/gem5.opt -d spec_results/specsjeng1 configs/example/se.py --cpu-type=MinorCPU --cpu-clock=1Ghz --caches --l2cache -c spec_cpu2006/458.sjeng/src/specsjeng -o "spec_cpu2006/458.sjeng/data/test.txt" -I 100000000
#5th benchmark lbm
echo "Starting benchmark speclibm"
./build/ARM/gem5.opt -d spec_results/speclibm1 configs/example/se.py --cpu-type=MinorCPU --cpu-clock=1Ghz --caches --l2cache -c spec_cpu2006/470.lbm/src/speclibm -o "20 spec_cpu2006/470.lbm/data/lbm.in 0 1 spec_cpu2006/470.lbm/data/100_100_130_cf_a.of" -I 100000000
ls -la
