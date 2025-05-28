#memmoisation 
import sys
sys.setrecursionlimit(100000)

fibDict ={0:1, 1:1}
n=int(input("Enter a number: "))
def fib(n):
    if n <= 1:
        return n
    else:
        if n in fibDict.keys():
            return(fibDict[n])
        else:
            fibDict[n] = fib(n-1) + fib(n-2)  
        return(fibDict[n]) 
print(fib(n))