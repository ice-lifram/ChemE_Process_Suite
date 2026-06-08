# Material Balance engine

def dof_calculate(num_unknown, num_equations):
    dof = num_unknown - num_equations
    if dof == 0:
        return "Solvable"
    elif dof > 0:
        return "Underspecified"
    else:
        return "Oversaturated system"

def mass_balance(inp, out): # list of input and output
    total_in = sum(inp)
    total_out = sum(out)
    return total_in - total_out

def mixture_calc(flow1, con1, flow2, con2): # for mixing two streams
    component_mass = (flow1 * con1) + (flow2 * con2) # Calculate mass of solute
    total_flow = flow1 + flow2 # Calculate total flow of mixture
    return component_mass / total_flow # calculate final concentration


