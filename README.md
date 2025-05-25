# Ternary Search Tree Implementation – Data Science Project 2024–2025

## Overview

This project is a Python-based implementation of a **Ternary Search Tree (TST)**, developed as part of the *Concepts of Data Science* course (2024–2025). The project focuses on the design, implementation, correctness testing, and performance benchmarking of the TST using High-Performance Computing (HPC) infrastructure.

## Features

- Object-oriented implementation of the TST in Python
- Modular design for use in Jupyter notebooks and standalone Python scripts
- Extensive correctness testing
- Benchmarking of insert and search operations using large datasets
- HPC job script for performance analysis at scale
- Comparison with alternative data structures such as B-Trees (optional)

## Files and Structure

- `ternary_search_tree.py`: Python module implementing the ternary search tree
- `test_tst.py`: Test suite for validating correctness
- `benchmark.py`: Script used for insert/search timing
- `run_benchmark.sh`: Slurm batch script used to run benchmarks on the HPC cluster
- `benchmark_results.txt`: Includes time measurements for insert and search operations
- `README.md`: Project documentation and summary (this file)

## Benchmark Results

**Dataset Size:** 100,000 words  
**Cluster Platform:** HPC infrastructure  
**Performance:**
- **Insert Time:** 1.2067 seconds
- **Search Time:** 0.6371 seconds

These results were measured using a large input file containing English words. The operations scale reasonably well and show consistent performance in practical workloads.

## Time and Space Complexity

| Operation | Best Case | Average Case | Worst Case |
|-----------|-----------|--------------|------------|
| Insert    | O(log n)  | O(log n)     | O(n)       |
| Search    | O(log n)  | O(log n)     | O(n)       |

- **Space Complexity:** O(n) where *n* is the total number of nodes (each character node uses space).

## Usage

### Run Tests

```bash
python test_tst.py
```

### Benchmark on Local System

```bash
python benchmark.py
```

### Benchmark on HPC

Submit the job via:

```bash
sbatch hpc_job.sh
```

## Git & Collaboration Notes

This project was developed collaboratively using GitHub. All commits are traceable, and contribution by each team member is reflected in the repository history. Collaboration included shared debugging, development of benchmark logic, and test case design.

## Conclusion

The Ternary Search Tree implementation demonstrates both correctness and efficiency at scale. The data structure is particularly suitable for prefix-based string search operations and shows competitive performance in HPC settings.

## License

This project is for academic use only. All rights reserved by the authors.
