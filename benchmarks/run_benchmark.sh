#!/bin/bash
#SBATCH --job-name=tst-bench
#SBATCH --time=01:00:00
#SBATCH --output=benchmark_results.txt
#SBATCH --cpus-per-task=4
#SBATCH --account=lp_h_ds_students
#SBATCH --cluster=genius

# Move to your project root
cd $HOME/ternary-search-tree

# Make sure Python sees your src/ package
export PYTHONPATH="$PWD"

# Run the benchmark with the system Python3 interpreter
/usr/bin/python3 "$PWD/benchmarks/benchmark.py"