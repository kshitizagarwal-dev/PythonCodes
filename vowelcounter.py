# Definig the vowels
vowel = ['A','a', 'E','e', 'I','i' ,'O','o', 'U','u']
# taking the statement input
sent = input('Enter the statement')
#Intialization
found = []
count_a = 0
count_e = 0
count_i = 0
count_o = 0
count_u = 0

#checking for vowels 
for c in sent:
    if c in vowel:
        found.append(c)
        if c is 'a' or c is 'A':
            count_a +=1
        if c is 'e 'or c is 'E':
            count_e +=1
        if c is 'i' or c is 'I':
            count_i +=1
        if c is 'o' or c is 'O':
            count_o +=1
        if c is 'u' or c is 'U':
            count_u +=1
# converting the counters in list
counter = [count_a, count_e, count_i, count_o, count_u]
#displaying
print('vowels in sentence-',found)
print('Each vowel is repeated as -',counter)

