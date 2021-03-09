tax_info = []

tax_info.append(eval(input("Wages, salaries, and tips earned by the husband: ")))
tax_info.append(eval(input("Wages, salaries, and tips earned by the wife: ")))
tax_info.append(eval(input("Bonus earned by the family combined: ")))

print("This is your yearly income:", sum(tax_info))
tax_info.append(sum(tax_info))

tax_info.append(eval(input("What is your standard health insurance deduction: ")))

if tax_info[4] > tax_info[3]:
    tax_info.append(0)
    print("Your taxable income is:", tax_info[5])

elif tax_info[4] < tax_info[3]:
    tax_info.append(tax_info[3] - tax_info[4])
    print("Your taxable income is:", tax_info[5])

tax_info.append(eval(input("Federal income tax withheld from paychecks for husband: ")))
tax_info.append(eval(input("Federal income tax withheld form paychecks for wife: ")))

tax_info.append(tax_info[6] + tax_info[7])
print("These are your total payments and credits:", tax_info[8])

tax_info.append(tax_info[5]*0.28)
print("Federal tax:", tax_info[9])

tax_info.append(eval(input("Property tax owed: ")))

tax_info.append(tax_info[9] +tax_info[10])
print("This is your total tax:", tax_info[11])

tax_info.append(tax_info[11] - tax_info[8])

if tax_info[8] > tax_info[11]:
    print("You have overpaid your taxes by:", tax_info[12])

elif tax_info[8] < tax_info[11]:
    print("You have to pay the following amount:", tax_info[12])
