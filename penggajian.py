# simple payroll calculator (penggajian)
# usage: python penggajian.py BASE_SALARY ALLOWANCES DEDUCTIONS

import sys

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: python penggajian.py BASE_SALARY ALLOWANCES DEDUCTIONS")
        sys.exit(1)

    try:
        base_salary = float(sys.argv[1])
        allowances = float(sys.argv[2])
        deductions = float(sys.argv[3])
    except ValueError:
        print("Please provide numeric inputs for salary, allowances, and deductions")
        sys.exit(1)

    gross_pay = base_salary + allowances
    net_pay = gross_pay - deductions

    print(f"Base Salary  : {base_salary:10.2f}")
    print(f"Allowances   : {allowances:10.2f}")
    print(f"Gross Pay    : {gross_pay:10.2f}")
    print(f"Deductions   : {deductions:10.2f}")
    print("--------------------------")
    print(f"Net Pay      : {net_pay:10.2f}")
