import engine.data.engine_mmass as mw
import engine.stoichiometry as st
import engine.molar_mass_parser as parser
import engine.titration as titrate
import engine.material_balance as mb

class ChESuite():
    def __init__(self):
        print("Welcome to ChE Process Suite!")
        self.running = True
    
    def molarmass_tool(self):
        while True:
                element = input("Enter chemical formula (press q to quit): ")
        
                if element.lower() == "q":
                    break

                try:
                    mass = parser.calculate_molar_mass(element)
                    print(f"The molar mass of {element} is {mass} g/mol.")
                except ValueError as e:
                    print(f"Error: {e}")
    
    def stoichiometry(self):
        while True:
            print("n/ Select Options (enter q to exit)")
            print("1. Mass to Mole")
            print("2. Mole to Mass")
            print("3. Mole to Mole")
            print("4. Mass to Mass")
            option = input("Enter option here: ")
            print("----------------------")

            if option == "1":
                try:
                    mass = float(input("Enter mass (g): "))
                    formula = input("Enter compound formula: ")
                    molar_mass = parser.calculate_molar_mass(formula)
                    result = st.mass_to_moles(mass, molar_mass)
                    print(f"For {mass}g of {formula} ({molar_mass} g/mol), the result is {result:.4f} moles.")
                except ValueError as e:
                    print(f"Input Error: {e}")
                except Exception as e:
                    print(f"An unexpected error occurred: {e}")

            elif option == "2":
                try:
                    moles = float(input("Enter moles (mol): "))
                    formula = input("Enter compound formula: ")
                    molar_mass = parser.calculate_molar_mass(formula)
                    result = st.moles_to_mass(moles, molar_mass)
                    print(f"For {moles} moles of {formula} ({molar_mass} g/mol), the result is {result:.4f} g.")
                except ValueError as e:
                    print(f"Input Error: {e}")
                except Exception as e:
                    print(f"An unexpected error occurred: {e}")

            elif option == "3":
                try:
                    moles = float(input("Enter moles of substance A: "))
                    coefA = float(input("Enter coefficient of A in balanced equation: "))
                    coefB = float(input("Enter coefficient of B in balanced equation: "))
                    result = st.mole_ratio_conversion(moles, coefA, coefB)
                    print(f"Using a mole ratio of {coefB}:{coefA}, {moles} moles of A produces {result:.4f} moles of B.")
                except ValueError as e:
                    print(f"Input Error: {e}")
                except Exception as e:
                    print(f"An unexpected error occurred: {e}")

            elif option == "4":
                try:
                    massA = float(input("Enter mass of substance A (g): "))
                    formulaA = input("Enter compound formula for A: ")
                    molarmassA = parser.calculate_molar_mass(formulaA)

                    formulaB = input("Enter compound formula for B: ")
                    molarmassB = parser.calculate_molar_mass(formulaB)

                    coefA = float(input("Enter coefficient of A: "))
                    coefB = float(input("Enter coefficient of B: "))

                    result = st.mass_to_mass_calculations(massA, molarmassA, molarmassB, coefA, coefB)
                    print(f"Starting with {massA}g of {formulaA}, the theoretical yield of {formulaB} is {result:.4f} g.")
                except ValueError as e:
                    print(f"Input Error: {e}")
                except Exception as e:
                    print(f"An unexpected error occurred: {e}")

            elif option == "q":
                break

            else:
                print("Invalid input, please try again.")

    def titration(self):
        while True:
            print("n/Titration Calculator")
            print("1. Molarity")
            print("2. Volume")
            option = input("Enter number (enter q to exit): ")
            try:
                if option == "1":
                    M1 = float(input("Enter Concentration 1: "))
                    V1 = float(input("Enter Volume 1: "))
                    V2 = float(input("Enter Volume 2: "))
                    print(titrate.unknown_molarity(M1, V1, V2))

                elif option == "2":
                    M1 = float(input("Enter Concentration 1: "))
                    M2 = float(input("Enter Concentration 2: "))
                    V1 = float(input("Enter Volume 1: "))
                    print(titrate.unknown_volume(M1, M2, V1))

                elif option.upper() == "Q":
                    break
                else:
                    print("Invalid option; try again")
            except ValueError as e:
                print(f"Invalid input: {e}")
    
    def mass_balance(self):
        while True:
            print("Mass Balance")
            print("1. Degree of Freedom Analysis")
            print("2. Total Mass")
            print("3. Final concentration of two mixture")
            option = input("Enter a number (enter q to exit): ")

            try:
                if option == "1": # This "might" be replaced to ask for list for the equations, which will be appended to a list
                    num_unknown = float(input("Enter number of unknowns: "))
                    num_equations = float(input("Enter number of equations: "))
                    print(mb.dof_calculate(num_unknown, num_equations))

                elif option == "2":
                    inp = []
                    out = []

                    while True:
                        try:
                            in_num = float(input("Add the data for the input (enter any letters to exit: "))
                            inp.append(in_num)
                        except ValueError:
                            break

                    while True:
                        try:
                            out_num = float(input("Add the data for the output (enter any letters to exit: "))
                            out.append(out_num)
                        except ValueError:
                            break

                    print(mb.mass_balance(inp, out))
                
                elif option == "3":
                    flow1 = float(input("Enter flow 1: "))
                    flow2 = float(input("Enter flow 2: "))
                    con1 = float(input("Enter concentration 1: "))
                    con2 = float(input("Enter concentration 2: "))
                    print(mb.mixture_calc(flow1, con1, flow2, con2))

                elif option.lower() == "q":
                    break

            except ValueError as e:
                print(f"Invalid value: {e}")

    # The main menu
    def start(self):
        while self.running:
            print("\nMain Menu:")
            print("M - Molar Mass Lookup")
            print("S - Stoichiometry")
            print("T - Titration")
            print("B - Material Balance")
            print("Q - Quit Program")

            choice = input("Select a tool: ").upper()

            if choice == "M":
                self.molarmass_tool()
            elif choice == "S":
                self.stoichiometry()
            elif choice == "T":
                self.titration()
            elif choice == "B":
                self.mass_balance()
            elif choice == "Q":
                print("Exiting... Goodbye!")
                self.running = False
            else:
                print("Invalid choice, please try again.")

# The initializer: crucial to start the program properly
if __name__ == "__main__":
    app = ChESuite()
    app.start()
