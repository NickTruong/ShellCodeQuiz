# QUESTION 4
# ----------
# For this question, you must modify the multiply() function 
# such that it multiplies the two positive integers a and b using 
# MAINLY loops, conditions, and addition. Absolutely do NOT use the 
# multiplication operator as that defeats the purpose of this excercise!
# To clarify, only touch the modify() function. Do NOT touch main() here!
#
# You can test whether your multiply function correctly multiplies by 
# running the program. The output of the program will let you know!
# -----------------------------------------------------------------------

def multiply(a, b):
  # Put your code here!
  # Don't forget to "return" a value! Don't print it!
  return

# Please don't touch main 🙂
def main():
  try:
    print("Input two positive integers to multiply.")
    num1 = int(input("Input the first number: "))
    num2 = int(input("Input the second number: "))
    if num1 < 0 or num2 < 0:
      raise
    product = multiply(num1, num2)
    print(f"\nmultiply({num1}, {num2}) results in: {product}")
    if product == num1*num2:
      print("\nThis is correct! ✔️")
      return 1
    elif product == None:
      print(f"multiply({num1}. {num2}) seems to be returning None. " \
       + f"Be sure to return a result! ❌")
    else:
      print("\nThis is incorrect! ❌")
  except:
    print("\nInvalid input!")
