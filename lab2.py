def unique (i):
 result=[i[0]]

 for num in i[1:]:
          if num != result[-1]:
            result.append(num)

 return result

print(unique([1, 2, 2, 3, 3, 3, 2, 2, 1]))  
print(unique([1, 2, 3, 3]))               




def split_string(s):
    mid = (len(s) + 1) // 2  
    front = s[:mid]
    back = s[mid:]
    return front, back



def split_and_merge(a, b):
    def split_string(s):
        mid = (len(s) + 1) // 2  # extra char goes to the front if odd
        return s[:mid], s[mid:]

    a_front, a_back = split_string(a)
    b_front, b_back = split_string(b)

    return a_front + b_front + a_back + b_back



print(split_and_merge('abcde', 'xyz'))
s = "ab"
front, back = split_string(s)
print("Front:", front)  
print("Back:", back)    


def all_unique(numbers):
    return len(numbers) == len(set(numbers))
print(all_unique([1, 5, 7, 9]))        
print(all_unique([2, 4, 5, 5, 7, 9]))  


import random

def guess_game():
    print("🎯 Welcome to the Guessing Game!")
    
    while True:
        tries = 10
        number_to_guess = random.randint(1, 100)
        guessed_numbers = set()
        print("\n🔢 I have chosen a number between 1 and 100. Try to guess it!")

        while tries > 0:
            try:
                guess = int(input(f"\nYou have {tries} tries left. Enter your guess: "))
            except ValueError:
                print("❌ Please enter a valid number.")
                continue

            # Out of range
            if guess < 1 or guess > 100:
                print("🚫 Number out of range! Enter a number between 1 and 100.")
                continue

            # Repeated guess
            if guess in guessed_numbers:
                print("⚠️ You've already guessed that number! Try a different one.")
                continue

            guessed_numbers.add(guess)

            # Correct guess
            if guess == number_to_guess:
                print("🎉 Congratulations! You guessed the correct number!")
                number_to_guess = random.randint(1, 100)
                print("🔁 A new number has been generated!")
                continue  # Continue with remaining tries

            # Wrong guess
            tries -= 1
            if guess < number_to_guess:
                print("⬆️ Too low! Try a higher number.")
            else:
                print("⬇️ Too high! Try a lower number.")

        # Out of tries
        print("\n💀 You've used all your tries! The correct number was:", number_to_guess)
        play_again = input("🔄 Do you want to play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            print("👋 Thanks for playing! Goodbye.")
            break

# Run the game
guess_game()
