# Topsis for Multi Criteria Decision Making
## Introduction
TOPSIS (**Technique for Order Preference by Similarity to Ideal Solution**) is a widely used **multi-criteria decision-making (MCDM)** method.  
It helps in ranking multiple alternatives by comparing their distance from an **ideal best solution** and an **ideal worst solution**.
Due to its simplicity and effectiveness, TOPSIS is commonly applied in areas such as decision analysis, resource selection, performance evaluation, and ranking problems involving multiple criteria.

This repository demonstrates TOPSIS through **three different implementations**:
- A Python command-line program  
- A reusable Python package (published on PyPI)  
- A web-based TOPSIS service
  
---

## Table of Contents

- [Python Command-Line Implementation](#1-python-command-line-implementation)
- [Python Package (PyPI)](#2-python-package-pypi)
- [TOPSIS Web Service](#3-topsis-web-service)

---

## 1. Python Command-Line Implementation

This module provides a **command-line based Python implementation** of the TOPSIS algorithm.

### Features
- Accepts input data from a CSV file
- Validates weights, impacts, and data format
- Computes TOPSIS scores and ranking
- Outputs results to a CSV file

### Input
- **CSV file**  
- **Weights**: Comma-separated numeric values  
- **Impacts**: Comma-separated values (`+` or `-` )

### Usage example
1. Must have Python installed
2. Clone this repository to your local machine :
   ```bash
   git clone https://github.com/Suhani1104/Topsis
   ```
3. Navigate to the project directory
4. Run Topsis script with command line arguments : 
   Example
```bash
python topsis.py input.csv "1,1,1,1,1" "-,+,-,-,-" output.csv
```
5. Result will be saved to the specifies CSV file.
Command line implementation

<img width="1626" height="93" alt="Screenshot 2026-01-19 232853" src="https://github.com/user-attachments/assets/8cb45582-e2d7-4e20-88c4-914b7ce0e175" />

Input File

<img width="636" height="327" alt="image" src="https://github.com/user-attachments/assets/53dd7c91-a3f6-45f8-bcba-dfc67dee4849" />

### Output
Output file

<img width="847" height="299" alt="image" src="https://github.com/user-attachments/assets/4f2a473d-aaf3-4c3e-8c9b-fc829dc5d0c1" />


## 2. Python Package (PyPI)
A reusable Python Package implementation of TOPSIS, designed for easy integration into other projects.
- Published on PyPi :
  https://pypi.org/project/Topsis-Suhani-102313038/1.0.1/

### Package Name
```bash
Topsis-Suhani-102313038
```

### Installation
```bash
pip install Topsis-Suhani-102313038
```

### Usage 
```bash
python -m topsis_suhani_102313038.topsis input.csv "1,1,1,1" "+,-,+,+" output.csv
```

### Output
The output CSV file contains:
- Topsis Score for each alternative
- Rank of alternatives based on their closeness to the ideal solution
  
### License
This package is released under the MIT [LICENCE](LICENSE)



## 3. TOPSIS Web Service
A web-based implementation of TOPSIS is provided using Flask, allowing users to perform TOPSIS analysis through an interactive interface.

### Features
- Upload CSV file through the browser
- Enter weights, impacts, and email id via form input
- Validates Email format, Matching number of weights and impacts, Correct impact symbols (+ or -)
- Displays results directly on the web page
- Generates downloadable result CSV file sent via mail

### User Inputs
- CSV file
- Weights (comma-separated)
- Impacts (comma-separated + or -)
- Email ID
  
<img width="550" height="413" alt="image" src="https://github.com/user-attachments/assets/5dc1e4d1-0ffc-443e-b62e-03b5d2872813" />

### Outputs
Result table displayed on the web page 

<img width="550" height="733" alt="image" src="https://github.com/user-attachments/assets/3ff22343-add3-49da-96cd-d6abc3e9f5f6" />


Downloadable result CSV file sent via mail

<img width="550" height="458" alt="Screenshot 2026-01-20 190224" src="https://github.com/user-attachments/assets/61ef56ce-65d9-4de6-8664-2696206018ce" />

