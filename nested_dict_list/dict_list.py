# Change the value 10 in x to 15.
x = [[5, 2, 3], [10, 8, 9]]
x[1][0] = 15
print(x)

# Change the last_name of the first student from 'Jordan' to 'Bryant'
students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'}
]
students[0]['last_name'] = "Bryant"
print(students)

# In the sports_directory, change 'Messi' to 'Andres'
sports_directory = {
    'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer': ['Messi', 'Ronaldo', 'Rooney']
}
sports_directory['soccer'][0] = 'Andres'
print(sports_directory)

# Change the value 20 in z to 30
z = [{'x': 10, 'y': 20}]
z[0]['y'] = 30
print(z)

# 2
students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]


def iterateDictionary(some_list):
    for i in some_list:
        print(f"First name: {i['first_name']}, Last name: {i['last_name']}")


iterateDictionary(students)

# 3


def iterateDictionary2(key_name, some_list):
    for i in some_list:
        print(i[key_name])


iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)

# 4
dojo = {
    'LOCATIONS': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'INSTRUCTORS': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
    for key, value in some_dict.items():
        print(f"{len(value)} {key}")
        for key in value:
            print(f"{key}")

printInfo(dojo)