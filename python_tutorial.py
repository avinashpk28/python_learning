"""first_name = "Avinash"
last_name = "pk"
print(first_name,last_name)
print(first_name +" "+ last_name)"""

number = 1
def show_global():
    global number
    number = 2
show_global()    
print(number)


#----Decorator---- 
"""def upper_name(func):
    def make(name):
        name = name.upper()
        func(name)
    return make

@upper_name
def show(name):
    print(name)
show("test python")"""

#----Python file operation----
"""f = open("test_file.txt","r")
print(type(f.read()))"""


