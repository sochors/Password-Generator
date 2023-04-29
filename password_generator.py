import random
import string

password_characters = string.ascii_letters + string.digits + string.punctuation
pass_length = int(input("Jak dlouhé by mělo vaše heslo být? "))

def password_generator(pass_length):
    return "".join(random.choice(password_characters) for i in range(pass_length))

generated_pass = password_generator(pass_length)

print(generated_pass)