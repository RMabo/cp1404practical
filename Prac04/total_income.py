"""
CP1404/CP5632 Practical`
Starter code for cumulative total income program
"""


incomes = []
months = int(input("How many month ? "))
for i in range (1,months +1):
    incomes.append(float(input(F"income {i}")))
print(incomes)
print("Income Report")
print("-------------")
total = 0
for i in range(1,len(incomes)+1):
    total += incomes[i-1]
    print(f"Month  {i} - Income: ${incomes[i-1]} Total ${total:10.2f}")