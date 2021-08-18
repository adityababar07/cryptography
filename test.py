import random

decrypted = '''abcdefghijklmnopqrstuvwxyz 1234567890`~!@#$%^&*()_-+=}{[]|:;'""'<,>.?/\\'''
encrypted = ''''''

shuffle_list = []
for i in decrypted:
    shuffle_list.append(i)

for i in range(len(shuffle_list)):
    position = random.randint(0, len(shuffle_list)-1)
    encrypted += decrypted[position]

print("Begines=>"+encrypted+"<=Ends")
decrypted.encode()
encrypted.encode()