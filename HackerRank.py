// Ratio 
def ratio(newArray,n):
    positveCount = 0; negativeCount = 0; zeroCount = 0;
    for num in newArray:
        if num > 0:
            positveCount += 1
        elif num < 0:
            negativeCount +=1
        else:
            zeroCount +=1
    f_positiveCount = "{:.6f}".format(positveCount/n)
    f_negativeCount = "{:.6f}".format(negativeCount/n)
    f_zeroCount = "{:.6f}".format(zeroCount/n)
    
    print(f_positiveCount, f_negativeCount, f_zeroCount, sep='\n')
  
ratio( [1,2,3, -1, -7, -8], 6)


// Fizz Buzz 
def fizzBuzz(n):
    for i in range(n+1):
        if i%3==0 and i%5==0:
            print("FizzBuzz")
        elif i%3 ==0 and i%5 !=0:
            print("Fizz")
        elif i%5==0 and i%3 !=0:
            print("Buzz")
        else:
            print(i)
fizzBuzz(100)


// Give an integer and create an array based on the given integer and calculate the ratio of that number
import numpy as np

def ratio(n):
    s1 = []
    if n > 100:
        print("N must be positive and must not be greater than 100")
    else:
        for i in range(n):
            s1.append(i)
        for i in range(n):
            s1.append(-i)
        s1.append(0)
    newArray = np.random.choice(s1, n, replace=False)
    positveCount = 0; negativeCount = 0; zeroCount = 0;
    for num in newArray:
        if num > 0:
            positveCount += 1
        elif num < 0:
            negativeCount +=1
        else:
            zeroCount +=1
    f_positiveCount = "{:.6f}".format(positveCount/n)
    f_negativeCount = "{:.6f}".format(negativeCount/n)
    f_zeroCount = "{:.6f}".format(zeroCount/n)
    
    print(f_positiveCount, f_negativeCount, f_zeroCount, sep='\n')
    

ratio(10)
