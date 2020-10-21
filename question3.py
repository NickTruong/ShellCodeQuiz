# QUESTION 3
# ----------
# For this question, you just have to guess the output of the "bar" function.
# No need to modify this file, just read the code, run it and follow the instructions!
# ------------------------------------------------------------------------------------

# What is the output of this function? (i.e. what does it return?)
def baz():
  z = [0, 1, 3, 4, 5, 8, 9, 11, 12, 16, 2, 3, 4]
  result = 0
  for i in range(0, len(z)):
    if z[i] % 4 == 0:
      result += z[i]
  return result

# Stay away from my main()!
def main():
  try:
    user_answer = input("What will the output of baz() be? ")
    if user_answer == str(baz()):
      print("\nCorrect! ✔️")
      return 1
    else:
      print("\nIncorrect 😭   ❌")
  except:
    print("Something went wrong!")
    raise
