#Name: Johnathan Sullivan AKA Bruce Wayne_Jung
#Lab10part1
#11/03/2024
#This program receives test scores from a user and displays a letter grade and the average for each score

print(f"Welcome to the Grade and Average Calculator Master Wayne_Jung. ")
print(f"This program accepts 4 test scores, and displays a grade letter and an average")

#This is the main function
def main():
    test1 = int(input("Please enter test score #1: ")) #input test score 1

    grade1 = determine_grade(test1) #determine grade1

    test2 = int(input("Please enter test score #2: "))  #input test score 2

    grade2 = determine_grade(test2) #determine grade2

    test3 = int(input("Please enter test score #3: "))  #input test score 3

    grade3 = determine_grade(test3) #determine grade3

    test4 = int(input("Please enter test score #4: "))  #input test score 4

    grade4 = determine_grade(test4) #determine grade4

    avg = calc_average(test1, test2, test3, test4)

    letter_grade = determine_grade(avg)

    print(f"Grades: {grade1}, {grade2}, {grade3}, {grade4}")
    print(f"Average Score: {avg} Letter Grade: {letter_grade} ")

#calc-average Function
def calc_average(t1, t2, t3, t4):
    return (t1 + t2 + t3 + t4) / 4

#determine_grade function, followed by boolean scores & return grade letters
def determine_grade(score):
    if 90 <= score <= 100:
        return 'A'
    elif 80 <= score < 90:
        return 'B'
    elif 70 <= score < 80:
        return 'C'
    elif 59 <= score < 70:
        return 'D'
    else:
        return 'F'


main()

