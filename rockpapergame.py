import random

class RockPaperScissorsGame:
    def __init__(self):
        self.choices = ["rock", "paper", "scissors"]
        self.user_score = 0
        self.computer_score = 0

    def get_computer_choice(self):
        return random.choice(self.choices)

    def get_user_choice(self):
        user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
        while user_choice not in self.choices:
            print("Invalid choice. Please try again.")
            user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
        return user_choice

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "It's a tie!"
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            self.user_score += 1
            return "You win!"
        else:
            self.computer_score += 1
            return "Computer wins!"

    def display_score(self):
        print(f"Score - You: {self.user_score}, Computer: {self.computer_score}")

    def play(self):
        print("Welcome to Rock-Paper-Scissors game..!")
        while True:
            user_choice = self.get_user_choice()
            computer_choice = self.get_computer_choice()
            print(f"You chose: {user_choice}")
            print(f"Computer chose: {computer_choice}")
            result = self.determine_winner(user_choice, computer_choice)
            print(result)
            self.display_score()
            
            next_calculation = input("Do you want to play another round? (yes/no): ").lower()
            if next_calculation != 'yes':
                print("Thank you for playing Rock-Paper-Scissors. Goodbye!")
                break

if __name__ == "__main__":
    game = RockPaperScissorsGame()
    game.play()
