import re
import engine.data.engine_mmass as mm

def calculate_molar_mass(formula):
    """
    Calculates the molar mass of a chemical formula.
    Supports:
    - Single elements (e.g., 'H', 'He')
    - Compounds with subscripts (e.g., 'H2O', 'H2SO4')
    - Nested parentheses (e.g., 'Ca(NO3)2', 'Fe2(SO4)3')
    """

    def parse_formula(formula, index):
        total_mass = 0.0

        while index < len(formula):
            char = formula[index]

            if char == '(':
                # Start of a group: solve recursively
                group_mass, next_index = parse_formula(formula, index + 1)
                index = next_index

                # Look for a multiplier after the closing parenthesis
                multiplier_match = re.match(r'^(\d+)', formula[index:])
                if multiplier_match:
                    multiplier = int(multiplier_match.group(1))
                    group_mass *= multiplier
                    index += len(multiplier_match.group(1))

                total_mass += group_mass

            elif char == ')':
                # End of a group: return current mass to the caller
                return total_mass, index + 1

            elif char.isupper():
                # Start of an element symbol
                # Match element name (Upper + optional Lower)
                element_match = re.match(r'^([A-Z][a-z]*)', formula[index:])
                if element_match:
                    element = element_match.group(1)
                    index += len(element)

                    # Look for a subscript (number) immediately following the element
                    subscript_match = re.match(r'^(\d+)', formula[index:])
                    multiplier = 1
                    if subscript_match:
                        multiplier = int(subscript_match.group(1))
                        index += len(subscript_match.group(1))

                    # Retrieve mass from the data dictionary
                    mass = mm.elements_molarmass.get(element)
                    if mass is None:
                        raise ValueError(f"Element '{element}' not found in Periodic Table.")

                    total_mass += mass * multiplier
                else:
                    index += 1
            else:
                if char.isdigit():
                    raise ValueError(f"Unexpected digit '{char}' at position {index}. Subscripts must follow elements or groups.")
                index += 1

        return total_mass, index

    try:
        final_mass, _ = parse_formula(formula, 0)
        return round(final_mass, 4)
    except Exception as e:
        raise ValueError(str(e))

# --- Simple Testing Block ---
if __name__ == "__main__":
    test_cases = {
        "H": 1.008,
        "H2O": 18.015,
        "H2SO4": 98.079,
        "NaCl": 58.44,
        "Ca(NO3)2": 164.087,
        "Fe2(SO4)3": 399.88,
        "Al2(SO4)3": 342.15
    }


## for testing

    print("Testing Molar Mass Parser...")
    for formula, expected in test_cases.items():
        try:
            result = calculate_molar_mass(formula)
            status = "✅" if abs(result - expected) < 0.1 else "❌"
            print(f"{status} {formula}: Expected ~{expected}, Got {result}")
        except Exception as e:
            print(f"❌ {formula}: Error - {e}")
