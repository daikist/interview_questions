from itertools import permutations
import sys
import numpy as np

# [0, 0, 2, 2, 3, 4, 4, 8, 8, 9, 9]
input_vector = ([0, 0, 2, 2, 3, 4, 4, 8, 8, 9, 9])
# since this is a telephone number simulator we will only accept numbers from 0 to 9
# checking if vector contains only accepted numbers


def check_vector(input):
    for num in input:
        if (num < 0 or num > 9) or (len(input) != 11):
            print("This vector can not be used for the generator, please enter numbers between 0 and 9 and only enter "
                  "11 numbers")
            sys.exit()
    return print("This vector can be used for the generator, please wait.")


check_vector(input_vector)

perms = list(permutations(input_vector))
# eliminating possibility of duplicates converting to set and then list again
perms = list(set(perms))
primes = [2, 3, 5, 7]
numbers = []

for perm in perms:
    # digit counter, will help for some rules (e.g. nines)
    digit_count = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
        9: 0
    }
    for p in perm:
        digit_count[p] += 1
        # end digit counter

        # last number is prime
    if perm[-1] in primes:
        # second to last divisible with last
        if perm[-2] % perm[-1] == 0:
            #  5 6 7 divisible by same number considering that 1 is not part of the list of divisors
            if (perm[4] != 0) & (perm[5] != 0) & (perm[6] != 0):

                def check_divisibility_all(check_numbers, divisors):
                    return all(n % divisors == 0 for n in check_numbers)

                check_numbers = [perm[4], perm[5], perm[6]]
                num = [2, 3]
                if (check_divisibility_all(check_numbers, num[0])) or (check_divisibility_all(check_numbers, num[1])):
                    # all 3 surrounded by same number
                    for z in range(0, len(perm) - 1):
                        if perm[z] == 3:
                            if (z - 1 >= 0) & (z + 1 <= 10):
                                if perm[z - 1] == perm[z + 1]:
                                    # this rule only applies if there are two or more nines

                                    satisfy = True
                                    for j, digit in enumerate(perm):
                                        if digit == 9:
                                            if not ((j < len(perm) - 2 and digit_count[perm[j + 1]] == 1 and perm[j + 2] == 9) or (
                                                    j > 2 and digit_count[perm[j - 1]] == 1 and perm[j - 2] == 9)):
                                                satisfy = False
                                    if satisfy:

                                        # e.g. number:
                                        # [0,0,7,8,2,9,1,9,4,9,3]

                                        # all 8 are consecutive
                                        eights = [j for j, num in enumerate(perm) if num == 8]
                                        if sorted(eights) == list(range(min(eights), max(eights) + 1)):
                                            # AB separated by 8s

                                            max_eight = max(eights)
                                            min_eight = min(eights)
                                            if max_eight < len(perm) - 1 and min_eight > 0:
                                                # print(perm[max_eight+1])
                                                # print(perm[min_eight-1])

                                                if digit_count[perm[max_eight + 1]] == 2 and digit_count[perm[min_eight - 1]] == 2 \
                                                        and perm[max_eight + 1] != perm[min_eight - 1]:
                                                    numbers.append(perm)

# function to convert arrays to venezuelan telephone number format


def convert_list_to_string(list_of_arrays):
    # convert list to string
    string = ''.join(map(str, list_of_arrays))

    # Split the string into groups of 4, 3, and 4 characters
    groups = [string[:4], string[4:7], string[7:]]

    # Join the groups with spaces
    result = ' '.join(groups)

    return result


ven_telephone_numbers = []

for numb in numbers:
    new_phone_number = convert_list_to_string(numb)
    ven_telephone_numbers.append(new_phone_number)
print(ven_telephone_numbers)

# Since this is a mobile phone we can search for the codes for each Mobile Phone Carrier which are
digitel = 412
movistar = 414, 424
tesan = 415
movilnet = 416, 426
digicel = 417
infonet = 418
# Since there are 0 values of 1 and 6 in the input vector, we can assume that the number we're looking for is a movistar
# number which means that it starts with 424.
# We can also see that the vector contains 11 numbers when Venezuelan numbers are
# usually structured as" 0 + (area code or carrier code) + 7 numbers". The 0 represents the trunk prefix used in several
# countries to initiate a call and to avoid miscommunication.
# This means that we're looking for a number that has a 0 (trunk prefix) in the beginning and is followed with 424.

sms_number = []
for sms in ven_telephone_numbers:
    if sms[:4] == '0424':
        sms_number.append(sms)

print(sms_number)
