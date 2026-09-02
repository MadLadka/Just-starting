class rpg:
    def __init__(self, player_name, started):
        self.name = player_name
        self.starting_area = started

        
k_items = ["legend key", "ticket"]
password = "the one who is bright"

rpg1 = rpg("ramus", "amber vale")

print(f"your registered name is : {rpg1.name}")
print(f"you started at : {rpg1.starting_area}")

class Movement():
    def up(self):
        print("you move up")
    def down(self):
        print("you move down")
    def left(self):
        print("you move left")
    def right(self):
        print("you move right")

class Inventory():
    def key_items(self):
        items = ", ".join(k_items)
        print(items)
    def add_items(self):
        while True:
            choice = input("enter an item you wanna add: ")
            
            if choice == "break":
                break
            else:k_items.append(choice)

class Location():
    def cities(self, *args):
        for arg in args:
         print(arg)
    def spot(self, **kwargs):
        for key, value in kwargs.items():
            print(f"{key} : {value}")
         

choices = [Movement(), Inventory(), Location()]

while True:
    passw = input("enter the code: ")
    if not passw == password:
        print("wrong code")
    else:
        

        while True:
            choice = input("enter a choice: ")
                    
            if choice == "up":
                choices[0].up()
            elif choice == "down":
                choices[0].down()
            elif choice == "left":
                choices[0].left()
            elif choice == "right":
                choices[0].right()
                        
            
            elif choice == "inv":
                    choices[1].key_items()
            elif choice == "add":
                    choices[1].add_items()
            elif choice == "location":
                    choices[2].cities("Cerulean")
            elif choice == "spot":
                    choices[2].spot(right_now = "pokemon center")    
            
            else:
                print("this command is not available")    

    
            


                    

