#create a python program to calculate Taxpayer's tax due
# Taxpayer's tax due is computed as follows;
# The taxpayer's dependency_exemption is determined by multiplying 3000 times the number of children.
# The taxpayer net_income is determined by taking the taxpayer's gross income and subtracting the taxpayer's dependency exemption. (print net_income).
# If the taxpayer's net income is between 0 and 50,000, the tax due is 15% of net income.
# If the taxpayer's net income is greater than 50,000, the tax due is 15% of the first 50,000 of net income.
# 25% of any income over 50,000
children = int(input("Enter the number of children: "))
gross_income = int(input("Enter your gross income: "))
dependency_exemption = 3000 * children
net_income = gross_income - dependency_exemption
#print(net_income)
if net_income<50000 and net_income>0:
    tax = 15/100 * net_income
    print("Your due tax is",tax)

elif net_income>50000:
    num = net_income - 50000
    tax1 = 15/100 * 50000
    tax2 = 25/100 * num
    tax = tax1 + tax2
    print("Your due tax is",tax)