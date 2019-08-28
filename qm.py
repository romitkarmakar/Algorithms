import random

class QM:
    variables = 0
    dontcares = ''
    def __init__(self, no):
          self.variables = no
          self.dontcares = '-'*no     

    def getVars(self):
        v = [chr(val) for val in range(65, 91)]
        return v

    def decToBin(self, n): 
        return bin(n).replace("0b","")

    def reverse(self, s): 
        if len(s) == 0: 
            return s 
        else: 
            return self.reverse(s[1:]) + s[0] 

    def pad(self, num):
        temp = ''
        for i in range(self.variables - len(num)):
            temp += '0'
        temp += num
        return temp

    def isGrayCode(self, a, b):
        flag = 0
        for index, val in enumerate(a):
            if val != b[index]:
                flag +=1
        return (flag == 1)

    def replace_complements(self, a, b):
        temp = ''
        for index, val in enumerate(a):
            if val != b[index]:
                temp += '-'
            else:
                temp += val

        return temp

    def reduce(self, minterms):
        newminterms = []
        checked = [0 for val in range(len(minterms))]
        for indexP, valP in enumerate(minterms):
            for index, val in enumerate(minterms):
                if self.isGrayCode(valP, val):
                    checked.insert(indexP, 1)
                    checked.insert(index, 1)
                    if newminterms.count(self.replace_complements(valP, val)) == 0:
                        newminterms.append(self.replace_complements(valP, val))
        
        for index, val in enumerate(minterms):
            if checked[index] != 1 and newminterms.count(val) == 0:
                newminterms.append(val)
    
        return newminterms

    def getValue(self, a):
        temp = ''
        vars = self.getVars()
        print()
        if a == self.dontcares:
            return '1'
        for index, val in enumerate(a):
            if val != '-':
                if val == '0':
                    temp += vars[index] + '\''
                else:
                    temp += vars[index]

        return temp

    def checkEqArr(self, a, b):
        a.sort()
        b.sort()
        if a == b:
            return True
        else:
            return False

if __name__ == '__main__':
    choice = 'y'
    no = 0
    while choice == 'y':
        print('Enter the number of variables', end=' ')
        no = int(input())
        q = QM(no)

        print('Enter the number of minterms to be generated', end=' ')
        nomin = int(input())
        minterms = []
        minterms = [random.randrange(0, 2**no) for val in range(nomin)]
        minterms.sort()

        print("The generated minterms are")
        print(minterms)
        binminterms = [q.pad(q.decToBin(val)) for val in minterms]
        binminterms.sort()
        while not q.checkEqArr(binminterms, q.reduce(binminterms)):
            binminterms = q.reduce(binminterms)
            binminterms.sort()

        finalResult = [q.getValue(val) for val in binminterms]
        for val in finalResult:
            print(val, end='+')

        print("\nDo you want to continue more (y/n)", end=' ')
        choice = input()