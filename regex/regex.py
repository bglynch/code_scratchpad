import re

# will be searching this multiline string
text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

coreyms.com

321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T

cat
mat
pat
bat

'''

sentence = 'Start a sentence and then bring it to an end'

# ==============================================================================
def string_vs_raw_string():
    # raw string - does not handle '\' in any way
    print('\t tab')
    print(r'\t tab')

'''
will use the re.compile() method to write our patterns
allows us to extract patterns out to variable
make its eaasier to reuse patterns
'''
def match_phoneNumbers(text_to_search):
    pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')
    matches = pattern.finditer(text_to_search)
    # finditer - returns an iterator that contains all of the matches
    
    for match in matches:
        print(match)
    # >>> <_sre.SRE_Match object; span=(1, 4), match='abc'>

def match_phoneNumbers_from_an_other_file():
    with open('data.txt') as f:
        contents = f.read()
        pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')
        matches = pattern.finditer(contents)
        
        for match in matches:
            print(match)
    
def match_phoneNumbers_with_character_set(text_to_search):
    pattern = re.compile(r'\d\d\d[.-]\d\d\d[.-]\d\d\d\d')
    matches = pattern.finditer(text_to_search)
    
    for match in matches:
        print(match)

def match_800_900_phoneNumbers(text_to_search):
    # match only 800 and 900 numbers
    pattern = re.compile(r'[89]00[.-]\d\d\d[.-]\d\d\d\d')
    matches = pattern.finditer(text_to_search)
    
    for match in matches:
        print(match)

def match_digit_range_1_to_5(text_to_search):
    pattern = re.compile(r'[^1-5]')
    matches = pattern.finditer(text_to_search)
    
    for match in matches:
        print(match)

def match_anything_but_letters(text_to_search):
    pattern = re.compile(r'[^a-zA-Z]')
    matches = pattern.finditer(text_to_search)
    
    for match in matches:
        print(match)

def match_phoneNumbers_with_exact_quantifier(text_to_search):
    pattern = re.compile(r'\d{3}.\d{3}.\d{4}')
    matches = pattern.finditer(text_to_search)
    
    for match in matches:
        print(match)

def match_men_names(text_to_search):
    pattern = re.compile(r'Mr\.?\s[A-Z]\w*')
    matches = pattern.finditer(text_to_search)
    
    for match in matches:
        print(match)
        
def match_all_names_using_Group(text_to_search):
    pattern = re.compile(r'(Mr|Ms|Mrs)\.?\s[A-Z]\w*')
    matches = pattern.finditer(text_to_search)
    
    for match in matches:
        print(match)
        

# ==============================================================================
emails = '''
CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net
'''
def match_first_email(text_to_search):
    pattern = re.compile(r'[a-zA-Z]+@[a-zA-Z]+\.com')
    matches = pattern.finditer(text_to_search)
    
    for match in matches:
        print(match)

def match_first_two_email(text_to_search):
    pattern = re.compile(r'[a-zA-Z.]+@[a-zA-Z]+\.(com|edu)')
    matches = pattern.finditer(text_to_search)
    
    for match in matches:
        print(match)

def match_all_email(text_to_search):
    pattern = re.compile(r'[a-zA-Z0-9.-]+@[a-zA-Z-]+\.(com|edu|net)')
    matches = pattern.finditer(text_to_search)
    
    for match in matches:
        print(match)



# ==============================================================================
urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''
def match_all_urls(text_to_search):
    pattern = re.compile(r'https?://(www\.)?\w+\.\w+')
    matches = pattern.finditer(text_to_search)
    
    for match in matches:
        print(match)

def match_all_urls_as_groups(text_to_search):
    pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
    matches = pattern.finditer(text_to_search)
    
    for match in matches:
        print(match)
        print(match.group(0))
        print(match.group(1))
        print(match.group(2))
        print(match.group(3))

def match_all_urls_as_subbed_groups(text_to_search):
    # create a patterns
    pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
    
    # use the pattern to sub out group 2 and 3 for all matches in 'urls'
    subbed_urls = pattern.sub(r'\2\3', text_to_search)
    
    print(subbed_urls)


# ==============================================================================
'''
for all previous example we used the finditer() method
there are other methods available
'''
pattern = re.compile(r'\.') 

matches = pattern.findall(text_to_search) 
# will just return matches as a list of strings. 
# Note that is there is groups it will only return the group

matches = pattern.match(text_to_search) 
# returns the first match
# only matches things that are at the begining of strings
# same as using the carrot(^) in your regex

matches = pattern.search(text_to_search) 
# returns the first match
# returns None if no match found


# ==============================================================================
def match_start_for_uppercase_or_lowercase(text_to_search):
    pattern = re.compile(r'[Ss][Tt][Aa][Rr][Tt]')
    matches = pattern.finditer(text_to_search)
    
    for match in matches:
        print(match)

def match_start_for_uppercase_or_lowercase_with_FLAG(text_to_search):
    pattern = re.compile(r'start', re.IGNORECASE)
    matches = pattern.finditer(text_to_search)
    
    for match in matches:
        print(match)


# ==============================================================================
lines = '''

    04/20/2009; 04/20/09; 4/20/09; 4/3/09
    Mar-20-2009; Mar 20, 2009; March 20, 2009; Mar. 20, 2009; Mar 20 2009;
    20 Mar 2009; 20 March 2009; 20 Mar. 2009; 20 March, 2009
    Mar 20th, 2009; Mar 21st, 2009; Mar 22nd, 2009
    Feb 2009; Sep 2009; Oct 2010
    6/2008; 12/2009
    2009; 2010

'''
def match_with_f_string(text_to_search):
    
    regex = fr'(\d{{1,2}})/(\d{{1,2}})/(\d{{4}}|\d{{2}})'
    date_found = re.findall(regex, lines)
    print(date_found)
    
    var = 'March'
    regex2 = fr'({var})'
    march_found = re.findall(regex2, lines)
    print(march_found)

match_with_f_string(lines)

       
# searching for strings containing MetaCharacters - characters which need to be escaped
pattern = re.compile(r'\.')             # '.'
pattern = re.compile(r'coreyms\.com')   # 'coreyms.com'
pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')   # 'match phone numbers'
pattern = re.compile(r'\d\d\d[.-]\d\d\d[.-]\d\d\d\d') # matches numbers that are seperated with either '.' or '-'
pattern = re.compile(r'[1-5]')   # any digits between 1 and 5
pattern = re.compile(r'[a-z]')   # any lowercase letter between a and z
pattern = re.compile(r'[a-zA-Z]')   # any lowercase and uppercase letter between a and z
pattern = re.compile(r'[^a-zA-Z]')   # any non lowercase and uppercase letter between a and z
pattern = re.compile(r'[^b]at') # match cat,mat,pat but not bat
