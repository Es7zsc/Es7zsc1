import random

# Lag to variabler for spiller 1 og spiller 2
spiller1 = random.randint(1, 10)
spiller2 = random.randint(1, 10)

# Skriv ut resultatene
print(f"Spiller 1: {spiller1}")
print(f"Spiller 2: {spiller2}")

# Sjekk hvem som vinner
if spiller1 > spiller2:
    print("Spiller 1 vinner!")
elif spiller2 > spiller1:
    print("Spiller 2 vinner!")
else:
    print("Det ble uavgjort!")