print("Ideal Gas Law Calculator (PV=nRT)")
print(" ")
print("By Patrick Chellakan")
print(" ")
print("Current as of February 6th, 2023")
print(" ")

print("This is a basic calculator meant to perform calculations with the ideal gas law.")
print("The ideal gas law is a mathematical relation used to predict the properties of a hypothetical ideal gas under specified conditions.")
print("Four themodynamic properties are represented in the relation: pressure (P), volume (V), temperature (T), and the number of moles of the substance of inquiry (n).")
print("Variables must be entered in SI units: kelvins for T, cubic meters for V, moles for n, and pascals for P.")
print("The universal gas constant R will be entered automatically as 8.314 Pa*m^3/mol*K.")
print(" ")

variableSelection = str(input("What variable is being solved for? (T/V/n/P): ")) # Recieve input from user.

if variableSelection == 'T': # If user would like to solve for this variable...

    Volume = float(input('Enter volume in cubic meters: '))
    def checkInput(input):
        try:
            Volume = float(input)
        except ValueError:
            print("The input is invalid; please try again. Variables must be integers.")
            exit()  
    checkInput(Volume)
    Moles = float(input('Enter moles: '))
    checkInput(Moles)
    Pressure = float(input('Enter pressure in pascals: ')) # Collect other three properties...
    checkInput(Pressure)
    answer = (Pressure*Volume)/(Moles*8.314) # Perform calculations...
    
    print(answer) # And finally, output the answer.            
    
elif variableSelection == 'V': # Repeat the process for V...

    Temperature = float(input('Enter temperature in kelvins: '))
    def checkInput2(input):
        try:
            Temperature = float(input)
        except ValueError:
            print("The input is invalid; please try again. Variables must be integers.")
            exit()
    checkInput2(Temperature)
    Moles = float(input('Enter moles: '))
    checkInput2(Moles)
    Pressure = float(input('Enter pressure in pascals: '))
    checkInput2(Pressure)
    
    answer = (Moles*Temperature*8.314)/Pressure
    
    print(answer)
    
elif variableSelection == 'n': # For n...
    
    Temperature = float(input('Enter temperature in kelvins: '))
    def checkInput3(input):
        try:
            Temperature = float(input)
        except ValueError:
            print("The input is invalid; please try again. Variables must be integers.")
            exit()
    checkInput3(Temperature)
    Volume = float(input('Enter volume in cubic meters: '))
    checkInput3(Volume)
    Pressure = float(input('Enter pressure in pascals: '))
    checkInput3(Pressure)
    
    answer = (Pressure*Volume)/(Temperature*8.314)
    
    print(answer)
    
elif variableSelection == 'P': # And for P.
    
    Temperature4 = float(input('Enter temperature in kelvins: '))
    def checkInput4(input):
        try:
            Temperature = float(input)
        except ValueError:
            print("The input is invalid; please try again. Variables must be integers.")
            exit()
    checkInput4(Temperature)
    Volume = float(input('Enter volume in cubic meters: '))
    checkInput4(Volume)
    Moles = float(input('Enter moles: '))
    checkInput4(Moles)
    
    answer = (Moles*Temperature*8.314)/Volume
    
    print(answer)
    
else:
    outputError = str("The input was invalid; please try again. Alphabetical characters should be entered as T, V, n, or P.") 
    print(outputError)
    # If the user inputs anything but a variable, output this error with a suggested fix for the user. 