import pyinputplus as pyip
def rate(quantity):
    if 0 < quantity <= 200:
        if 1 <= quantity <= 5:
            rate = 36.0
        elif 6 <= quantity <=15:
            rate = 34.5
        elif 15 <= quantity <=200:
            rate = 32.7
    else:
        return 0
    return rate

def check_reseller(option):
    if "Y" in option or "y" in option:
        discount = 0.2
    else:
        discount = 0
    return discount

data = {}
lst = []
while True:
    name = input("Enter the customer's name: ")
    quantity = pyip.inputInt(prompt="Enter the number of coffee beans bags(bag/1kg): ", min=1,max = 200)
    option = input("Enter yes or no to indicate the reseller: ")
    price = rate(quantity) * quantity
    discount = check_reseller(option) * price
    total = price - discount
    print("Total sales: "+ str(round(total,2)))
    print("----------------------------------------------------------------------")
    print()
    data[name] = name,quantity,option,total
    next = input("Do you want to add more(y/n) : ")
    print()
    print("*********************************************************************")
            
    if "n" in next:
        break
name_list = []
total_list = []
print("-------------------------------------------------------------------------")
print("*********************************************************************")
print("*********************************************************************")
print("\t\tSales Summary")
print("*********************************************************************")
print( "Name\t\tNo of bags\tReseller\t\tTotal")
#c = "center aligned"
#print(f"{c.center(30)}")
for name,quantity,option,total in data.values():
    print(f'{name.ljust(15)}\t{quantity}\t\t {option.ljust(8)}\t\t {round(total,2)}')
    name_list.append(name)
    total_list.append(total)
print("*********************************************************************")
print("*********************************************************************")
print("-------------------------------------------------------------------------")
print("*********************************************************************")


dtotal = dict(zip(name_list,total_list))

MaxValue = round(max(dtotal.values()),2)
MaxName = max(dtotal, key=dtotal.get) 
    
MinValue = round(min(dtotal.values()),2)
MinName = min(dtotal, key=dtotal.get) 

if len(dtotal) == 1:
    print("The customer {Name} spent {Value}".format(Name=MaxName,Value=MaxValue))
else:
    print("The customer spending most is {Name} : {Value}".format(Name=MaxName,Value=MaxValue))
    print("The customer spending least is {Name} : {Value}".format(Name=MinName,Value=MinValue))

print("*********************************************************************")
print("*********************************************************************")

    
    
    
    
    
    
    