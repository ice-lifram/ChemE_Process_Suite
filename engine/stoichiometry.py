## stoichiometry calculations

def mass_to_moles(mass, molar_mass):
    return mass / molar_mass

def moles_to_mass(moles, molar_mass):
    return moles * molar_mass

def mole_ratio_conversion(moles, coefA, coefB):
    return moles * (coefB / coefA)

def mass_to_mass_calculations(massA, molarmassA, molarmassB, coefA, coefB):
    molA = mass_to_moles(massA, molarmassA)
    molB = mole_ratio_conversion(molA, coefA, coefB)
    return moles_to_mass(molB, molarmassB)
