# Definition of Terms: ChemE Process Suite

This document defines the key technical terms used throughout the development of the ChemE Process Suite, divided into Chemical Engineering and Software Architecture domains.

---

## 🧪 Chemical Engineering Terms

### Core Stoichiometry
- **Molar Mass (Molecular Weight):** The mass of one mole of a chemical substance, typically expressed in grams per mole (g/mol). It is the sum of the atomic weights of all atoms in the formula.
- **Mole (mol):** The SI unit for amount of substance. One mole contains exactly 6.02214076 x 10^23 elementary entities (atoms, molecules, ions).
- **Stoichiometry:** The calculation of relative quantities of reactants and products in chemical reactions.
- **Stoichiometric Coefficient:** The number placed in front of a chemical formula in a balanced equation (e.g., the 2 in 2H2). It represents the molar ratio of the substance in the reaction.
- **Theoretical Yield:** The maximum amount of product that can be produced from a given amount of reactant, assuming 100% efficiency in the reaction.
- **Limiting Reagent (Limiting Reactant):** The reactant that is entirely consumed first in a chemical reaction, thereby limiting the amount of product that can be formed.

### Titration & Volumetric Analysis
- **Molarity (M):** The concentration of a solution expressed as the number of moles of solute per liter of solution (mol/L).
- **Standard Solution:** A solution whose concentration is accurately known.
- **Titer:** The solution of known concentration used to analyze the unknown.
- **C1V1 = C2V2:** The fundamental dilution/titration equation used to determine unknown concentrations.

### Chemical Equilibrium
- **Equilibrium Constant (K):** A value that describes the ratio of products to reactants at equilibrium.
- **Kc:** The equilibrium constant expressed in terms of molar concentrations.
- **Kp:** The equilibrium constant expressed in terms of partial pressures.
- **ICE Table (Initial, Change, Equilibrium):** A systematic method for calculating the concentrations of reactants and products at equilibrium.
- **Physical Root:** In mathematical solving, the specific root that is chemically possible (positive and within initial concentration bounds).

### Material Balance
- **Steady State:** A condition where the variables in a system do not change over time (Mass In = Mass Out).
- **Total Mass Balance:** The conservation of total mass across a process unit.
- **Component Balance:** The conservation of a specific chemical species within a total mass flow.
- **Degrees of Freedom (DoF) Analysis:** A method used to determine if a system of equations is solvable by comparing the number of unknowns to the number of independent equations.
- **Underspecified:** A system where DoF > 0; not enough information to find a unique solution.
- **Overspecified:** A system where DoF < 0; too much information, potentially leading to contradictions.

---

## 💻 Software Architecture Terms

### Design Patterns
- **Pure Engine Rule:** An architectural constraint where the logic layer (engines) performs calculations and returns values but does not interact with the user via input() or print(). This allows the same engine to be used by a CLI, a GUI, or a Web API.
- **Atomic Design Pattern:** The process of breaking a complex calculation into the smallest possible independent functions (e.g., mass_to_moles) that can be reused as building blocks for larger "composite" functions.
- **Pipeline Architecture:** A design where data flows through a series of processing steps. In this project, it refers to the chain of stoichiometry: Mass A -> Moles A -> Moles B -> Mass B.
- **OOP (Object-Oriented Programming):** A programming paradigm based on "objects" (like the ChESuite class) that encapsulate data and behavior, making the code more modular and extensible.

### Parsing & Logic
- **Tokenization:** The process of breaking a string (like a chemical formula) into smaller, meaningful pieces called "tokens" (e.g., breaking H2O into H, 2, O).
- **Recursion:** A programming technique where a function calls itself. In this project, it is used to solve formulas with nested parentheses (e.g., Ca(NO3)2).
- **Regular Expression (Regex):** A sequence of characters that forms a search pattern, used by the parser to identify element symbols and subscripts.
- **Input Normalization:** The process of cleaning user input (e.g., using .capitalize() or .lower()) to ensure it matches the format of the data stored in the dictionary, regardless of how the user typed it.
- **Graceful Error Handling:** Using try-except blocks and .get() methods to prevent the program from crashing when it encounters unexpected input, instead providing a helpful message to the user.
