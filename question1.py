# QUESTION 1
# ----------
# For this question, you just have to guess the output of the "foo" function.
# No need to modify this file, just read the code, run it and follow the instructions!
# ------------------------------------------------------------------------------------

# What is the output of this function? (i.e. what does it return?)
def foo():
  x = 5
  for i in range(1, 9, 2):
    x += i
  x /= 3
  return int(x)

# Do not touch!
def main():
  try:
    user_answer = input("What will the output of foo() be? ")
    if user_answer == str(foo()):
      print("\nCorrect! ✔️")
      return 1
    else:
      print("\nIncorrect 😭   ❌")
  except:
    print("Something went wrong!")
    raise
