#!/bin/sh
#$ -cwd
#$ -l cpu_4=1
#$ -l h_rt=00:10:00

./mm 2000 2000 2000

# naive cpu
#  ./mm 2000 2000 2000
# Matmul took 2246009 us --> 7.124 GFlops
# Matmul took 2237316 us --> 7.151 GFlops
# Matmul took 2244341 us --> 7.129 GFlops
# Matmul took 2252441 us --> 7.103 GFlops
# Matmul took 2239994 us --> 7.143 GFlops

