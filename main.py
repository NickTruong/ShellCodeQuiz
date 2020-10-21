# Do NOT touch this, but you are free to have a look at this if you are curious!
# It's not that complicated but this stuff isn't what matters.
# GLHF!

import question1
import question2
import question3
import question4
import question5
import question6

num_questions = 6

def anti_cheeky_measures():
  while True:
    try:
      input("\n\n\n\nInput anything to continue...")
      break
    except:
      print("\n\nBruh stop trynna be cheeky.")

def prompt_clear():
  anti_cheeky_measures()
  print('\033c', end="")

def check_progress():
  try:
    f = open("progress.txt", "r")
    progress = f.read()
    if len(progress) == 0:
      return reset_progress(range(0, num_questions))
    progress = progress.split()
    f.close()
    return progress
  except FileNotFoundError:
    return reset_progress(range(0, num_questions))
  except:
    print("ERROR: Failed to check progress.\n\n")
    prompt_clear()
    raise

def update_progress(progress):
  try:
    f = open("progress.txt", "w")
    string = ""
    for item in progress:
      string += f"{item} "
    f.write(string)
    f.close()
  except:
    print("ERROR: Failed to update progress.\n\n")
    reset_progress(progress)
    prompt_clear()

def reset_progress(progress):
  progress = [*progress]
  for i in range(0, len(progress)):
    progress[i] = 0
  update_progress(progress)
  return progress

def main():
  progress = check_progress()
  while True:
    try:
      print("Options:")
      print(f"\t[-1] Reset")
      print(f"\t[0] Quit")
      for i in range(1, num_questions+1):
        print(f"\t[{i}] Run Question {i} {' ✔️ ' if progress[i-1] == '1' else ' ❌ '}")
      choice = int(input("Which option would you like to choose? "))
      if choice == -1:
        progress = reset_progress(progress)
        prompt_clear()
        continue
      elif choice == 0:
        break
      elif choice not in range(1, num_questions+1):
        raise
    except:
      print("\nInvalid input! Please try again.")
      prompt_clear()
      continue
    try:
      if eval(f"question{choice}.main()") == 1:
        progress[choice-1] = "1"
    except:
      print("\nERROR: Either there is a mistake in your code or it is not complete.")
      prompt_clear()
      continue
    try:
      prompt_clear()
    except:
      prompt_clear()
  update_progress(progress)
  print("\n\nGood luck on the midterm! o7")

if __name__ == "__main__":
  main()
