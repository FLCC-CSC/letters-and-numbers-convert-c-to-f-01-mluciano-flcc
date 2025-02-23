# FILE NAME - convert_C_to_F_01.py

# NAME: Marcelo Luciano
# DATE: February 17, 2025
# BRIEF DESCRIPTION: Create a function to convert celsius to fahrenheit



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions below
# 4. The Sample Output has been included in this code for your convenience




    
# Don't forget to cast user input as a float!
    
########## ENTER YER CODE BELOW THIS LINE ##########
def convert_C_to_F():
    celsius = float(input("Enter a temperature in Celsius: "))
    fahrenheit = celsius * 9 / 5 + 32
    print("\n" + celsius + " degrees Celsius is " + fahrenheit + " degrees Fahrenheit.")
convert_C_to_F()
########### END YER CODE ABOVE THIS LINE ###########





########################################
#          SAMPLE OUTPUT
########################################

'''

Enter a temperature in Celsius: 100

100.0 degrees Celsius is 212.0 degrees Fahrenheit.

'''



'''

Enter a temperature in Celsius: -40

-40.0 degrees Celsius is -40.0 degrees Fahrenheit.

'''



'''

Enter a temperature in Celsius: 1

1 degrees Celsius is 33.8 degrees Fahrenheit.

'''



########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What does `float` mean?

A float is a floating point number, or a number with a decimal point.

2. Why do you think it is important to use `float` as opposed to
   a different type of variable type?

A float can provide more accuracy when performing calculations as opposed to integers which can't precisely perform division.

'''
