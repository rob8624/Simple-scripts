# function return the sum of two numbers

def addition(num_1, num_2):
   total = num_1, num_2 
   return sum(total)


def addition_two(num_1, num_2):
    return num_1 + num_2

print(addition(10, 32))
print(addition_two(10, 32))


# return the next number from an integer passed

def next_num(number):
    return number + 1

def next_num_two(number):
    next_num = number + 1
    return next_num

print(next_num(1000))
print(next_num_two(100))


# Convert minutes into seconds. Added print statement with f strings just so it read betters when used

def mins_to_secs(mins):
    conversion = mins * 60
    if mins <= 1:
        result = print(f"{mins} minute is {conversion} seconds")
        return result
    else:
        result = print(f"{mins} minutes is {conversion} seconds")
        return result

mins_to_secs(100)

# area of a triangle(muliplty the height with the width, then divide by two)

def triangle_area(height , width):
    return height * width // 2

print(triangle_area(17, 42))

# convert hours into second

def hours_to_seconds(hours):
    return hours * 60 * 60

print(hours_to_seconds(1))


# maximum edge of a triange

def max_edge(side_one, side_two):
    if side_one > 0 and side_two > 0 :
        return side_one + side_two - 1
    else:
        return "Both sides must be positive numbers and greater than 0"

print(max_edge(12, 43))

#...........................................................................

# Write a function that stutters a word as if someone is struggling to read it. 
# The first two letters are repeated twice with an ellipsis ... and space after each, 
# and then the word is pronounced with a question mark ?.

#using f-strings after slicing string

def stutter(word):
    get_stutter = word[0:2]
    return f"{get_stutter}... {get_stutter}... {word}?" 

#using multiplication after slicing string

def stutter_two(word):
    stuttered = word[0:2] 
    return (2 * (stuttered + "...")) + "?"


print(stutter("hellllllllo"))
print(stutter_two("goooodbye"))

# Create a function that takes a list of numbers lst, a string s and return a list of numbers as per the following rules:

# "Asc" returns a sorted list in ascending order.
# "Des" returns a sorted list in descending order.
# "None" returns a list without any modification.

#using sort (having to make a copy)

def sorted_test(lst, s):
    if s == "Asc":
       lst_copy = lst.copy() 
       lst_copy.sort()
       return lst_copy
    elif s == "Des":
        lst_copy = lst.copy()
        lst_copy.sort(reverse=True)
        return lst_copy
    elif s == None:
        return lst

#using sorted() which sorts and makes copy

def sorted_two(lst, s):
     return sorted(lst, reverse=s == "Des") if lst != "None" else lst




def asc_des_none(lst, s):
    if s is None:
        return lst

    try:
        rev = {'Asc': False, 'Des': True}[s] 
        print(s)
    except KeyError:
        raise ValueError(f"Unrecognized sorting direction '{s}'")

    return sorted(lst, reverse=rev)


randoms = [1, 4, 6, 89, 3, 9]    
print(sorted_test(randoms, "Asc"))   
print(sorted_test(randoms, "Des"))
print(sorted_test(randoms, None))


print(sorted_two(randoms, "Asc"))
print(sorted_two(randoms, "Des"))
print(sorted_two(randoms, "None"))

print(asc_des_none(randoms, "Asc"))
print(asc_des_none(randoms, "Des"))
print(asc_des_none(randoms, None))


# Return the Factorial
# Create a function that takes an integer and returns the factorial of that integer. 
# That is, the integer multiplied by all positive lower integers.

def factorial(num):
   result = 1
   for x in range(1, num + 1):
        result = x * result

   return result

print(factorial(5))
       
    

# Number Split
# Given a number, return a list containing the two halves of the number. 
# If the number is odd, make the rightmost number higher.    
   

def num_split(num):
    lst = []
    for x in range(2):
        lst.append(num // 2)
    if num % 2 == 1:
        lst[1]= lst[1]+1
   
    
    return lst

print(num_split(-9))

#list comprehension
 
def num_split_two(num):
    lst = [num // 2 for x in range(2)]
    if num % 2 == 1:
        lst[1]= lst[1]+1
    return lst

print(num_split_two(11))

# Create a function which concatenates the number 7 to the end of every chord in a list. 
# Ignore all chords which already end with 7.

def jazzify(chords):
    lst =  [x + "7" if x[-1] != "7" else x for x in chords]
    return lst


chord_lst = ["G", "F", "C", "C7"]

print(jazzify(chord_lst))

# Default Mood
# Create a function that takes in a current mood and return a sentence in the following format: 
# "Today, I am feeling {mood}". However, if no argument is passed, return "Today, I am feeling neutral".


def mood(*args):
    if args:
        for x in args:
            return f"today i am {x}"
    else:
        return f"today i am neutral"

print(mood("happy"))    
print(mood())

# Sum of v0w3ls
# Create a function that takes a string and returns the sum of vowels, 
# where some vowels are considered numbers.

def vowels_sum(text):
    dict = {"A":4, "E":3, "I":2, "O": 0 , "U": 0 }
    total = 0
    for x in list(text.upper()):
       if x in dict.keys():
        total += dict[x]    
    return total   

print(vowels_sum("robertee"))