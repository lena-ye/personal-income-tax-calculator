#Income Tax Calculator
#This program calculates the tax one should pay in a fiscal year by taking into consideration their annual personal income, 
#tax credits, and any tax deductions that can be applied to the calculation. Note that this program may not reflect recent 
#changes in the Canadian income tax system and that it is for educational purposes only. The actual amount of tax one must pay 
#heavily depends on their unique situations and conditions, while this calculator is merely a simplified version of the
#complex process.
#May 17, 2024

#Checks the validity of the income entered
netIncomeValid = False

while netIncomeValid == False:
    #input must be a number with or without decimals
    try:
        netIncome = float(input("Enter your net income: $"))
        #income must be a nonnegative number
        if netIncome >= 0:
            netIncomeValid = True
        else:
            print ("Invalid income amount. Please enter a nonnegative number.")
    except TypeError:
        print ("You did not input a number. Please try again.")
    except ValueError:
        print ("Invalid input. Please try again. ")
    except NameError:
        print ("Please enter a numerical value greater than or equal to 0. ")
    
print()

#Taking tax deductions into consideration
print ("Tax deductions are the amounts of money deducted from your taxable income before applying tax credits.")

#tax deduction input must be a number
taxDeductionsValid = False
while taxDeductionsValid == False:
    #input must be a number
    try:
        taxDeductions = float(input("Enter the total amount of tax decductions possible: $"))
        #tax deduction input must be a nonnegative number
        if taxDeductions >= 0:
            taxDeductionsValid = True
        else:
            print ("Invalid tax deduction amount. Please enter a nonnegative number.")
    except TypeError:
        print ("You did not input a number. Please try again.")
    except ValueError:
        print ("Invalid input. Please try again. ")
    except NameError:
        print ("Please enter a numerical value greater than or equal to 0. ")

totalTaxableIncome = netIncome-taxDeductions
print ("Your total taxable income is ${}.".format(totalTaxableIncome))

#Calculating tax amount based on brackets
taxAmount = 0
bracket1 = 55867
rate1 = 0.145
bracket2 = 111733
rate2 = 0.205
bracket3 = 173205
rate3 = 0.26
bracket4 = 246752
rate4 = 0.29
rate5 = 0.33

if totalTaxableIncome <= bracket1:
    taxAmount += totalTaxableIncome * rate1
elif totalTaxableIncome > bracket1:
    if totalTaxableIncome <= bracket2:
        taxAmount += (totalTaxableIncome-bracket1) * rate2
    elif totalTaxableIncome > bracket2:
        if totalTaxableIncome <= bracket3:
            taxAmount 

if totalTaxableIncome > bracket4:
    taxAmount = bracket1*rate1 + (bracket2-bracket1)*rate2 + (bracket3-bracket2)*rate3 + (bracket4-bracket3)*rate4 + (totalTaxableIncome-bracket4)*rate5
elif totalTaxableIncome > bracket3:
    taxAmount = bracket1*rate1 + (bracket2-bracket1)*rate2 + (bracket3-bracket2)*rate3 + (totalTaxableIncome-bracket3)*rate4
elif totalTaxableIncome > bracket2:
    taxAmount = bracket1*rate1 + (bracket2-bracket1)*rate2 + (totalTaxableIncome-bracket2)*rate3
elif totalTaxableIncome > bracket1:
    taxAmount = bracket1*rate1 + (totalTaxableIncome-bracket1)*rate2
else:
    taxAmount = totalTaxableIncome*rate1

print("Your tax amount before tax credits are applied is ${:.2f}".format(taxAmount))

#Applying tax credits
print()

#tax credits must be a number
taxCreditsValid = False
while taxCreditsValid == False:
    #input must be a number
    try:
        taxCredits = float(input("Enter the total amount of tax credits you currently have: $"))
        #tax credits input must be a nonnegative number
        if taxCredits >= 0:
            taxCreditsValid = True
        else:
            print ("Invalid tax credit amount. Please enter a nonnegative number.")
    except TypeError:
        print ("You did not input a number. Please try again.")
    except ValueError:
        print ("Invalid input. Please try again. ")
    except NameError:
        print ("Please enter a numerical value greater than or equal to 0. ")

if taxCredits >= taxAmount:
    remainingCredits = taxCredits-taxAmount
    taxAmount = 0
    print("Your tax credits are enough to cover your income tax this year. You have ${} tax credits left.".format(remainingCredits))
else:
    taxAmount -= taxCredits
    print ("After applying tax credits, you only need to pay a tax amount of ${:.2f}.".format(taxAmount))

#Outro
print()
print ("End of program.")