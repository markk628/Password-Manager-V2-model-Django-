import string
import random

def generate_password():
  # Takes every alphabet (upper and lowercase), number, and special characters and makes a random password
  chars = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
  size = random.randint(8, 12)
  return ''.join(random.choice(chars) for x in range(size))

generate_password()