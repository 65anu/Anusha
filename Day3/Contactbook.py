# contact book



# contact Book



howManycontact = int(input("Enter the number of contacts you want to add: "))


contactDictionary = {}

for i in range(0,howManycontact):
    name = input("Enter number:")
    number1 = input("Enter number1:")
    number2= input("Enter number2:")
    imageurl = input("Enter imageurl:")
    email = input("Enter email:")
    website = input("Enter website:")

    contactDictionary[name]= {
    "name":name,
    "number1":number1,
    "number2":number2,
    "imageurl":imageurl,
    "email":email,
    "website":website,
    }
