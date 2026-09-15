import math

constellations = [
    ("Cassiopea", 1.0, 60),
    ("Ibejis (Geminis)", 7.0, 20),
    ("Sagitario", 19.0, -25),
    ("Tauro", 4.5, 15),
    ("Draco", 17.0, 60),
    ("Aries", 2.5, 20),
    ("Cancer", 8.5, 20),
    ("Leo", 10.5, 15),
    ("Virgo", 13.0, -5),
    ("Libra", 15.0, -15),
    ("Escorpio", 16.5, -30),
    ("Capricornio", 21.0, -20),
    ("Acuario", 22.5, -10),
    ("Piscis", 0.5, 10)
]

for name, ra, dec in constellations:
    # Azimuthal equidistant projection centered on North Celestial Pole
    # Radius based on Dec: 90 is center, -30 is edge (max 120)
    r = (90 - dec)
    r_norm = (r / 120.0) * 0.45 # max radius 0.45
    
    # Angle based on RA: 0h is right (0 rad), 6h is bottom (pi/2) etc
    angle = (ra / 24.0) * 2 * math.pi
    
    cx = r_norm * math.cos(angle)
    cy = r_norm * math.sin(angle)
    
    print(f"{name}: cx={cx:.3f}, cy={cy:.3f}")
