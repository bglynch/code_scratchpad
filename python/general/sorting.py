li = [9,1,8,2,7,3,6,4,5]

def basic_sorting():
    '''2 methods: 'sorted()' and '.sort()'
    sorted()  -> returns a new sorted list
    .sort()   -> sorts the list in place and returns None
    '''
    print('Origional List:\t', li)
    # >>> Origional List:  [9, 1, 8, 2, 7, 3, 6, 4, 5]
    
    s_li = sorted(li)
    print('Sorted List:\t', s_li)   
    # >>> Sorted List:     [1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    li.sort()
    print('Origional List:\t', li)
    # >>> Origional List:  [1, 2, 3, 4, 5, 6, 7, 8, 9]


def sorting_in_reverse_order():
    s_li_decending_order = sorted(li, reverse=True)
    print('Decending Sorted List:\t', s_li_decending_order)
    # >>> Decending Sorted List:   [9, 8, 7, 6, 5, 4, 3, 2, 1]
    
    li.sort(reverse=True)
    print('Origional List:\t', li)
    # >>> Origional List:  [9, 8, 7, 6, 5, 4, 3, 2, 1]


def sorting_a_tuple():
    '''
    Sorting a tuple return a list
    '''
    tup = (9,1,8,2,7,3,6,4,5)
    
    s_tup = sorted(tup)
    print('Tuple:\t', s_tup)
    # >>> Tuple:   [1, 2, 3, 4, 5, 6, 7, 8, 9]


def sorting_a_dict():
    '''
    Sorting a dictionary return a list of the dict keys
    '''
    di = {'name': 'Brian', 'job':'software', 'age': None, 'os':'Mac'}
    s_di = sorted(di)
    print('Dict:\t', s_di)
    # >>> Dict:    ['age', 'job', 'name', 'os']


def sorting_with_keys():
    '''
    Here we use a key=abs to sort by the absolute value of the int
    '''
    li = [-6,-5,-4,1,2,3]
    
    s_li = sorted(li)
    s_li_absolute_value = sorted(li, key=abs)
    
    print(s_li)
    # >>> [-6, -5, -4, 1, 2, 3]
    
    print(s_li_absolute_value)
    # >>> [1, 2, 3, -4, -5, -6]


class Employee():
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    
    def __repr__(self):
        return '('+self.name+', '+str(self.age)+', €'+str(self.salary)+')'

e1 = Employee('Carl', 37, 70000)
e2 = Employee('Sarah', 29, 80000)
e3 = Employee('John', 43, 90000)

employees = [e1,e2,e3]


def sorting_class_instances_by_creating_custom_key():
    def e_sort(emp):
        return emp.name
    
    s_employees = sorted(employees, key=e_sort)
    print(s_employees)


def sorting_class_instances_by_attrgetter():
    from operator import attrgetter
    
    s_employees = sorted(employees, key=attrgetter('age'))
    print(s_employees)