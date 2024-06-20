p = float(input("enter the princple amount: "))
r = float(input("enter Rate of Interst: "))
n = int(input("Enter number of months: "))

r = r/(12*100)

emi = p * r * ((1+r)**n)/((1+r)**n - 1)
print("Monthly EMI is: ", round(emi,2))

