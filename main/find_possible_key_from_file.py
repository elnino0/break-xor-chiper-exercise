from decrypt_xor_exc import guess_key, xor_strings
from main.syntactic_analysis import is_text

with open("cipher.txt", "r") as f:
    first_line = f.readline()
    numbersStr_list = first_line.split(",")
    numbers_list = [int(a) for a in numbersStr_list]
    possible_match = guess_key(numbers_list, 3)
    count = 0
    for item in possible_match:
        if is_text(item[0]) is True:
            count += 1
            print("text candidate found ")
            print("key : ", item[1])
            print("text : ", item[0])

    print("total count ", count)
