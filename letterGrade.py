def letter_grade(number):

#Makes sure the the input is between 0 and 100.
    while number < 0 or number > 100:
        number = int(input("Enter your grade here (overall percent between 0 and 100), do not include the % symbol"))

#Takes number and returns letter grade.
    if number <= 100 and number >= 90:
        print('A')
        return
    elif number <90 and number >= 87:
        print('B+')
        return
    elif number < 87 and number >= 80:
        print('B')
        return
    elif number < 80 and number >= 77:
        print('C+')
        return
    elif number < 77 and number >= 70:
        print('C')
        return
    elif number < 70 and number >= 67:
        print('D+')
        return
    elif number < 67 and number >= 60:
        print('D')
        return
    else:
        print('F')
        return

def main():
    number_grade = int(input("Enter your grade here (overall percent between 0 and 100), do not include the % symbol"))
    letter_grade(number_grade)

main()