import numpy as np


def lithium_radiation_power(TE):
    T = TE * 1000
    Z = np.log10(T)

    if 100 <= T < 300:
        Y = (6.29800501254456e-02 * Z**3 -
             2.28650242066325e+00 * Z**2 +
             8.90825634273927e+00 * Z**1 -
             3.95660535055000e+01 * Z**0)
    elif 300 <= T < 1000:
        Y = (-3.27990411489566e+00 * Z**3 +
             2.69605680489987e+01 * Z**2 -
             7.43284074746929e+01 * Z**1 +
             3.79697102308800e+01 * Z**0)
    elif 1000 <= T < 2000:
        Y = (-1.75754559836462e+01 * Z**3 +
             1.63262796356844e+02 * Z**2 -
             5.05337664675811e+02 * Z**1 +
             4.90274527597888e+02 * Z**0)
    elif 2000 <= T < 5000:
        Y = (1.92654668633744e+00 * Z**3 -
             1.85489974274020e+01 * Z**2 +
             5.81529546308372e+01 * Z**1 -
             9.01508074163460e+01 * Z**0)
    elif 5000 <= T < 10000:
        Y = (1.49264497067756e+01 * Z**3 -
             1.73847732754050e+02 * Z**2 +
             6.73491741451911e+02 * Z**1 -
             8.99360780192436e+02 * Z**0)
    else:
        Y = (-9.68479196520852e-01 * Z**3 +
             1.33337615299491e+01 * Z**2 -
             6.10275887439805e+01 * Z**1 +
             6.10843015892650e+01 * Z**0)
    
    PRTIN = (10**Y) * 1e+32  # account for Astra units 
    return PRTIN

# Esempio di utilizzo
Te = np.linspace(0.1,20,200)
TE_value = 0.5  # Esempio di temperatura dell'energia
for i in Te:
    radiation_power = lithium_radiation_power(i)

#print("Lithium radiation power:", radiation_power, "MW*m^3")
print(radiation_power)