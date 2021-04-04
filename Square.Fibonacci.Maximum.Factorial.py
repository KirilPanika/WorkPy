def Maximum():
    a = float(input())
    b = float(input())
    c = float(input())

    max = a

    if b > max:
        max = b

    if c > max:
        max = c

    print(max)

    
    

def square1(num):
    return num**2

def square2(num):
    return num**2




def Fibonacci(n, i = 0, f1 = 0, f2 = 1):

    if (i <= n ):
        if (i == 0): 
            print(0, end = ' ')
            Fibonacci(n, i+1, 0, 1)
        
        elif (i == 1):
            print(1, end = ' ')
            Fibonacci(n, i+1, 0, 1)
        
        else:
            print(f1 + f2, end = ' ')
            Fibonacci(n, i+1, f2, f1 + f2)




def factorial( x):
    if (x > 1):
        return factorial(x - 1) * x
    
    else:
        return 1
    
    

#Maximum()

num = 2.5
#print(square1(num))

#print(square2(num))  #Python doesn't have pointers


#Fibonacci(10)


print(factorial(4))
