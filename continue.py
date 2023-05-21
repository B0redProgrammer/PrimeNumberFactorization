import os
import time

current_primes = []
for file in os.listdir():
    try:
        suffix = file.split('.')[1]

        if suffix == 'txt':
            txt_file = open(file, "r")

            for line in txt_file:
                current_primes.append(int(line.replace("\n", '')))
    except Exception as e:
        pass

last_num = 10000440

def check_div(num):
    for prime in current_primes:
        if num % prime == 0:
            return False
    return True

def check_prime(last_digit):
    checked_num = last_num + last_digit
    if check_div(checked_num):
        file = open(str(last_digit) + ".txt", "a")
        file.write(str(checked_num) + "\n")
        file.close()

        print(checked_num)

        current_primes.append(checked_num)

last_digits = [1, 3, 7, 9]

while True:
    for last_digit in last_digits:
        check_prime(last_digit)
    last_num += 10
