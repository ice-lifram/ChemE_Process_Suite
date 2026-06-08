# Equilibrium Calculator (Scope: Eq Constant Expression)
import numpy as np

def equilibrium_calc(reactant, product, r_coef, p_coef):
    return (product ** p_coef) / (reactant ** r_coef)

def ice_table_solver(initial_reactants, k_value, reactant_coef, product_coef):
    
