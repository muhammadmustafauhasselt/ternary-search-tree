#!/bin/bash
#SBATCH --job-name=tst_benchmark
#SBATCH --output=output/benchmark_output_%j.txt
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=2
#SBATCH --mem=4G
#SBATCH --time=00:30:00
#SBATCH --partition=batch

# Load Python module
module purge
module load Python/3.11.3-GCCcore-12.3.0

# Move to your script directory
cd $VSC_DATA/tst_project/benchmark

# Run Python script
python3 benchmark.py
