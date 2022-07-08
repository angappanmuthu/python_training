# single line command
'''
    Applications of Python:
        * Web Application (Django,Flask,....)
        * Mobile Application (Kivy)
        * IoT (Micropython,CircuitPython)
        * Web Scraping
        * Data Science (ML/DL)
        * Automation
'''

# Variables and datatypes

'''
    Text Type:	str
    Numeric Types:	int, float, complex
    Sequence Types:	list, tuple, range
    Mapping Type:	dict
    Set Types:	set, frozenset
    Boolean Type:	bool
    Binary Types:	bytes, bytearray, memoryview
    None Type:	NoneType

syntax:
    variable_name = value
    varaible_a, variable_b, variable_c = 2, 3, 5
'''

# INTEGER


from typing import final
a = 0

# FLOAT

b = 2.4

# STRING

c = "F"

# or

name = 'mani'

dt = '12/03/2000'

# BOOLEAN

d = False

# NULL

e = None


'''
IO Operation in Python
    * print()
    * input()
'''

# print("Hello")
# int(input("Enter a value : "))

'''
Operators:
    Arithmatic: +, -, *, /, %, //
    Relational: <, >, <=, >=, !=
    Logical: and, or, not
    Identity: is, is not or == or !=
    Membership: in, not in or exists or not exists
'''

''' 
Conditional Statement
    * if <condition>
    * if <condition> ... else
    * if <condition> .... elif <condition> .... else

syntax:

if <condition>:
    # block 1
elif <condition>:
    # block 2
else:
    # block 3

'''

if 2 > 3:
    print("statement 1")
elif 5 > 2:
    print("statement 2")
else:
    print("statement 3")

'''
Loop 
    * for
        syntax:
            for value in array:
                ......
    * while
        syntax:
            while <condition>:
                ......
'''

for i in range(10):         # eg: 1. range(10) -> 0....9 | eg: 2. range(1,10) -> 1....9
    print(i)

v = 0

while (v < 3):
    v = v + 1
    print(v)

'''
    list : List is a collection which is ordered and changeable. Allows duplicate members.
    tuple : Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
    set : Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
    dict : Dictionary is a collection which is ordered** and changeable. No duplicate members.
'''

# list

p = []              # declearing empty list
p = list()          # declearing empty list

p.append(2)
p.insert(1, 'a')
p.remove('a')
# p.sort() # for numbers
p.extend([1, 2, 3, 4, 5, "h", 4.2, False])

# print(p)


# tuple

t = ()
t = tuple()

t = (1, 2, 3, 4, 5, 5, 5)

print(t.count(5))
print(t.index(2))

# set

s = {}
s = set()

s1 = {1, 2, 5, 6, 7}
s2 = {4, 5, 1, 1, 1}

print(s1.intersection(s2))

# dict

sample_dict = {"name": "ramu", "age": 45, "roll_no": "2020541003"}

sample_dict.update({"name": "dhiya"})
sample_dict.pop("name")
print("age", sample_dict.get("age"))  # or sample_dict['age']
print(sample_dict.values())

print(sample_dict)
