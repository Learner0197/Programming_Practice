
# Q1
def add_numbers(*a):
    s = 0
    for i in a:
        s += i
    return s

print(add_numbers(1, 2, 3, 4, 5))

# Q2
def performAction(l, n):
    new_list = []
    for i in range(0, len(l), n):
        new_list.append(l[i:i+n])
    return new_list

my_list =[1,2,3,"a","b","c"]
n_val = 3
print(performAction(my_list, n_val))

# Q3
def full_names(names, surnames):
    full_names = []
    for i in range(len(names)):
        full_names.append(f"{names[i]} {surnames[i]}")
    return full_names

names_list = ["Arnav", "Aditya", "Rahul"]
surnames_list = ["Jade", "Sharma", "Kumar"]
print(full_names(names_list, surnames_list))

# Q4
def separate_elements(x):
    odds = []
    evens = []
    primes = []

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    for num in x:
        if isinstance(num, int):
            if num % 2 == 0:
                evens.append(num)
            else:
                odds.append(num)
            if is_prime(num):
                primes.append(num)
    return odds, evens, primes



# Demonstration for Question 3


# Demonstration for Question 4
data=[65,3,26,7,19,54,32]
odds_list, evens_list, primes_list = separate_elements(data)
print(odds_list)
print(evens_list)
print(primes_list)
