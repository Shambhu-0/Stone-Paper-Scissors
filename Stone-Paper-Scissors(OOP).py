import random

class Game:
    def __init__(self):
        self.choices = { 1: "🪨" ,
                    2: "📃",
                    3: "✂️"
        }
        self.win = { 2 : 1,
                     3 : 2, 
                     1 : 3
        }
        self.pl_choice = 0
        self.my_choice = 0
        self.game_state = True
        self.score = 0
        self.games = 0
        self.games_won = 0
        self.games_tied = 0
        self.games_lost = 0
            
    @staticmethod
    def rules():
        print("Rules To play :".center(100))
        print("1. Select the number before the symbol to play".center(112))
        print("2. At the same time the computer will select a symbol".center(120) )
        print("3. Both will be displayed and winner will be declared".center(120))
        print("\n")
    
    @staticmethod
    def greeting():
        print("🧩 Welcome to Stone-paper-Scissors 🧩".center(150))
        print("\n") 
        
    @staticmethod
    def print_choices():
        print("Choices ...".center(150))
        print("1. 🪨 (Stone)".center(150))
        print("2. 📃 (Paper)".center(150))
        print("3. ✂️ (Scissors)".center(154))
        print("\n")
    
    def assign_symbols(self,choice):
        return self.choices[choice]

    def print_symbols(self, pl_symbol ,my_symbol):
        print(("Player" + " " * 9 + "Computer").center(150))
        print((pl_symbol + " " * 7 + "X" + " " * 6 + my_symbol).center(148))
        print("\n")
    
    def check(self):
        if self.pl_choice == self.my_choice:
            print("Its a tie ...".center(150))
            self.games_tied += 1
        elif self.win[self.pl_choice] == self.my_choice:
            print("Congratulations, You Won !!!".center(150))
            self.update_score()
            self.game_state = False
        else:
            print("You lost !".center(150))
            print("Better luck next time...".center(150))
            self.games_lost += 1
            self.game_state = False
    
    def pl_opt(self):
        while True:
            try:
                self.pl_choice = int(input("Enter your choice: ".rjust(60)))
                if self.pl_choice not in self.choices:
                    print("Enter a valid choice ...".center(110))
                else:
                    break
            except ValueError:
                print("Enter a valid number ...".center(110))
    
    def my_opt(self):
        self.my_choice = random.randint(1,3)
    
    def ask_play_again(self):
        while True:
            reset = input("Wanna play again ?[Y/N]: ".rjust(80)).strip().upper()
            if reset == "Y":
                self.game_state = True
                break
            elif reset == "N":
                self.game_state = False
                self.print_info()
                break
            else:
                print("Enter Valid Option")
                
            
    def update_score(self):
        self.score += 10
        self.games_won += 1
        
    def update_attempts(self):
        self.games += 1
        
    def print_info(self):
        print("\n")
        print("YOUR SCORE CARD".center(150))
        print(f"Total Score = {self.score}".center(150))
        print(f"Total games = {self.games}".center(150))
        print(f"Games Won = {self.games_won}".center(150))
        print(f"Games Lost = {self.games_lost}".center(150))
        print(f"Games Tied = {self.games_tied}".center(150))
        
        
    
    def start_game(self):
        while self.game_state:
            self.print_choices()
            self.pl_opt()
            self.my_opt()
            my_symbol = self.assign_symbols(self.my_choice)
            pl_symbol = self.assign_symbols(self.pl_choice)
            self.print_symbols(pl_symbol,my_symbol)
            self.check()
            self.update_attempts()
            self.ask_play_again()
            
game = Game()
game.greeting()
game.rules()
game.start_game()