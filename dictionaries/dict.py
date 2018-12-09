student = {'name': 'John', 'age': 25, 'courses': ['Maths', 'Physics']}

def get_values(student):
    print(student)
    # >>> {'age': 25, 'name': 'John', 'courses': ['Maths', 'Physics']}
    
    print(student['name'])
    # >>> John
    
    print(student['courses'])
    # >>> ['Maths', 'Physics']
        
    ''' here we try to access a key that does not exits
        this throws an error '''
    print(student['phone'])
    # >>> Traceback (most recent call last):
    # >>>   File "dict.py", line 10, in <module>
    # >>>     print(student['phone'])
    # >>> KeyError: 'phone'

def get_values_using_get_method(student):
    '''
    using the get method here we can see that it returns 'None' instead of an error
    '''
    print(student.get('name'))
    # >>> John
    
    print(student.get('phone'))
    # >>> None

def get_values_using_get_method_with_fail_return(student):
    ''' 
    can give a second arguemen to the get method to return on error 
    '''
    print(student.get('name', 'Not found'))
    # >>> John
    
    print(student.get('phone', 'Not found'))
    # >>> Not found

def add_new_key(student):
    student['phone'] = '555-5555-555'
    
    print(student.get('phone', 'Not found'))
    # >>> 555-5555-555

def update_dict_key(student):
    print(student)
    # >>> {'age': 25, 'name': 'John', 'courses': ['Maths', 'Physics'], 'phone': '555-5555-555'}
    
    student['name'] = 'Jane'
    
    print(student)
    # >>> {'age': 25, 'name': 'Jane', 'courses': ['Maths', 'Physics'], 'phone': '555-5555-555'}

def update_many_dict_keys(student):
    print(student)
    # >>> {'name': 'John', 'age': 25, 'courses': ['Maths', 'Physics']}
    student.update({'name':'Jane', 'age': 26, 'phone': '444-4444-444'})
    
    print(student)
    # >>> {'name': 'Jane', 'age': 26, 'courses': ['Maths', 'Physics'], 'phone': '444-4444-444'}
    
def delete_item(student):
    del student['age']
    
    print(student)
    # >>> {'name': 'John', 'courses': ['Maths', 'Physics']}
    
def delete_item_but_save_value(student):
    
    age = student.pop('age')
    
    print(student)
    # >>> {'name': 'John', 'courses': ['Maths', 'Physics']}
    
    print(age)
    # >>> 25

def get_data_from_dict(student):
    print(len(student))
    # >>> 3
    
    print(student.keys())
    # >>> dict_keys(['name', 'age', 'courses'])
    
    print(student.values())
    # >>> dict_values(['John', 25, ['Maths', 'Physics']])
    
    
    print(student.items())
    # >>> dict_items([('name', 'John'), ('age', 25), ('courses', ['Maths', 'Physics'])])
    
    for key in student:
        print(key)
    # >>> name
    # >>> age
    # >>> courses
    
    print('')
    for key in student.items():
        print(key)
    # >>> ('name', 'John')
    # >>> ('age', 25)
    # >>> ('courses', ['Maths', 'Physics'])    
    
    
    print('')
    for key,value in student.items():
        print(key, value)
    # >>> name John
    # >>> age 25
    # >>> courses ['Maths', 'Physics']# >>> 