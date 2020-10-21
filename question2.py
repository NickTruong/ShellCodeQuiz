# QUESTION 2
# ----------
# For this question, you just have to guess the output of the "bar" function.
# No need to modify this file, just read the code, run it and follow the instructions!
# ------------------------------------------------------------------------------------

# What is the output of this function? (i.e. what does it return?)
def bar():
  y = 0
  counter = 9
  while counter > 0:
    if counter % 9 == 0:
      y += 9
    elif counter % 3 == 0:
      y += 3
    counter -= 3
  return y

# Don't touch this!
def main():
  try:
    user_answer = input("What will the output of bar() be? ")
    if user_answer == str(bar()):
      print("\nCorrect! ✔️")
      return 1
    else:
      print("\nIncorrect 😭   ❌")
  except:
    print("Something went wrong!")
    raise
