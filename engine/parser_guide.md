# Molar Mass Parser Guide

This document provides a detailed technical analysis of the `molar_mass_parser.py` engine and its integration into the `logic.py` interface.

## 🎯 Purpose
The parser transforms a chemical formula string (e.g., `Ca(NO3)2`) into its total molar mass (g/mol) by translating chemical "grammar" into mathematical operations.

---

## 🔍 Technical Analysis: `engine/molar_mass_parser.py`

### 1. The `calculate_molar_mass(formula)` Function
This is the entry point of the engine. It acts as a wrapper around the recursive parsing logic.

- **Input:** A string representing the chemical formula.
- **Output:** A float representing the total molar mass, rounded to 4 decimal places.
- **Error Handling:** It wraps the internal parser in a `try-except` block to ensure that any syntax or lookup errors are raised as `ValueError`, which the `logic.py` layer can then catch and display to the user.

### 2. The `parse_formula(formula, index)` Inner Function
This is a **recursive function**. Recursion is used here because chemical formulas can have "nested" structures (parentheses inside parentheses).

#### **The Logic Flow:**
The function iterates through the string using an `index` pointer.

**A. Handling Parentheses `(` (The Recursive Dive)**
```python
if char == '(':
    group_mass, next_index = parse_formula(formula, index + 1)
```
When a `(` is encountered, the function calls *itself*. This creates a new "local" mass counter for the group. It continues parsing until it hits a `)`.

**B. Handling the Group Multiplier**
```python
multiplier_match = re.match(r'^(\d+)', formula[index:])
if multiplier_match:
    multiplier = int(multiplier_match.group(1))
    group_mass *= multiplier
```
After returning from a group (after the `)`), the parser looks for a number immediately following the closing parenthesis. If found, it multiplies the entire group's mass by that number.

**C. Handling Elements `[A-Z][a-z]*`**
```python
element_match = re.match(r'^([A-Z][a-z]*)', formula[index:])
```
The parser uses a Regular Expression to identify elements. It looks for one uppercase letter followed by zero or more lowercase letters. This allows it to correctly distinguish between:
- `Co` (Cobalt) $\rightarrow$ One element.
- `CO` (Carbon Monoxide) $\rightarrow$ Two elements (Carbon and Oxygen).

**D. Handling Subscripts `(\d+)`**
After finding an element, it checks for a trailing number. If `H2` is found, it retrieves the mass of `H` and multiplies it by `2`.

---

## 🔗 Integration with `logic.py`

The parser is integrated as a service that `logic.py` calls whenever a molar mass is needed.

### 1. Import and Initialization
```python
import engine.molar_mass_parser as parser
```
The parser is imported as a module, keeping the interface layer clean.

### 2. The Request-Response Pattern
In `logic.py`, the interaction follows this flow:
1. **User Input:** `formula = input("Enter compound formula: ")`
2. **Engine Call:** `molar_mass = parser.calculate_molar_mass(formula)`
3. **Error Catching:** 
   ```python
   try:
       # ... call parser ...
   except ValueError as e:
       print(f"Input Error: {e}")
   ```
   Because the parser raises `ValueError` for unknown elements or bad syntax, `logic.py` can display a clean error message instead of crashing.

### 3. Application in Stoichiometry
The parser is used as the first step in the stoichiometry pipeline. For example, in the "Mass to Mole" tool:
- **Input:** Mass (g) and Formula.
- **Step 1:** Call `parser.calculate_molar_mass(formula)`.
- **Step 2:** Pass the resulting mass into `st.mass_to_moles(mass, molar_mass)`.
- **Step 3:** Format the final result into a professional f-string.

---

## 🧪 Summary Table: Parsing Examples

| Input | Tokenization Path | Calculation | Result |
| :--- | :--- | :--- | :--- |
| `H2O` | `H` (2), `O` (1) | $(1.008 \times 2) + 15.999$ | $18.015$ |
| `NaCl` | `Na` (1), `Cl` (1) | $22.990 + 35.45$ | $58.44$ |
| `Ca(NO3)2` | `Ca` (1) $\rightarrow$ `(` $\rightarrow$ `N` (1), `O` (3) $\rightarrow$ `)` $\rightarrow$ (2) | $40.078 + [14.007 + (15.999 \times 3)] \times 2$ | $164.087$ |
