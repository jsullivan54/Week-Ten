#Johnathan Sullivan
#11/03/2024
#lab10part2

#import random library as r to save typing which I spent here... Ugh...
import random as r
print("Welcome to my Dragon Dice Game ")
#Main function with loops
def main():
    #Constant for valid dice types
    DICE_DICE_BABY = {4, 6, 8, 10, 12, 20}
    #Boolean Expression/ loop
    while True:
        # Ask Master Wayne_jung for the die type
        die_type = int(input("Select and enter the die type to roll (4, 6, 8, 10, 12, 20) or enter 0 to exit: "))

        # Sentinel value
        if die_type == 0:
            print("Goodbye Master Wayne_Jung.")
            return  # Exit end the program

        # Check for valid die type
        if die_type not in DICE_DICE_BABY:
            print(f"WRONG: {die_type} That's not a correct die type. You need to choose from {DICE_DICE_BABY}.")
            #make sure you re-ask if they enter a WRONG die type
            int(input("Select and enter the die type to roll (4, 6, 8, 10, 12, 20) or enter 0 to exit: "))
        # Ask how many dice to roll
        num_rolls = int(input(f"How many {die_type}-sided dice would you like to roll? "))

        # Determine the number of rolls
        if num_rolls <= 0:
            print("Error: Please enter a correct number of dice to roll.")
            return  # Re-ask for a valid number of rolls

        # Keep a total of rolls
        total = 0
        rolls_output = "You rolled: "

        # Roll the dice using a while loop
        count = 0
        #my while loop
        while count < num_rolls:
            roll_result = roll(die_type)
            total += roll_result

            # Add the roll result to the output
            if count > 0:
                rolls_output += ", "
            rolls_output += f"{roll_result}"
            # +1 for counting
            count += 1

        # Display the rolls and the total
        print(rolls_output)
        print(f"Total: {total}")
#I added this to the program. It was not a requirement. I hope that I don't lose points for it
        play_again = input("Do you want to play again? (Yes or No):")
        if play_again != 'yes':
            print("Thanks For Playing Master Wayne_Jung. ")
            return

#the one roll function
def roll(die_type):
    return r.randint(1, die_type)  # Use the passed die_type


# Call the main function/ exit the program
main()
