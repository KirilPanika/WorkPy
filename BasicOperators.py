def task1():
    num1 = int(input("input first number:  "))
    num2 = int(input("input second number: "))
    print("product is", num1 * num2)
    print("quotient is", num1 / num2)

def task2():
    num1 = float(input("input first number:  "))
    num2 = float(input("input second number: "))
    num3 = float(input("input third number:  "))
    sum = num1 + num2 + num3
    print("sum is {:.2f}".format(sum))    

def task3():
    num1 = float(input("input first number:  "))
    num2 = float(input("input second number: "))
    dp = float(input("number of decimal places:  "))
    sum = num1 + num2
    f = "sum is {:."+str(int(dp))+"f}"
    print(f.format(sum))    

def task4():
    num1 = float(input("input width number:   "))
    num2 = float(input("input length number:  "))
    num3 = float(input("input height number:  "))
    vol = num1 * num2 * num3
    print("volume is", vol, "m3") 
    print("volume is", vol*1000000, "cm3")

def task5():
    num1 = int(input("How old are you in years?  "))
    print("Next birthday you will be", num1 + 1, "years old")

def task6():
    num1 = int(input("Enter days:  "))
    print(num1//7, "week(s) and", num1%7, "day(s)")
    
def task7():
    sec = int(input("Enter seconds:  "))
    hours = sec // 3600
    sec = sec - 3600*hours
    mint = sec // 60
    sec = sec - 60*mint
    print(hours, "hour(s),", mint, "minutes,", sec, "second(s)")

def task8():
    num1 = int(input("Enter km/hr:  "))
    print(round(num1/1.60934449789), "miles/hr")



    
#task1()

#task2()

#task3()

#task4()

#task5()

#task6()

#task7()

task8()


