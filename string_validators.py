def al(str):
     for i in str:
       if 'A' <= i <= 'Z':
           return 'True'
       elif 'a'<= i <='z' :
           return  'True'
       elif'0'<= i <= '9':
           return "True"
       else:
           continue
     return "False"


def alpha(str):
    for i in str:
        if 'A' <= i <= 'Z' or 'a' <= i <= 'z':
            return 'True'
        else:
            continue
    return 'False'


def digit(str):
    for i in str:
        if i >= '0' and i <= '9':
            return 'True'
        else :
            continue
    return 'False'

def lowercase(str):
    for i in str:
        if i >= 'a' and i <= 'z':
            return 'True'
        else :
         continue
    return 'False'


def uppercase(str):
    for i in  str:
        if 'A'<= i <='Z':
            return 'True'
        else:
            continue
    return 'False'

if __name__ == "__main__":
    str = '1aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa1aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa1aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
    print (al(str))

    print(alpha(str))

    print(digit(str))

    print(lowercase(str))
    print(uppercase(str))
