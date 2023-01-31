# A simple script to count the letters in a piece of text

# line one : defines the function which takes one argument "text" which must be a string
# line two : create an empty dictionary which is used to store the letters (key) and the number
#            of times the occur (value)
# line three : this is a for loop to iterate over the given string 
# line four : an if statement to check a) if the letter is a letter using the isalpha() method
#             which returns True if all strings are letters and b) check if the letter already
#             exists in the dictionary, so we only get one key for each letter.
# line five : creates a dictionary key using the for loop letter and the value assigned is achieved
#             by passing letter to the count() method which is used on the text argument passed to
#             the function.
# line six :  the dictinary is returned 


def word_count(text):
    letter_dict = {}
    for letter in text:
        if letter.isalpha() and letter not in letter_dict:
            letter_dict[letter] = text.count(letter)
    return letter_dict


print(word_count("Test this text, please"))


# Output : {'T': 1, 'e': 4, 's': 3, 't': 4, 'h': 1, 'i': 1, 'x': 1, 'p': 1, 'l': 1, 'a': 1}

