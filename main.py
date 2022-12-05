# import numpy as np
# import pandas as pd


# Constants
MAX = 20


# Mass to moles
def mass2mole(mass, mole_mass):
    return mass / mole_mass


def mole2mass(mole_mass, mass):
    return mass * mole_mass


def molar_mass2mass(molar_mass, moles):
    return molar_mass * moles


def get_molar_mass(atomic_mass, moles):
    return atomic_mass * moles


def mass_predict(H2S_mass, CO2_mass):
    H2S_molar_mass = 34.0808
    CO2_molar_mass = 44.0098
    H2S_amount = mass2mole(H2S_mass, H2S_molar_mass)
    CO2_amount = mass2mole(CO2_mass, CO2_molar_mass)
    limiting_reagent = "CO2" if H2S_amount / 2 < CO2_amount else "H2S"
    product_amount = CO2_amount * 5 if limiting_reagent == "CO2" else H2S_amount * 2.5
    product_mass = mole2mass(product_amount, 460.63588)
    result = [
        H2S_mass,
        CO2_mass,
        product_mass,
        product_mass * 14.0268 / 460.63588,
        product_mass * 2.016 / 460.63588,
        product_mass * 256.52 / 460.63588,
        product_mass * 18.01528 / 460.63588,
        product_mass * 170.0578 / 460.63588,
    ]
    return result


# algorithm to determine ratio of input materials required
# 4CO₂ + 8H₂S → 1CH₂+ 5H₂+ 8S + 2H₂O + 1 glyceraldehyde-3-phosphate
