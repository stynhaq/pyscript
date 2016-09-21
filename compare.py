number1 = float(input("Enter Number1:  "))
number2 = float(input("Enter Number2:  "))
number3 = float(input("Enter Number3:  "))

if number1 <= number2 and number1 <= number3:
	print("The Minimum Value is ",number1);
elif number2 <= number1 and number2 <= number3:
	print("The Minimum Value is ",number2);
else:
	print("The Minimum Value is ",number3);


if number1 >= number2 and number1 >= number3:
	print('The Maximum Value is ',number1);
elif number2 >= number1 and number2 >= number3:
	print('The Maximum Value is ',number2);
else:
	print('The Maximum Value is ',number3);


if (number1 >= number2 and number1 <= number3) or (number1 >= number3 and number1 <= number2):
	print ("Median is ", number1)
elif (number2 >= number3 and number2 <= number1) or (number2 >= number1 and number2 <= number3):
	print ("Median is ", number2)
else:
	print ("Median is ", number3)
