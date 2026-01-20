# Topsis for Multi Criteria Decision Making
## Introduction

This repository contains a Python implementation of the **Technique for Order Preference by Similarity to Ideal Solution (TOPSIS)**.  
TOPSIS is a powerful **multi-criteria decision-making (MCDM)** method that assists in ranking a set of alternatives based on their relative closeness to the ideal solution.

The method is widely used in decision analysis problems where multiple, often conflicting, criteria must be evaluated simultaneously. TOPSIS identifies solutions that have the **shortest distance from the ideal solution** and the **farthest distance from the negative-ideal solution**, thereby providing a clear and logical ranking of alternatives.

This repository demonstrates TOPSIS through python command-line implementation, python package, and a web-based service.

---

## Table of Contents

- [Python Command-Line Implementation](#1-python-command-line-implementation)
- [Python Package (PyPI)](#2-python-package-pypi)
- [TOPSIS Web Service](#3-topsis-web-service)

---

## 1. Python Command-Line Implementation

This part provides a **Python program** to execute the TOPSIS algorithm using the command line.

### Features
- Accepts input data from a CSV file
- Validates weights, impacts, and data format
- Computes TOPSIS scores and ranks alternatives
- Outputs results to a CSV file

### Input
- **CSV file**  
- **Weights**: Comma-separated numeric values  
- **Impacts**: Comma-separated values (`+` for benefit, `-` for cost)

### Usage example
```bash
python topsis.py input.csv "1,1,1,1,1" "-,+,-,-,-" output.csv
```
Command line implementation
<img width="1626" height="93" alt="Screenshot 2026-01-19 232853" src="https://github.com/user-attachments/assets/8cb45582-e2d7-4e20-88c4-914b7ce0e175" />

Input File
<img width="636" height="327" alt="image" src="https://github.com/user-attachments/assets/53dd7c91-a3f6-45f8-bcba-dfc67dee4849" />

### Output
Output file
<img width="847" height="299" alt="image" src="https://github.com/user-attachments/assets/4f2a473d-aaf3-4c3e-8c9b-fc829dc5d0c1" />



