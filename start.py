import tkinter as tk
from tkinter import ttk

def milesToFt(miles):
    
    feet = miles * 5280
    return feet

def milesToInches(miles):
    
    inches = miles * 63360
    return inches

def milesToKM(miles):
    
    km = miles * 1.60934
    return km

def milesToMeters(miles):
    
    meters = miles * 1609.34
    return meters



milesMain = ''
result = 0
option = ""
mainF = tk.Tk()
from tkinter import *
result_var = tk.StringVar()
option2  = tk.StringVar()
def initiateConversion():
    entered_miles = filesEntry.get()
    option = optionBox.get()
    print(entered_miles)
    print(option)
    option2.set(option)
    

    if option == "Feet":
        result = milesToFt(int(entered_miles))
        result_var.set(f'{result} {option}')
        print(result)
    elif option == "Inches":
        result = milesToInches(int(entered_miles))
        result_var.set(f'{result} {option}')
        print(result)
    elif option == "Kilometers":
        result = milesToKM(int(entered_miles))
        result_var.set(f'{result} {option}')
        print(result)
    elif option == "Meters":
        result = milesToMeters(int(entered_miles))
        result_var.set(f'{result} {option}')
        print(result)
    
    
    
    

        

mainF.title('Miles to X Converter')
Label(mainF, text='Enter Miles:').pack(pady=10)
filesEntry = Entry(mainF, textvariable=milesMain)

filesEntry.pack(pady=5)

selectLabel  = ttk.Label(mainF, text='Select Conversion:')
selectLabel.pack(pady=10)


optionBox = ttk.Combobox(mainF, values=["Feet", "Inches", "Kilometers", "Meters"], state='readonly')
optionBox.pack(pady=5)
optionBox.set("Select Conversion")

convertButton = ttk.Button(mainF, text='Convert', width=15, command=initiateConversion)
convertButton.pack(pady=20)

resultLabel = ttk.Label(mainF, textvariable=result_var)
resultLabel.pack(pady=10)

mainF.mainloop()