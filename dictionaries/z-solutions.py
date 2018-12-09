def exercise01():
    inventory = {
        'gold' : 500,
        'pouch' : ['flint', 'twine', 'gemstone'],
        'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
    }
    
    print(inventory)
    
    inventory['key'] = ['seashell', 'strange berry','lint']
    
    inventory['backpack'].sort()
    
    inventory['backpack'].remove('dagger')
    
    inventory['gold'] += 50
    
    print(inventory)


def exercise02():
    #Create the prices dictionary:
    prices={}
    #Add values
    prices["banana"]=4
    prices["apple"]= 2
    prices["orange"]= 1.5
    prices["pear"]= 3
    
    #Create the stock dictionary
    stock={}
    #Add values
    stock["banana"]= 6
    stock["apple"]= 0
    stock["orange"] =32
    stock["pear"]= 15
    
    
    for fruit in prices:
        print(fruit)
        print('price: ' + str(prices[fruit]))
        print('stock: ' + str(stock[fruit]))
        
    total = 0
    for fruit in prices:
        st = stock[fruit]
        pr = prices[fruit]
        total += st*pr
    
    print(total)


def exercise03():
    grocery_list = ['banana', 'orange', 'kiwi', 'apple']
    
    stock = {
        "banana": 6,
        "apple": 0,
        "orange": 32,
        "pear": 15
    }
    
    prices = {
        "banana": 4,
        "apple": 2,
        "orange": 1.5,
        "pear": 3
    }
    
    
    def compute_bill(food_list):
        total = 0
        for item in food_list:
            if item not in prices:
                print(item + ' was not in the shop')
            elif stock[item] == 0:    
                print(item + ' was not in stock')
            else:
                total += prices[item]
                stock[item] -= 1
        print(stock)
        return total
    
    print(compute_bill(grocery_list))

def exercise04():
    # PART 01--------------------------------------------------
    llyod = {}
    alice = {}
    tyler = {}
    
    llyod['name'] = 'Llyod'
    alice['name'] = 'Alice'
    tyler['name'] = 'Tyler'
    
    llyod['homework'] = []
    alice['homework'] = []
    tyler['homework'] = []
    
    llyod['quizzes'] = []
    alice['quizzes'] = []
    tyler['quizzes'] = []
    
    llyod['tests'] = []
    alice['tests'] = []
    tyler['tests'] = []
    
    
    # PART 02--------------------------------------------------
    lloyd = {
      "name": "Lloyd",
      "homework": [90.0,97.0,75.0,92.0],
      "quizzes": [88.0,40.0,94.0],
      "tests": [75.0,90.0]
    }
    alice = {
      "name": "Alice",
      "homework": [100.0, 92.0, 98.0, 100.0],
      "quizzes": [82.0, 83.0, 91.0],
      "tests": [89.0, 97.0]
    }
    tyler = {
      "name": "Tyler",
      "homework": [0.0, 87.0, 75.0, 22.0],
      "quizzes": [0.0, 75.0, 78.0],
      "tests": [100.0, 100.0]
    }
    
    students = [lloyd, alice, tyler]
    
    for student in students:
        print(student['name'])
        print(student['homework'])
        print(student['quizzes'])
        print(student['tests'])
        
    def average(list_numbers):
        '''
        list_number: list containing ints or floats
        '''
        average = sum(list_numbers)/len(list_numbers)
        return average
        
    def get_average(student):
        '''
        students: dictionary
        '''
        homework = average(student['homework'])
        quizzes = average(student['quizzes'])
        tests = average(student['tests'])
        
        weighted_avg = homework*.1 + quizzes*.3 + tests*.6
        
        return weighted_avg
    
    
    def get_letter_grade(score):
        '''
        students: int or float
        '''
        if score >= 90:
            return 'A'
        elif score >= 80:
            return 'B'
        elif score >= 70:
            return 'C'
        elif score >= 60:
            return 'D'
        else:
            return 'F'
    
    print(get_letter_grade(get_average(lloyd)))
    
    def get_class_average(students):
        '''
        students: list of dictionaries
        '''
        results = []
        for student in students:
            results.append(get_average(student))
        return average(results)
    
    students_average = get_class_average(students)
    
    print(students_average)
    
    print(get_letter_grade(students_average))