import Ru_Local as Ru
v = 38241
h = 16637000000
n = int(input(print(Ru.start)))
h1 = h + (n * 24 * v)  # In miles.
h2 = round(h1 * 1.60934, 2)  # In kilometers.
h3 = round(h2/149597871, 2)  # In astronomical units.
z = round((h2 * 1000 - 149597870700)/(299792458*3600), 2)  # Communication delay.

print(h1, Ru.units_measure1)
print(h2, Ru.units_measure2)
print(h3, Ru.units_measure3)
print(z, Ru.time)
