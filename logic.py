import data.engine_mmass as mw


class ChESuite():
    def __init__(self):
        print("Welcome to ChE Process Suite!")
        self.running = True
    
    def molarmass_tool(self):
        while True:
                element = input("Enter element symbols (press q to quit): ")
        
                if element.lower() == "q":
                    break

                element = element.capitalize()
                mass = mw.elements_molarmass.get(element)
    
                if mass is not None:
                    print(element, mass)
                else:
                    print(f"Sorry, {element} is not found in the Periodic Table")
    
    # The main menu
    def start(self):
        while self.running:
            print("\nMain Menu:")
            print("M - Molar Mass Lookup")
            print("S - Stoichiometry (Coming Soon)")
            print("Q - Quit Program")

            choice = input("Select a tool: ").upper()

            if choice == "M":
                self.molarmass_tool()
            elif choice == "S":
                print("Stoichiometry module is under development!")
            elif choice == "Q":
                print("Exiting... Goodbye!")
                self.running = False
            else:
                print("Invalid choice, please try again.")

# The initializer: crucial to start the program properly
if __name__ == "__main__":
    app = ChESuite()
    app.start()
