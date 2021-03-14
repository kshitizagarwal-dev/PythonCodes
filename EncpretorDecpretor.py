#   FUNCTION FOR ENCRYPTING MESSAGE:
def encryptor(key,msg):
    i=0
    count=[0]*10
    for ch in msg:
        #   transformation of each character into next kth character.
        if ch.isalpha():
            temp = ord(ch) + key # ord() for calculating ASCII Code of character 
            # Checking if it is in upper 
            if ch.isupper():
                while temp >90:
                    count[i]=1
                    temp%=90
                    if temp<=90:
                        msg=msg.replace(ch,chr(temp+64))
                        break
                else:
                    msg = msg.replace(ch, chr(temp))
            else:
                while temp>122:
                    count[i]=1
                    temp%=122
                    if temp<=122:
                        msg=msg.replace(ch,chr(temp+96))
                        break
                else:
                     msg=msg.replace(ch,chr(temp))

        #   Increasing each numeric character with k according to the problem
        elif ch.isnumeric():
            ch1=int(ch)
            temp = ch1 + key
            while temp>9:
                temp%=9
                count[i]=1
                if temp <= 9:
                    break
            msg= msg.replace(ch,str(temp))

        #   transformation of each space into @
        elif ch==' ': msg=msg.replace(ch,'@')
        #   transformation of each full stop into #
        elif ch=='.': msg=msg.replace(ch,'#')
        i+=1
    return msg,count

#   FUNCTION FOR DECRYPTING MESSAGE: (In reverse of encryption)
def decryptor(key,msg,count):
    i=0
    for ch in msg:
        if ch.isalpha():
            if ch.isupper():
                msg=msg.replace(ch,chr(ord(ch)-k+count[i]*90))
            else:
                msg=msg.replace(ch,chr(ord(ch)-k+count[i]*122))
        elif ch.isnumeric():
            msg=msg.replace(ch,str(abs(int(ch)-key+count[i]*9)))


        elif ch=='@': msg=msg.replace(ch,' ')
        elif ch=='#': msg=msg.replace(ch,'.')
    return msg



#   FOR MESSAGE SENDER:
if __name__=='__main__':
    print("Message Sender\n\nHello MIT CELL:")
    #   1 < k < 20
    k=int(input('Please enter k value to shift transform message:\t'))
    msg=input('Now please type your message:\t')
    e_msg,count = encryptor(k, msg)
    print(f"You send-\t{e_msg}\n\n")

#   FOR MESSAGE RECEIVER:
    print("Message Receiver\n\nHello Instructor:")
    print(f"You got a message: {e_msg}")
    int(input("To read this in original please type k value for provided by Cell:-"))
    print("Original Message:\t{}".format(decryptor(k,e_msg,count)))
