
"""This function can be used for sum like if 4 mean 4+4+4+4=16 or 4*4"""


def sum(n):
    return n*n


"""This function can be use for multiple like if 4 mean 4*4*4*4=256"""


def mul(n):
    ans=1
    for i in range(n):
        ans=ans*n
    return ans


"""Geting input from the user"""

n=int(input())
if n==0:
    print(0)
elif n==1:
    print(2)
else:
    print(sum(n)+mul(n))

