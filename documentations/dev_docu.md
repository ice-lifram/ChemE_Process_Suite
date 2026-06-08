# Development Documentation: ChemE Process Suite

## Project Overview
The **ChemE Process Suite** is a modular software toolkit designed for chemical engineering calculations. The project is structured to separate the data (reference values), the engine (calculation logic), and the interface (CLI/GUI).

---

## 📂 Module Directory & Functionality

### 1. `engine/data/engine_mmass.py`
**Purpose:** Acts as the primary data loader for atomic weights.
- **Architecture:** Loads molar mass data from an external `elements.json` file to decouple data from logic.
- **Key Components:**
    - `elements_molarmass` (Dictionary): A mapping of chemical element symbols to their respective molar masses in g/mol, populated from JSON.
- **Usage:** Imported by engine modules to provide accurate mass data for stoichiometric calculations.

### 2. `engine/molar_mass_parser.py`
**Purpose:** Translates chemical formulas into molar masses.
- **Architecture:** Uses a recursive descent algorithm to handle simple compounds and nested groups (e.g., `Ca(NO3)2`).
- **Key Functions:**
    - `calculate_molar_mass()`: The main entry point that processes a formula string and returns the total mass.
- **Usage:** Called by `logic.py` to automatically determine molar masses without requiring user lookup.

### 3. `engine/stoichiometry.py`
**Purpose:** Core logic for stoichiometric conversions.
- **Architecture:** Implements an **Atomic Design Pattern** where complex calculations are broken into reusable, pure functions.
- **Atomic Helpers:**
    - `mass_to_moles()`: Converts mass to moles.
    - `moles_to_mass()`: Converts moles to mass.
    - `mole_ratio_conversion()`: Handles inter-substance conversion using coefficients.
- **Composite Functions:**
    - `mass_mass_calculation()`: Chains atomic helpers to solve Mass A -> Mass B problems.

### 4. `engine/titration.py`
**Purpose:** Volumetric analysis calculations.
- **Architecture:** Simplified M1V1 = M2V2 model.
- **Key Functions:**
    - `unknown_molarity()`: Calculates unknown concentration.
    - `required_volume()`: Calculates the volume of standard solution needed.

### 5. `engine/equilibrium.py` (In Development)
**Purpose:** Equilibrium constant and concentration calculations.
- **Planned Architecture:** User-input based constants (Calculator approach).
- **Planned Functions:**
    - `calculate_k()`: Forward calculation of the equilibrium constant.
    - `solve_ice_table()`: Solving for equilibrium concentrations using NumPy roots.
    - `convert_kp_to_kc()`: Conversion between pressure and concentration constants.

### 6. `engine/material_balance.py` (In Development)
**Purpose:** Steady-state mass balance and system analysis.
- **Planned Architecture:** Multi-tier complexity (Bookkeeper -> Analyst -> Designer).
- **Planned Functions:**
    - `calculate_dof()`: Degrees of Freedom analysis to check solvability.
    - `find_missing_mass()`: Total mass balance to find missing stream values.
    - `calculate_mixture_conc()`: Concentration calculations for mixing streams.

### 7. `logic.py`
**Purpose:** The main orchestration layer and User Interface (CLI) handler.
- **Class: `ChESuite`**
    - `__init__(self)`: Initializes the application.
    - `molarmass_tool(self)`: Sub-loop for element lookups.
    - `stoichiometry(self)`: Sub-loop for stoichiometry calculations.
    - `titration(self)`: Sub-loop for titration calculations.
    - `start(self)`: Main hub menu routing users to tools.

---

## 🛠 Technical Implementation Details

### Architectural Patterns
1. **Pure Engine Rule:** Engine files contain no `input()` or `print()` statements. They take arguments and return values. This ensures the logic can be plugged into any interface (CLI or GUI).
2. **Atomic Refactoring:** Complex calculations are broken into the smallest possible logical units (Unit Border vs. Substance Border).
3. **Data Decoupling:** Data is separated from logic, allowing for future transitions to JSON or Database storage.

### Input Normalization Flow
`User Input` -> `.capitalize()` -> `Dictionary Lookup` -> `Result/Error`

---

## 🚀 How to Run
1. Ensure you are in the project root.
2. Execute the logic file:
   ```bash
   python logic.py
   ```
3. Follow the on-screen menu prompts.
