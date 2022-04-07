from random import randint
# Calculate a + b

def add(num1, num2):
    # casting the numbers to comfortable format
    num1Sign, num2Sign = 1,1
    strNum1, strNum2 = str(num1), str(num2)
    if strNum1[0] == '-': 
        num1Sign = -1
        strNum1 = strNum1[1:]
    if strNum2[0] == '-' : 
        num2Sign = -1
        strNum2 = strNum2[1:]
    if num1Sign==num2Sign:
        if len(strNum1) > len(strNum2):
            for i in range(len(strNum1)-len(strNum2)):
                strNum2 = '0' + strNum2
        elif len(strNum2) > len(strNum1):
            for i in range(len(strNum2)-len(strNum1)):
                strNum1 = '0' + strNum1
        carry = 0
        summation = ''
        for i in range(len(strNum1)):
            s = str(int(strNum1[-i-1]) + int(strNum2[-i-1]) + carry)
            # print(s)
            if len(s) == 2:
                carry = int(s[0])
            else:
                carry = 0
            summation = s[-1] + summation
        if carry > 0:
            summation = str(carry) + summation
        while summation[0] == '0':
            summation = summation[1:]

        if num1Sign == -1 and num2Sign == -1:
            return '-' + summation
        else:
            return summation
    else:
        borrow = ''
        summation = ''
        if len(strNum1) == len(strNum2):
            if int(strNum1[0]) > int(strNum2[0]):
                val1 = strNum1
                val2 = strNum2
            elif int(strNum1[0]) == int(strNum2[0]):
                for i in range(len(strNum1)):
                    if (int(strNum1[i]) == int(strNum2[i])):
                        continue
                    elif (int(strNum1[i]) > int(strNum2[i])):
                        val1 = strNum1
                        val2 = strNum2
                        break
                    else:
                        # changing the sign along the variables
                        tempSign = ''
                        val1 = strNum2
                        tempSign = num1Sign
                        num1Sign = num2Sign
                        val2 = strNum1
                        num2Sign = tempSign
                        break
            else:
                # changing the sign along the variables
                tempSign = ''
                val1 = strNum2
                tempSign = num1Sign
                num1Sign = num2Sign
                val2 = strNum1
                num2Sign = tempSign
        else:
            if len(strNum1) > len(strNum2):
                val1 = strNum1
                val2 = strNum2
            else:
                # changing the sign along the variables
                tempSign = ''
                val1 = strNum2
                tempSign = num1Sign
                num1Sign = num2Sign
                val2 = strNum1
                num2Sign = tempSign
        if len(val1) > len(val2):
            for i in range(len(val1)-len(val2)):
                val2 = '0' + val2
        elif len(val2) > len(val1):
            for i in range(len(val2)-len(val1)):
                val1 = '0' + val1
            
        val1 = list(val1)
        val2 = list(val2)
        for i in range(len(val1)):
            if int(val1[-i-1]) < int(val2[-i-1]):
                borrow = '1'
                counter = 2
                while(val1[-i-counter] == '0'):
                    val1[-i-counter] = str(9)
                    counter+=1
                val1[-i-counter] = str(int(val1[-i-counter]) - 1)
            s = str(int(borrow + val1[-i-1]) - int(val2[-i-1]))
            summation = s + summation
            borrow = ''
        while summation[0] == '0':
            summation = summation[1:]

        if num1Sign == -1:
            return '-' + summation
        return summation

for i in range(17390864090):
    a = randint(-10**1000,10**1000)
    b = randint(-10**1000,10**1000)
    c = add(a,b)
    d = str(a+b)
    if (c == d) == False:
        print('sdsdd')
        print(c)
        print('===============')
        print(d)
        print(int(c)-int(d))
        break