class Birds:
    def __init__(self):
        '''Constructor for this class'''
        #Create animals
        self.members = ['Sparrow','Robin','Duck']

    def printMembers(self):
        print('Members Birds Class')
        for member in self.members:
            print('\t%s' %member)

