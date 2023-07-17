income=float(input("Enter your monthlhy income.\n"))
if income<85528:
    tax=0.18*income-556.02
elif income>85528:
    tax=14839.02+(income-85528)*0.32
tax=round(tax,0)
if tax<0:
    print("Your tax is 0.0 thalers.\n")
else:
    print("Your tax is", tax ,"thalers.\n")




