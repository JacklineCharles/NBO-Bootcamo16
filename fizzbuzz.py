def fizz_buzz(num):#creating a function called fizz_buzz
    if isinstance(num, int):#checking whether variable num is an integer	
  
        if num%15 == 0:#if the number is divisible by 3 and 5,print FizzBuzz 
           print ("FizzBuzz")

        elif num%3==0:#if the number is divisible by 3,print Fizz 
            print("Fizz")

        elif num%5==0:#if the number is divisible by 5,print Buzz 
           print("Buzz")

        else: #if the number is not divisible by either 3 and 5,return the number
            return num
  
fizz_buzz(54)
