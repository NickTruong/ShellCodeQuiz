# QUESTION 6
# ----------
# For this question, you must modify all functions except for main such that
# the program reads text from "question3.txt", and puts all the words into 
# a dictionary, where the word is the key and the length of the word in the 
# text file is the value (key -> string, value -> int).
#
# Don't worry about accounting for punctuation or anything like that.
# Note: You can get all the "words" in a string by calling .split() on it.
# Example: 
#     string = "Hello and goodbye!"
#     string = string.split() # string becomes ["Hello", "and", "goodbye!"]
#
# At the end, the program should print out the longest word in the dictionary.
#
# This one doesn't have validation built-in.
# You will probably know if it's correct.
# ----------------------------------------------------------------------------

# This should read text from the file "question6.txt" and return the text
def read():
  return "some text"

# This generates a dictionary with the text passed in as parameters
# This should return the dictionary
def generate_dictionary(text):
  words = dict()
  return words

# Do NOT touch main!
def main():
  words = generate_dictionary(read())
  for word in words:
    print(f"{word}   {words[word]}")
  while True:
    try:
      choice = input("\n\nDo you think you got this question correct? Be honest! \nInput 'Y' or 'N': ")
      if choice == 'Y':
        return 1
      elif choice == 'N':
        return 0
      else:
        raise
    except:
      print("Invalid choice. Try again!")