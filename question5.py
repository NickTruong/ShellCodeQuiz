# QUESTION 5
# ----------
# For this question, you must create a Person class. Each Person should have 
# variables that store string values for: First name, Last name, Occupation.
# 
# The program must then take input for each of these values, and it should do 
# so such that with the values inputted, the program can (and will) create 3 
# instances of the Person class and store them in a list!
#
# Finally, the program must print out the first name, last name, and occupation
# of all three instances of the Person class that the program has created.
#
# For this question, do NOT touch main!
# -----------------------------------------------------------------------------

class Person:
  # create the constructor below!
  def for_the_sake_of_not_crashing():
    print("Remove this function once you start working on the Person class.")

# Create an array of Person objects and create 3 instances of Person
# After creation, prints information about each Person instance
# Returns a list of 3 instances of the Person class
def create_and_print_people():
  people = []
  return people

# Don't touch main!
def main():
  people = create_and_print_people()
  if len(people) != 3:
    return
  for p in people:
    if type(p) != Person:
      return
  while True:
    try:
      choice = input("\n\nDo you think you got this question correct? Input 'Y' or 'N': ")
      if choice == 'Y':
        return 1
      elif choice == 'N':
        return 0
      else:
        raise
    except:
      print("Invalid choice. Try again!")