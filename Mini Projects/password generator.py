import random

Capital_letters = [chr(i) for i in range(65, 91)]
Lowercase_letters = [chr(i) for i in range(97, 123)]
symbols = ["!", "@", "#", "$", "%", "&", "-", "*"]
number = ["1", "2", "3", "5", "4", "6", "7", "8", "9", "0"]
l_random_pass = [random.sample(symbols, 2),
                 random.sample(number, 2),
                 random.sample(Lowercase_letters, 2),
                 random.sample(Capital_letters, 2)]
random_pass = []
for i in range(4):
    for j in range(2):
        random_pass.append(l_random_pass[i][j])
password = ""
pass_ = random.sample(random_pass, 8)
for i in pass_:
    password += i
print(password)
