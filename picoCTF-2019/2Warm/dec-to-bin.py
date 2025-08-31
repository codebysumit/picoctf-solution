# https://play.picoctf.org/practice/challenge/86

'''
decimal_number = 42
binary_representation = bin(decimal_number)
print(binary_representation)
'''

dec = 42
bin = []

while dec > 0:
    bin.append(dec % 2)
    dec = dec // 2

# Reverse the list to get the correct binary representation
bin.reverse()

# print(len(bin))
# print(bin)

length = len(bin)
for i in range(length):
    print(bin[i], end="")

# picoCTF{101010}
