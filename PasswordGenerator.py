import random
import string

def gen_password():
    letters = string.ascii_letters
    digits = string.digits
    sp_symbols = string.punctuation
    total = letters + digits + sp_symbols

    password = random.sample(total, k=9)
    conv_list = map(str, password)
    result = "".join(conv_list)
    print(f"Your password: {result}")

gen_password()
