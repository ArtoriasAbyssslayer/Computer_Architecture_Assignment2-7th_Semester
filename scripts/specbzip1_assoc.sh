#!/bin/bash

./build/ARM/gem5.opt -d spec_results/tests/specbzip_tests/256cachelinesize_othermods/Associativity_tests/A1 configs/example/se.py  --cpu-type=MinorCPU --caches --l2cache  --l1d_size=128kB --l1i_size=128kB --l2_size=4MB --l1i_assoc=1 --l1d_assoc=1 --l2_assoc=8 --cacheline_size=256 --cpu-clock=1GHz -c spec_cpu2006/401.bzip2/src/specbzip -o "spec_cpu2006/401.bzip2/data/input.program 10" -I 100000000

./build/ARM/gem5.opt -d spec_results/tests/specbzip_tests/256cachelinesize_othermods/Associativity_tests/B1 configs/example/se.py  --cpu-type=MinorCPU --caches --l2cache  --l1d_size=128kB --l1i_size=128kB --l2_size=4MB --l1i_assoc=4 --l1d_assoc=4 --l2_assoc=8 --cacheline_size=256 --cpu-clock=1GHz -c spec_cpu2006/401.bzip2/src/specbzip -o "spec_cpu2006/401.bzip2/data/input.program 10" -I 100000000

./build/ARM/gem5.opt -d spec_results/tests/specbzip_tests/256cachelinesize_othermods/Associativity_tests/C1 configs/example/se.py  --cpu-type=MinorCPU --caches --l2cache  --l1d_size=128kB --l1i_size=128kB --l2_size=4MB --l1i_assoc=8 --l1d_assoc=8 --l2_assoc=8 --cacheline_size=256 --cpu-clock=1GHz -c spec_cpu2006/401.bzip2/src/specbzip -o "spec_cpu2006/401.bzip2/data/input.program 10" -I 100000000

./build/ARM/gem5.opt -d spec_results/tests/specbzip_tests/256cachelinesize_othermods/Associativity_tests/D1 configs/example/se.py  --cpu-type=MinorCPU --caches --l2cache  --l1d_size=128kB --l1i_size=128kB --l2_size=4MB --l1i_assoc=8 --l1d_assoc=8 --l2_assoc=16 --cacheline_size=256 --cpu-clock=1GHz -c spec_cpu2006/401.bzip2/src/specbzip -o "spec_cpu2006/401.bzip2/data/input.program 10" -I 100000000
