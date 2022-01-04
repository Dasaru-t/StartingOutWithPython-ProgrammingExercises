#9. Celsius to Fahrenheit Temperature Converter
celsius = float(input('Enter a temperature in Celsius: '))

#string '.2f', is the format specifier, .2 specifies the precision and f specifies that the data type of the number we are formatting (float).
print('Temperature in Fahrenheit: ',format((9/5)* celsius + 32,'.2f'))