import matplotlib.pyplot as plt
from functions import *

# Générer une liste de valeurs x
x_values = range(-10, 11)

# Utiliser les fonctions pour calculer les valeurs y
y_values_carre = calculate_values(carre, x_values)
y_values_cube = calculate_values(cube, x_values)

# Afficher les valeurs calculées sur un graphique
plt.figure(figsize=(12, 6))

# Tracer la courbe du carré
plt.subplot(1, 2, 1)
plt.plot(x_values, y_values_carre, 'ro-', label='y = x^2')
plt.title('Fonction Carré')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()

# Tracer la courbe du cube
plt.subplot(1, 2, 2)
plt.plot(x_values, y_values_cube, 'bs-', label='y = x^3')
plt.title('Fonction Cube')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()

# Afficher les graphiques
plt.tight_layout()
plt.show()
