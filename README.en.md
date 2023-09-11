# Loan Calculator
[![es](https://img.shields.io/badge/Español-red.svg)](README.md)

![](https://github.com/eitancj/preview_images/blob/main/loancalc_cli_2_en.png?raw=true)

\
An interactive tool for calculating personal loans.

### Input
- Loan amount
- Annual interest rate
- Monthly payment amount

### Output
- The time it would take to pay the loan back
- Total accumulated interest-fees
- Total amount paid
- Monthly-payment table [optional] 

### Features
- Main:  
Calculate the duration, interest fees and total expenses of a personal loan,
given some user data. 

- Languages: Spanish, English
- Currency: Euro, Dollar, Pound, Bitcoin
- Display a Monthly-Payment Table
- Formatted and Coloured Output
- Start New Loan-Calculation continually and indefinitely
- Remember User's Preferences when starting a new loan-calculation

### Tech Stack
- Python 3.11.4
- - pandas 2.1.0
- macOS X

### Prerequisites
- Python >= 3.11.0

### Run Program
> [optional] Create a new *venv* in case you prefer to install the required packages in an isolated environment.
```sh
python3 -m venv loan_calc
source 'loan_calc/bin/activate'
```
> Install packages
```sh
python3 -m pip install -r requirements.txt
``` 
>  Run Loan Calculator
>> *The Pandas package might take a moment to load the first time you run it*
```sh
python3 loan_calculator.py
```

### Clean up
> Revert the PATH executables to their original values (*if you created a new venv*)
```sh
deactivate
```

> **Carefully** delete the cloned repo from your local machine

> If you wish to uninstall the dependency packages in a comprehensive way, I recommend using the specialised package *pip-autoremove*

### Open Issues
1. Add: Option to choose between several payment periods (not just 'monthly')

### Notes
1. The type of loan this tool **intends** to calculate is the fixed-interest TIN, used in Spain.
2. The duration of the loan isn't solicited,\
    instead an estimation of it is returned, based on the data supplied by the user.
3. Commissions, Personal Credits,\
and other additional fees and products are not taken into account.
4. This tool is a personal project to help practice the use of Python3 and Pandas.\
    I'm oblivious as to whether the calculations used here are actually accurate, as I am not a professional accountant nor have I undergone any fiscal training.