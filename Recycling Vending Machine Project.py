class RecyclableItem:
    def __init__(self,name,price):
        self.name=name
        self.price=price

    def setName(self,name):
        self.name=name

    def setPrice(self,price):
        self.price=price

    def getName(self):
        return self.name

    def getPrice(self):
        return self.price

class PlasticBottle(RecyclableItem):
    def __init__(self):
        super().__init__('PlasticBottle',0.50)

class GlassBottle(RecyclableItem):
    def __init__(self):
        super().__init__('GlassBottle',1.00)

class Paper(RecyclableItem):
    def __init__(self):
        super().__init__('Paper',0.10)

class CardBoard(RecyclableItem):
    def __init__(self):
        super().__init__('CardBoard',0.30)

class RecyclingMachine:
    def __init__(self):
        self.itemsInMachine={'PlasticBottle':0,'GlassBottle':0,'Paper':0,'CardBoard':0}
        self.amountToPay=0
        self.itemsAddedByUser={'PlasticBottle':0,'GlassBottle':0,'Paper':0,'CardBoard':0}
        

    def select_product(self):
        print('Enter (1) for Plastic Bottle. ')
        print('Enter (2) for Glass Bottle. ')
        print('Enter (3) for Paper. ')
        print('Enter (4) for CardBoard. ')
        print('Enter (0) to QUIT')
        product=int(input('Enter your choice:  '))
        if product==0:
            quit()
        if product>=1 and product<=4:
            if product==1:
                item=PlasticBottle()
            elif product==2:
                item=GlassBottle()
            elif product==3:
                item=Paper()
            else:
                item=CardBoard()
            numOfItems=int(input('Enter number of items:  '))
            if numOfItems>0 and numOfItems<=50:
                self.accept_product(item,numOfItems)
            else:
                 print('Number of items are not correct start over.')
                 self.select_product()
        else:
             print('Select the right option please.')
             self.select_product()
        

    def accept_product(self,item,numOfItems):
        for i in range(numOfItems):
            if self.itemsInMachine[item.getName()]<51:
                print(item.getName() + ' Accepted')
                self.itemsInMachine[item.getName()]+=1
                self.amountToPay+=item.getPrice()
                self.itemsAddedByUser[item.getName()]+=1
            else:
                print('Item limit reached.')
                break

    def payout(self):
        print ('Amount Paid: ' + '%.2f' %self.amountToPay)
        return float('%.2f' %self.amountToPay)

    def print_reciept(self):
        print('----- Final Reciept -----')
        if self.itemsAddedByUser['PlasticBottle']>0:
            print(str(self.itemsAddedByUser['PlasticBottle'])+' ' +'PlasticBottles'+'    ' + '$'+str(0.50*self.itemsAddedByUser['PlasticBottle']))
        if self.itemsAddedByUser['GlassBottle']>0:
            print(str(self.itemsAddedByUser['GlassBottle'])+' ' +'GlassBottles'+'    ' + '$'+str(1.00*self.itemsAddedByUser['GlassBottle']))
        if self.itemsAddedByUser['Paper']>0:
            print(str(self.itemsAddedByUser['Paper'])+' ' +'Paper'+'    ' + '$'+str(0.10*self.itemsAddedByUser['Paper']))
        if self.itemsAddedByUser['CardBoard']>0:
            print(str(self.itemsAddedByUser['CardBoard'])+' ' +'CardBoard'+'    ' + '$'+str(0.30*self.itemsAddedByUser['CardBoard']))
        print('Number of items:         ' + str(self.itemsAddedByUser['PlasticBottle']+self.itemsAddedByUser['GlassBottle']+self.itemsAddedByUser['Paper']+self.itemsAddedByUser['CardBoard']))
        print('Amount Paid:             '+'%.2f' %self.amountToPay)
        self.amountToPay=0
        self.itemsAddedByUser={'PlasticBottle':0,'GlassBottle':0,'Paper':0,'CardBoard':0}
            

class Driver:
    def __init__(self):
        self.s=RecyclingMachine()
        self.run()

    def run(self):
        self.s.select_product()
        inp=input('Do you have more items? (y)es or (n)o?:  ')
        if inp=='n':
            print('                                                               ')
            self.s.payout()
            print('                                                               ')
            self.s.print_reciept()
            print('                                                               ')
            print('         THANK YOU FOR USING RECYCLING MACHINE                 ')
            print('                                                               ')
            print('                                                               ')
            print('                NEXT USER PLEASE.')
        self.run()
            
            
d=Driver()














            
        

