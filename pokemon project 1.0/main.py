import scrip2
import time
added = []


class pokemon:
    def __init__(self, name, attack, defense, spatk, spdef):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.spatk = spatk
        self.spdef = spdef


    def call_name(self):
        print(f"you chose {self.name}")
    def call_stats(self):
        print(self.attack)
        print(self.defense)
        print(self.spatk)
        print(self.spdef)

    

class bulbasaur(pokemon):
     pass

Bulbasaur = bulbasaur("bulbasaur", 22, 33, 44, 55)
                          
class charmander(pokemon):
    pass
Charmander = charmander("charmander", 69, 54, 46, 42)

class squirtle(pokemon):
    pass
Squirtle = squirtle("squirtle", 45, 53, 63, 65)

class new_enteries(pokemon):
     def new_entries():
             for add in added:
                  time.sleep(1)
                  print(add, end=" ")
                  print()
                  

Pokemons = [Bulbasaur, Charmander, Squirtle]


while True:
    print("1-> your inventory and stats")
    print("2-> new entry")
    print("3-> see added entries")

    options = input("what choice do you wanna make:> ")
    
    

    while True:
        if options == "1":
                print("choice 1: pokemon stats--")
            
                choice = input("enter a choice: ")
                if choice == "bulbasaur":
                    selected = Pokemons[0]
                elif choice == "charmander":
                    selected = Pokemons[1]
                elif choice == "squirtle":
                    selected = Pokemons[2]
                else:
                    choice == "return"
                    break
                        
            
                selected.call_name()
                time.sleep(1)
                print("your stats are-----")
                time.sleep(1)
                selected.call_stats()

        elif options == "2":
                print("choice 2: your mon and stat--")
                while True:
                    choice = input("enter a new entry: ")
                    if choice == "return":
                        break
                    if choice not in scrip2.pokemon_names:
                        print("not a valid choice enter only kanto")
                        continue
                    
                    added.append(choice)
                break
        elif options == "3":
                 print("choice 3: added mons--")
            
                 new_enteries.new_entries()
                 
                 another = input("enter what to do next: ")
                 if another == "return":
                    break
                 
                 
                        
                      
                
            
                     
                     
                    
                
    
                
                
            