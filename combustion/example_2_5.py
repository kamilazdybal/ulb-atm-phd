# Enthalpies of formation:
hCH4 = -74831
hCO2 = -393546
hH2O = -241845
hN2 = 0
hO2 = 0

# Reactants:
NrCH4 = 1
NrO2 = 2
NrN2 = 2*3.76

# Products:
NpCO2 = 1
NpH2O = 2
NpN2 = 7.52

Hreact = NrCH4 * hCH4 + NrO2 * hO2 + NrN2 * hN2
print(Hreact)

# Specific heats:
cpCO2 = 56.21
cpH2O = 43.87
cpN2 = 33.71

T0 = 298 # K

def Tad():

    Tad = (Hreact - NpCO2*hCO2 - NpH2O*hH2O - NpN2*hN2) / (NpCO2*cpCO2 + NpH2O*cpH2O + NpN2*cpN2) + T0

    return Tad

print(Tad())
