from zeep import Client, Transport

transport = Transport(cache=None)
client = Client("http://localhost:8000/?wsdl", transport=transport)

answer = input("What operation would you like to use?" +
            "\n1. Addition\n2. Multiplication\n")
first_number = input("Insert your first number: \n")
second_number = input("Insert your second number: \n")

if int(answer) == 1:
    print(client.service.add(first_number, second_number))
else:
    print(client.service.multiply(first_number, second_number))
    
