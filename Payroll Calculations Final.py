#Author:    Christopher Todd
#Date:      June 24, 2020
#Purpose:   Create a pay slip to be included in a cheque envelope for a small business
#           User will be prompted for employee name, number of hours worked, their rate of pay, and their tax exemption status
#           User is not allowed to enter non-alphanumeric characters for employee name
#           User is not allowed to enter negative values for hours worked or rate of pay
#           User is not allowed to enter negative values or values greater than 100 for deduction percent

#fuction to prompt user for hours worked, hourly rate, and percent tax deducted, with restraints on min/max values:

def getFloatValue(prompt, minimum, maximum) : 
    goodValue = False #assign false to goodValue to enter while loop
    while not goodValue : 
        try :
            lineOfInput = input(prompt) #prompt for a value and assign to lineOfInput
            value = float(lineOfInput)  #assign numerical type float to value
            if (value < minimum) or (value > maximum) :      #check to see if bad data entered
                print("Value is out of range. Please enter a valid value. You entered", value)
            else :
                goodValue = True  #good value entered, gets us out of the while loop
        except ValueError:
            print("non numeric characters entered. must enter only numeric characters. You entered", lineOfInput) 
    return value #return a value within the acceptable range

#prompt user for employee name and validate that it's alphanumeric:

goodValue = False
while not goodValue : #validate that the name is alphanumeric
    employeeName = input("Please enter the name of the Employee: ")
    if employeeName.replace(" ", "").isalpha() == False:
        print("Please enter a valid alphanumeric name.")
    else:
        goodValue = True 

#prompt user for hours worked and rate of pay using functions to restrict the values entered:
    
hoursWorked = getFloatValue("Please enter the number of hours worked by the Employee: ", 0, 100000) #prompts user for hours worked and calls function. Min = 0, max = large value
hourlyRate = getFloatValue("Please enter the rate of pay for the Employee ($/hr): ", 0, 100000)     #prompts user for hourly rate and calls function. Min = 0, max = large value

#prompt user for tax exemption status and prevent invalid entries:

goodValue = False #assign false to goodValue to enter loop
while not goodValue :
    taxExempt = input("Is the Employee tax exempt? [Y/N]: ") #assign either yes or no to taxExempt variable
    if taxExempt != "N" and taxExempt != "n" and taxExempt != "Y" and taxExempt != "y" : #accounts for small and large Y/N
        print("You must answer either Y or N. You entered ", taxExempt)
    else : 
        goodValue = True
        if taxExempt == "N" or taxExempt == "n" :
            deductPercent = getFloatValue("Enter deduction percentage: ", 0, 100) #if user enters no, deduction percentage is prompted using function. Min = 0, max = 100%
        else :
            deductPercent = 0 #no deduction if user answers yes

#calculate output variables:
        
grossPay = hoursWorked * hourlyRate #calculates gross pay
deductions = grossPay * deductPercent / 100 #calculates employee deductions, if applicable
netPay = grossPay - deductions #calculates net pay

#output results:

print('{:<20}  {:>10}'.format("Empolyee Name:", employeeName), "\n",
      '{:<20} ${:>10,.2f}'.format("Hourly Rate:", hourlyRate), "\n",
      '{:<20}  {:>10,.2f}'.format("Hours Worked:", hoursWorked), "\n",
      "                    ------------", "\n",
      '{:<20} ${:>10,.2f}'.format("Gross Pay:", grossPay), "\n",
      '{:<20}-${:>10,.2f}'.format("Deductions:", deductions), "\n"
      "                    ------------", "\n",
      '{:<20} ${:>10,.2f}'.format("Net Pay:", netPay), sep='')  

