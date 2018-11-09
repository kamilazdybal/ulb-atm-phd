'''
Reproducing figure 2.11 from S.R. Turns - Introduction to Combustion

For a reaction:

CO + 0.5 O2 -> (1 - alpha) CO2 + alpha CO + alpha/2 O2

where alpha is a dissociation fraction, we find the chemical equilibrium using two approaches:
    * Second-law of thermodynamics considerations
    * Gibbs function
'''
import numpy as np
import matplotlib.pyplot as plt

# Discretization of dissociation fraction:
alpha = np.arange(0,1,0.1)
Tad = []
T0 = 298 # temperature of reactants [K]

# Enthalpies of formation:
hCO = -110541 # kJ/kmol
hO2 = 0 # kJ/kmol
hCO2 = -393546 # kJ/kmol

# Reactants:
NrCO = 1
NrO2 = 0.5

# Specific heat at 298 K:
cpCO2ref = 62.718
cpCOref = 29.072
cpO2ref = 40.686

# Enthalphy of formation of reactants:
Hreact = NrCO * hCO + NrO2 * hO2

# Second-law of thermodynamics approach

# Specific heats (assuming linear function of T):
def cpCO2(T):
    return (63.919 - 32.387)/(5000-298) * (T - 298) + 32.387

def cpCO(T):
    return (38.033 - 29.072)/(5000-298) * (T - 298) + 29.072

def cpO2(T):
    return (42.627 - 28.473)/(5000-298) * (T - 298) + 28.473

# Computing the adiabatic flame temperature:
for item in alpha:
    if item == 0:
        T = T0
        Tprev = T
        print(T)
    else:
        T = (Hreact - (1 - item)*hCO2 - item*hCO - (item/2)*hO2) / ((1 - item)*cpCO2(Tprev) + item*cpCO(Tprev) + (item/2)*cpO2(Tprev)) + T0
        Tprev = T
        print(T)
        Tad.append(T)

Tad.append(T0)

print(Tad)
plt.plot((1-alpha), Tad)
plt.show()

# Gibbs function approach
