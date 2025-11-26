import string 
import random
import re 


email = input("Enter your email id: ")

pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

if not re.match(pattern, email):
    print("❌ Invalid email format!")
    exit()


l = int(input("Enter the length of the password required: "))

def password_gen(l):
    username = email.split("@")[0]

    part = ''.join(random.choice(username) for _ in range (4))
    

    special = random.choice(string.ascii_letters)
    numbers = ''.join(random.choice(string.digits) for _ in range(2))
    secure = random.choice(string.printable)
    hex = ''.join(random.choice(string.hexdigits) for _ in range(2))

    parts = [special , numbers , secure , hex , part]

    random.shuffle(parts)

    password_base = ''.join(parts)

    if l < len(password_base):
        return password_base[:l]
    
    left = l - len(password_base)

    addition = string.ascii_letters + string.digits
    extra = ''.join(random.choice(addition) for _ in range(left))
    
    return password_base + extra

print("", password_gen(l))
