def my_function():
    print('hello, great day')

my_function()

def greet(name):
    print ( "Hi "    +   name)

greet ('Priya')

def greet(name):
    print ( "Hi",name)

greet ('Priya')

def full_name(first, last):
    print(first + " "+ last)

full_name ('Haripriya', 'Prakash')

def full_name(first, last):
    print(first, last)

full_name ('Priya', 'Prakash')

def kids(* names):
    print ('youngest is '+ names[2])
kids('Hari','anu','ammu')

def kids (child3, child2, child1):
    print('youngest is ' + child3)
kids(child2= 'Arun', child3= 'Anu', child1= 'Ammu')

def my_function (**kid):
    print('last name is ' + kid ['lname'])
my_function(fname= 'Kiran', lname= 'Das')

def country(name= "India"):
    print('I am from ' + name)
country()
country('USA')

def my_function (food):
    for x in food:
        print(x)

fruits = ['cherry','apple','orange']
my_function(fruits)

def get_addition(x):
    return 5 + x
print(get_addition(3))

def get_multiplication(x):
    return 5 * x
print(get_multiplication(3))

def get_square (A):
    return A*A
print (get_square(2))

def countdown(n):
    if n == 0:
        print("Done!")
    else:
        print(n)
        countdown(n - 1)
countdown(5)
