import engine.data.engine_mmass as mw
import engine.stoichiometry as st

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
    
    def stoichiometry(self):
        while True:
            print("n/ Select Options (enter q to exit"))
            print("1. Mass to Mole")
            print("2. Mole to Mass")
            print("3. Mole to Mole")
            print("4. Mass to Mass")
            option = input("Enter option here: ")
            print("----------------------")

            if option == "1":
                mass = float(input("Enter mass: "))
                molar_mass = mw.elements_molarmass.get(input("Enter element symbol for molar mass: ").capitalize())
                print(st.mass_to_moles(mass, molar_mass)) # output to be refactored soon "f("The result is {function})"; same to other outputs

            elif option == "2":
                moles = float(input("Enter mole: "))
                molar_mass = mw.elements_molarmass.get(input("Enter element's symbol for its molar mass: ").capitalize())
                print(st.moles_to_mass(moles, molar_mass))

            elif option == "3":
                moles = float(input("Enter moles: "))
                coefA = float(input("Enter the coefficient A/number of mole A of compound: "))
                coefB = float(input("Enter coefficient B/number of mole B of compound: "))
                print(st.mole_ratio_conversion(moles, coefA, coefB))

            elif option == "4":
                massA = float(input("Enter mass: "))
                molarmassA = mw.elements_molarmass.get(input("Enter element symbol for molar mass A: ").capitalize()) 
                molarmassB = mw.elements_molarmass.get(input("Enter element symbol for molar mass B: ").capitalize())
                coefA = float(input("Enter coefficient A/number of moles in element A: "))
                coefB = float(input("Enter coefficient B/number of moles in element B: "))
                print(st.mass_to_mass_calculations(massA, molarmassA, molarmassB, coefA, coefB))

            elif option == "q":
                break

            else:
                print("Invalid input, please try again.")

    # The main menu
    def start(self):
        while self.running:
            print("\nMain Menu:")
            print("M - Molar Mass Lookup")
            print("S - Stoichiometry")
            print("Q - Quit Program")

            choice = input("Select a tool: ").upper()

            if choice == "M":
                self.molarmass_tool()
            elif choice == "S":
                self.stoichiometry()
            elif choice == "Q":
                print("Exiting... Goodbye!")
                self.running = False
            else:
                print("Invalid choice, please try again.")

# The initializer: crucial to start the program properly
if __name__ == "__main__":
    app = ChESuite()
    app.start()
