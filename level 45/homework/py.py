def count_letters(text):
    return sum(1 for char in text if char.isalpha())

text = input("შეიყვანეთ ტექსტი: ")
print("ასობგერების რაოდენობა:", count_letters(text))
#================================

def check_number(number):
    if number > 0:
        return "დადებითი რიცხვია"
    elif number < 0:
        return "უარყოფითი რიცხვია"
    else:
        return "ნულია"

number = float(input("შეიყვანეთ რიცხვი: "))
print(check_number(number))


#==================================




def categorize_age(age):
    if age < 13:
        return "ბავშვი"
    elif age < 18:
        return "თინეიჯერი"
    elif age < 65:
        return "ზრდასრული"
    else:
        return "პენსიონერი"

age = int(input("შეიყვანეთ ასაკი: "))
print("ასაკობრივი კატეგორია:", categorize_age(age))

#================================




def split_even_odd(numbers):
    evens = [num for num in numbers if num % 2 == 0]
    odds = [num for num in numbers if num % 2 != 0]
    return evens, odds

numbers = list(map(int, input("შეიყვანეთ რიცხვები (გამოყავით მძიმით): ").split(',')))
evens, odds = split_even_odd(numbers)
print("ლუწი რიცხვები:", evens)
print("კენტი რიცხვები:", odds)

#======================





def calculate_average(numbers):
    return sum(numbers) / len(numbers) if numbers else 0

numbers = list(map(int, input("შეიყვანეთ რიცხვები (გამოყავით მძიმით): ").split(',')))
print("საშუალო რიცხვი:", calculate_average(numbers))



