def basic_commands():
    # create empty set
    s1 = set()
    
    s1 = set([1,2,3,4,5])
    print(s1)
    
    s1 = {1,2,3,4,5}
    print(s1)
    
    # set removes duplicate values
    s1 = {1,2,3,4,5,4,3,5,1}
    print(s1)
    
    print('')# -----------------------------------------ADDING VALUES TO A SET
    
    # add single value to the set
    s1.add(6)
    print(s1)
    
    # add multiple values to a set
    s1.update([6,7,8])
    print(s1)
    
    # add set to another set
    s2 = {8, 9, 10}
    s1.update([6,7,8], s2)
    print(s1)
    
    
    print('')# -----------------------------------------REMOVING VALUES TO A SET
    
    # remove value from a set
    s1 = {1,2,3,4,5}
    s1.remove(5)
    print(s1)
    
    # remove value using discard
    # discard() does not throw an error if the values doesnt exist in the set
    s1 = {1,2,3,4,5}
    s1.discard(6)
    print(s1)

def comparing_sets():
    s1 = {1, 2, 3}
    s2 = {2, 3, 4}
    s3 = {3, 4, 5}
    
    # s1 values that are in s2
    s4 = s1.intersection(s2)
    print(s4)
    
    # s1 values that are in s2 and s3
    s4 = s1.intersection(s2, s3)
    print(s4)
    
    # s1 values that are not in s2
    s4 = s1.difference(s2)
    print(s4)
    
    # s2 values that are not in s1
    s4 = s2.difference(s1)
    print(s4)
    
    # s2 values that are not in s1 and s3
    s4 = s2.difference(s1, s3)
    print(s4)
    
    # values that are not in the intersection of s1 and s2
    s4 = s1.symmetric_difference(s2)
    print(s4)

def remove_duplicates_from_list():
    # remove duplicates from a list
    l1 = [1,2,3,1,2,3]
    
    l2 = list(set(l1))
    print(l2)

def sample_questions(): 
    employees = ['Corey', 'Jim', 'Steven', 'April', 'Judy', 'Jenn', 'John', 'Jane']
    
    gym_members = ['April', 'John', 'Corey']
    
    developers = ['Judy', 'Corey', 'Steven', 'Jane', 'April']
    
    # get employees that have gym membership and are developers
    result = set(gym_members).intersection(developers)
    print(result)
    
    # employees who are neither gym members or developers
    result = set(employees).difference(gym_members, developers)
    print(result)
