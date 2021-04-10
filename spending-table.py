#Current date and time
from datetime import datetime
todaysdate = datetime.now()

infile = open("spending-table.txt").read()

#Initial balance and ammount of savings
balance = float(input("\nEnter current balance: $"))
savings = float(input("How much of it is savings?: $"))
spendable = balance - savings

#Savings and spendable based on income
income = float(input("Enter income: $"))
i_save = income * int(input("How many percent of your income are you saving?: %"))/100
i_spend = income - i_save

#Total ammount of money you have combined
t_balance = balance + income
t_save = savings + i_save
t_spend = spendable + i_spend

output = todaysdate.strftime("%d/%m/%Y (%B)") + \
      "\nCurrent Balance : $" + str(format(balance,".2f")) + \
      "\nSavings         : $" + str(format(savings,".2f")) + \
      "\nSpendable       : $" + str(format(spendable,".2f")) + \
      "\nIncome          : $" + str(format(income,".2f")) + \
      " ($" + str(format(i_save,".2f")) + " + $" + str(format(i_spend,".2f")) + ")" + \
      "\nTotal Balance   : $" + str(format(t_balance,".2f")) + \
      "\nTotal Savings   : $" + str(format(t_save,".2f")) + \
      "\nTotal Spendable : $" + str(format(t_spend,".2f") + "\n\n")

#Output
print("\n==================================================\n")
print(output)

#Write a file
outfile = open("spending-table.txt", "w")
outfile.write(str(output)+ str(infile))
outfile.close()

print(">>>Data writen to spending-table.txt")

pause = input("\n//press enter to exit//\n")
