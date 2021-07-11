import random

class Game:
    
    def computer_input(self):
        
        computer_choice = random.randint(0,2)
        
        if computer_choice == 0:
            computer_choice =='K'
        elif computer_choice == 1:
             computer_choice == 'P'
        elif computer_choice == 2:
            computer_choice =='N'
        
        print ("Komputer wybrał!")
        
        return computer_choice
    
    def user_input(self):
        
        user_choice = input("Jaki symbol chcesz wybrać? K, P, N?")
        
        return user_choice
    
    def run(self, wybor1, wybor2):
        #wybor2 to komputer
        print("GRA SIE ROZPOCZYNA")
        
        if wybor1 == wybor2:
            print("REMIS")
        elif wybor1 == 'K' and wybor2 == 'P':
            print(f"{wybor1} - {wybor2}!")
            print("Wygrał komputer")
        elif wybor1 == 'P' and wybor2 == 'N':
            print(f"{wybor1} - {wybor2}!")
            print("Wygral komputer") 
        elif wybor1 == 'N' and wybor2 == 'K':
            print(f"{wybor1} - {wybor2}!")
            print("Wygral komputer")
        else:
            print(f"{wybor1} - {wybor2}!")
            print("wygral gracz!")