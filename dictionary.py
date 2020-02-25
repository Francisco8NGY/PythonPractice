
person = {
    'first_name':'Jhon',
    'last_name':'Doe',
    'age':30
}

#use constructor

#person2 = dict(first_name='Sara', last_name='Williams')

#print(person, type(person))

print(person['first_name'])
print(person['last_name'])

#Add key/value

person['phpne'] = '555-555-555'

print(person.keys())
print(person)

#copy dict
person2 = person.copy()
person2['city'] ='Boston'
print(person2)

#Remove item
del(person['age'])

print(person)

#clear
person.clear()
print(person)

people = [
    {'name':'Martha', 'age':30},
    {'name':'Kevin', 'age':25}
]

print(people[0]['name'])
