"""
Created on Wed Jan 17 18:54:01 2018
@author: Brolan
Credit: Fermat's Library
"""
from decimal import Decimal
from decimal import getcontext

def pi(precision):
    getcontext().prec=1000000000
    return sum(1/Decimal(16)**k * 
        (Decimal(4)/(8*k+1) - 
         Decimal(2)/(8*k+4) - 
         Decimal(1)/(8*k+5) -
         Decimal(1)/(8*k+6)) for k in range (1000000000))
print(pi(10))