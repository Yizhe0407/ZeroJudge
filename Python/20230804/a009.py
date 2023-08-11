words = " !\"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~"
new_words = words[7:] + words[:7]
passwords = dict(zip(new_words, words))

password = input()
for i in password:
    if i in passwords:
        print(passwords[i], end='')
