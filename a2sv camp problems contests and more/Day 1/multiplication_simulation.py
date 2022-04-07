# Calculate a*b

from addition_simulation import add

def multiply(num1, num2):
    strNum1, strNum2 = str(num1), str(num2)
    answer = 0
    count = 0
    for i in reversed(strNum1):
        value = ''
        carry = 0
        for j in reversed(strNum2):
            tempValue = str(int(i) * int(j) + int(carry))
            if len(tempValue) == 2:
                carry = tempValue[0]
                tempValue = tempValue[1]
            else:
                carry = 0
            value = tempValue + value 
        value = str(carry) + value + count*'0'
        carry = 0
        count += 1
        answer = (add(answer, value))
    return answer

a = multiply(7548643689075486436890253486908598690567560375486436890468099823589754864368907548643689075486436890,75486436890754864368907548643689075486436890253486908598690567560375486436754864368907548643689075486436890890468099823589)
b = (7548643689075486436890253486908598690567560375486436890468099823589754864368907548643689075486436890*75486436890754864368907548643689075486436890253486908598690567560375486436754864368907548643689075486436890890468099823589)
print(a)
print(b)
print(a == str(b))