


class Tic_Tac_toe:
     
    def __init__(self):
        self.dic_tionary = {1:"", 2:"", 3:"", 4:"", 5:"", 6:"", 7:"", 8:"", 9:""}
        self.is_full = False
        self.game_won = False
        
    def __repr__(self):
        return "Welcome to Duzy's Tic Tac Toe!"
    
    
    def display(self):
        
        print("  {}     |   {}     |  {}    ".format(self.dic_tionary[1], self.dic_tionary[2], self.dic_tionary[3]))
        print("-------------------------")
        print("  {}     |   {}     |  {}    ".format(self.dic_tionary[4], self.dic_tionary[5], self.dic_tionary[6]))
        print("-------------------------")
        print("  {}     |   {}     |  {}    ".format(self.dic_tionary[7], self.dic_tionary[8], self.dic_tionary[9]))
    
    
    def play(self):

        for i in range(0,8):
            
                
            if i % 2 == 0 and i <= 4:
                print("1  |  2   | 3\n---------------\n 4  |  5   | 6\n---------------\n 7  |  8   | 9")
                print("Pick numbers 1 to 9, to play in their respective spaces")
                print("Your turn Player_X:")
                Player_X = input()
                self.dic_tionary[int(Player_X)] = "X"
                self.display()

                while int(Player_X) not in [1,2,3,4,5,6,7,8,9]:
                    print("Wrong input. Try again")
                    print("Pick numbers 1 to 9, to play in their respective spaces")
                    print("Your turn Player_X:")
                    Player_X = input()
                    self.dic_tionary[int(Player_X)] = "X"
            
            if i % 2 == 1 and i <= 4:
                print("1  |  2   | 3\n---------------\n 4  |  5   | 6\n---------------\n 7  |  8   | 9")
                print("Pick numbers 1 to 9, to play in their respective spaces")
                print("Your turn Player_O:")
                Player_O = input()
                self.dic_tionary[int(Player_O)] = "O"
                self.display()

                while not int(Player_O) in [1,2,3,4,5,6,7,8,9]:
                    print("Wrong input. Try again")
                    print("Pick numbers 1 to 9, to play in their respective spaces")
                    print("Your turn Player_O:")
                    Player_O = input()
                    self.dic_tionary[int(Player_O)] = "O"
            
            if i % 2 == 0 and i > 4:
                self.check_for_win()
                if self.game_won == False:
                    print("1  |  2   | 3\n---------------\n 4  |  5   | 6\n---------------\n 7  |  8   | 9")
                    print("Pick numbers 1 to 9, to play in their respective spaces")
                    print("Your turn Player_X:")
                    Player_X = input()
                    self.dic_tionary[int(Player_X)] = "X"
                    self.display()

            if i % 2 == 1 and i > 4:
                self.check_for_win()
                if self.game_won == False:
                    print("1  |  2   | 3\n---------------\n 4  |  5   | 6\n---------------\n 7  |  8   | 9")
                    print("Pick numbers 1 to 9, to play in their respective spaces")
                    print("Your turn Player_O:")
                    Player_O = input()
                    self.dic_tionary[int(Player_O)] = "O"
                    self.display()

                


                    
                
    def restart_game(self):
        print("Initializing....")
        print(board_1)
        return self.play()     
            

        


    def check_for_win(self):
        if self.dic_tionary[1] == self.dic_tionary[2] and self.dic_tionary[2] == self.dic_tionary[3]:
            self.game_won = True
            self.display()
            print("Game Over! Player_{} won the game.".format(self.dic_tionary[1]))
            print("Do you want to go another round? Enter Yes or No:")
            y = input()
            while  y not in ["Yes", "yes", "No", "no"]:
                print("Wrong input. Enter Yes or No:")
                y = input()
            if y == "Yes" or y == "yes":
                self.restart_game()
            if y == "No" or y == "no":
                print("Thanks for playing. Have a great rest of the day!")
            

        elif self.dic_tionary[4] == self.dic_tionary[5] and self.dic_tionary[5] == self.dic_tionary[6]:
            self.game_won = True
            self.display()
            print("Game Over! Player_{} won the game.".format(self.dic_tionary[4]))
            print("Do you want to go another round? Enter Yes or No:")
            y = input()
            while y not in ["Yes", "yes", "No", "no"]:
                print("Wrong input. Enter Yes or No:")
                y = input()
            if y == "Yes" or y == "yes":
                self.restart_game()
            if y == "No" or y == "no":
                print("Thanks for playing. Have a great rest of the day!")

        elif self.dic_tionary[7] == self.dic_tionary[8] and self.dic_tionary[8] == self.dic_tionary[9]:
            self.game_won = True
            self.display()
            print("Game Over! Player_{} won the game.".format(self.dic_tionary[7]))
            print("Do you want to go another round? Enter Yes or No:")
            y = input()
            while y not in ["Yes", "yes", "No", "no"]:
                print("Wrong input. Enter Yes or No:")
                y = input()
            if y == "Yes" or y == "yes":
                self.restart_game()
            if y == "No" or y == "no":
                print("Thanks for playing. Have a great rest of the day!")

        elif self.dic_tionary[1] == self.dic_tionary[4] and self.dic_tionary[4] == self.dic_tionary[7]:
            self.game_won = True
            self.display()
            print("Game Over! Player_{} won the game.".format(self.dic_tionary[1]))
            print("Do you want to go another round? Enter Yes or No:")
            y = input()
            while y not in ["Yes", "yes", "No", "no"]:
                print("Wrong input. Enter Yes or No:")
                y = input()
            if y == "Yes" or y == "yes":
                self.restart_game()
            if y == "No" or y == "no":
                print("Thanks for playing. Have a great rest of the day!")

        elif self.dic_tionary[2] == self.dic_tionary[5] and self.dic_tionary[5] == self.dic_tionary[8]:
            self.game_won = True
            self.display()
            print("Game Over! Player_{} won the game.".format(self.dic_tionary[2]))
            print("Do you want to go another round? Enter Yes or No:")
            y = input()
            while y not in ["Yes", "yes", "No", "no"]:
                print("Wrong input. Enter Yes or No:")
                y = input()
            if y == "Yes" or y == "yes":
                self.restart_game()
            if y == "No" or y == "no":
                print("Thanks for playing. Have a great rest of the day!")

        elif self.dic_tionary[3] == self.dic_tionary[6] and self.dic_tionary[6] == self.dic_tionary[9]:
            self.game_won = True 
            self.display()
            print("Game Over! Player_{} won the game.".format(self.dic_tionary[3]))
            print("Do you want to go another round? Enter Yes or No:")
            y = input()
            while y not in ["Yes", "yes", "No", "no"]:
                print("Wrong input. Enter Yes or No:")
                y = input()
            if y == "Yes" or y == "yes":
                self.restart_game()
            if y == "No" or y == "no":
                print("Thanks for playing. Have a great rest of the day!")

        elif self.dic_tionary[1] == self.dic_tionary[5] and self.dic_tionary[5] == self.dic_tionary[9]:
            self.game_won = True
            self.display()
            print("Game Over! Player_{} won the game.".format(self.dic_tionary[1]))
            print("Do you want to go another round? Enter Yes or No:")
            y = input()
            while y not in ["Yes", "yes", "No", "no"]:
                print("Wrong input. Enter Yes or No:")
                y = input()
            if y == "Yes" or y == "yes":
                self.restart_game()
            if y == "No" or y == "no":
                print("Thanks for playing. Have a great rest of the day!")

        elif self.dic_tionary[3] == self.dic_tionary[5] and self.dic_tionary[5] == self.dic_tionary[7]:
            self.game_won = True
            self.display()
            print("Game Over! Player_{} won the game.".format(self.dic_tionary[3]))
            print("Do you want to go another round? Enter Yes or No:")
            y = input()
            while y not in ["Yes", "yes", "No", "no"]:
                print("Wrong input. Enter Yes or No:")
                y = input()
            if y == "Yes" or y == "yes":
                self.restart_game()
            if y == "No" or y == "no":
                print("Thanks for playing. Have a great rest of the day!")

        elif self.is_full == True and self.game_won == False:
            print("This is a stalemate. Do you want to go another round? Enter Yes or No:")
            y = input()
            while y not in ["Yes", "yes", "No", "no"]:
                print("Wrong input. Enter Yes or No:")
                y = input()
            if y == "Yes" or y == "yes":
                self.restart_game()
            if y == "No" or y == "no":
                print("Thanks for playing. Have a great rest of the day!")
                
                


        

        
        
        

board_1 = Tic_Tac_toe()
print(board_1)
board_1.play()