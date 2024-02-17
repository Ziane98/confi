from matplotlib import pyplot as plt
from data_loader import load

"""
TESTING 
"""

# Chargement des données
data, tag = load()
hsi_data = data[5]
label = tag[5]
print(f"image from  : {label}\n")

# Afficher quelques bandes HSI
plt.figure('20')
plt.imshow(hsi_data[20], cmap='gray')
plt.title('Bande HSI 20')

plt.figure('50')
plt.imshow(hsi_data[50], cmap='gray')
plt.title('Bande HSI 50')

plt.figure('100')
plt.imshow(hsi_data[100], cmap='gray')
plt.title('Bande HSI 100')

# Affichage d'une empreinte spectral
plt.figure('plot')
plt.plot(hsi_data[:,150, 150])

plt.tight_layout()
plt.show()
