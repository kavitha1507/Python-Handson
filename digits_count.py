def count_digits(number):

    number_str = str(number)
 
    digit_count = 0
    
    for char in number_str:
   
        if char.isdigit():
            digit_count += 1
    
    return digit_count


given_number = 123456
result = count_digits(given_number)
print(f"The total number of digits in {given_number} is: {result}")
