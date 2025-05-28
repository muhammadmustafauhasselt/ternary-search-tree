#!/bin/bash
#SBATCH --job-name=tst-bench
#SBATCH --time=01:00:00
#SBATCH --output=benchmark_results.txt
#SBATCH --cpus-per-task=4
#SBATCH --account=lp_h_ds_students
#SBATCH --cluster=genius

cd $HOME/ternary-search-tree
export PYTHONPATH="$PWD"

# Run the benchmark with both TST and B-Tree
/usr/bin/python3 "$PWD/benchmarks/benchmark.py"
