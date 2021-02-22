class Mammals:
    def __init__(self):
        '''Constructor for this class'''
        #Mammals members
        self.members = ['Tiger','Elephant','Wild Cat']
    
    def printMembers(self):
        print('Members Mammals class')
        for member in self.members:
            print('\t%s' % member)
