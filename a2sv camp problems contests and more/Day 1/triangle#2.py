#     *
#    ***
#   *****
#  *******
# *********

def makeTriangle(size):
    for i in range(size):
        print(' '*(size-i), end='')
        print('*'*(2*i + 1))

makeTriangle(10)