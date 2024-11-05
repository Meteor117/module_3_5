#Домашка - рекурсия

def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    l = len(str_number) - 1
    if l <= 1:
         return first
    return first * get_multiplied_digits(int(str_number[1:]))


result = get_multiplied_digits(40203)
print(result)
