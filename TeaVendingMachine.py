# Class

class teaVendingMachine:
# creating  variables
    plain_tea = 20
    ginger_tea = 25
    black_tea = 15
    green_tea = 50

    customer_name = ""
    lis = []
# for initializing by using name
    def __init__(self,name):
        self.customer_name = name


# For making tea only works for Plain and Ginger Tea
    def makeTea(self):
        
        self.tea = int(input('enter the amount of tea leaves in tsp'))
        self.milk = int(input('enter the amount of milk in cups'))
        
        self.lis.append(self.tea)
        self.lis.append(self.milk)
        
        if(bool(input('For sugar type True otherwise type False '))): # asking whether they required sugar or not
            self.sugar = int(input('Enter the amount of sugar in tsp'))
            self.lis.append(self.sugar)
        return self.lis






if __name__ == '__main__':

    name = input('Enter your name')
    # creating instance of class
    obj = teaVendingMachine(name)
    info = {}
     # different choices for customer
    print('press 1 for Plain Tea')
    print('press 2 for Ginger Tea')
    print('press 3 for Black Tea')
    print('press 4 for Green Tea')
    # taking the choice
    ch = int(input())

    if ch == 1:

        info[name] =  obj.makeTea()
        print('The tea is ready!!!')


    if ch == 2:

        info[name] =  obj.makeTea()
        print('The tea is ready!!!')


    if ch == 3:
        print('The tea is ready!!!')

    if ch == 4:
        print('The tea is ready!!!')

    print(info)


