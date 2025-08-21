num = int(input("Enter a Number : ")) #Taking integer type of  input from the user


if num > 1 :#Comparing the integer type of input number given by the user with 1,if input is greater than 1,the it moves to the for loop

    for i in range(2,num):#it consisting of numbers from 2 to num-1 
    
        if num % i == 0:#it divides the num with the range values(2,3,4....,num-1)
           
            print("Not a Prime Number")#if the num is divisible by range values then,it prints Not a Prime Number 
            
            break #break keyword is used to stop,when above print function is true,(break)it doesn't check further
        
    else: #if num is not divisible by i or if condition is not satisfied,then else part will be executed
            
            print("It is a prime Number") #It prints,It is a prime Number
else:#if the user is given input as less than 1  then this else will be executed
    print("It is  a prime Number")#it prints It is  a prime Number