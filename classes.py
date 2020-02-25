

class User:
    #Constroctor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
    

    def greeting(self):
        return f'My name is {self.name} and I am {self.age}'
    
    def has_birthday(self):
        self.age +=1

#extend class
class Customer(User):

    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0

    def set_balance(self,balance):
        self.balance = balance
    

    def greeting(self):
        return f'My name is {self.name} and I am {self.age} and my balance is {self.balance}'

    
    





#Init user object
brad = User('Brad Traversy','brad@gmail.com',45)

jannet = Customer('Jannet','jane@gmail',27)

jannet.set_balance(500)

print(jannet.greeting())

brad.has_birthday()
print(brad.greeting())