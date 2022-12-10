# write your code here
person = {
        'name': 'huda',
        'age': '58',
        'hobbies': ['reading', 'swimming'],
        'country' :'syria'
}
print(person['name'])
print(person['age'])
person['age']=66
print(person)
print(len(person))
person['hobbies'].append('uno player')
print(len(person['hobbies']))
def check_hobbies(person):
    if len(person['hobbies']) >= 3:
     print('WOW YOU ARE AMAZING')
check_hobbies(person)