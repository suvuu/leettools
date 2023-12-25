import csv
import random
import os

vowels = ["A", "E", "I", "O", "U"]
cons = ["B", "C", "D", "F", "G", "J", "K", "L", "M", "N", "P", "S", "T", "V", "Z"]

def build_name():
  name_length = random.randint(3, 3)
  name = ""
  for _ in range(name_length):
    random_vowel = random.choice(vowels)
    random_cons = random.choice(cons)
    name += random_vowel + random_cons
  return name.capitalize()

def build_email(first_name, last_name):
  domain = random.choice(["@gmail.com", "@yahoo.com"])
  email = f"{first_name.lower()}.{last_name.lower()}{domain}"
  return email

# 'a' opens in append mode
def write_to_csv(file_path):
  with open(file_path, 'a', newline="") as file:
    writer = csv.writer(file)
    first_name = build_name()
    last_name = build_name()
    email = build_email(first_name, last_name)
    writer.writerow([first_name, last_name, email])

def generate_names():
  home_dir = os.path.expanduser("~")
  desktop_path = os.path.join(home_dir, "Desktop","names.csv")

  for _ in range(10):
   write_to_csv(desktop_path)


