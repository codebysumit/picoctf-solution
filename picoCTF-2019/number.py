data_str = "16 9 3 15 3 20 6 { 20 8 5 14 21 13 2 5 18 19 13 1 19 15 14 }"

for item in data_str.split():
    if item.isdigit():
        num = int(item)
        char_code = num + ord('A') + 31
        # print(char_code, end=" => ")
        print(chr(char_code), end='')
    else:
        print(item, end='')
print()
