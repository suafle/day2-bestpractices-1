class Fish:
    def __init__(self):
        '''Constructor for this class'''
        #Create animals
        self.members = ['Tuna','Swordfish','Cod']

    def printMembers(self):
        print('Members Fish Class')
        for member in self.members:
            print('\t%s' %member)

