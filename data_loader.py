from PIL import Image
import os
import rasterio


def load():
    """_summary_

    Returns:
        data: _description_
        tag: _description_
    """

    DOSSIER = "ICONES-HSI/"
    LIST_FOLDER = ["Agriculture/",
                   "Cloud/",
                   "Dense_urban/",
                   "Desert/",
                   "Forest/",
                   "Mountain/",
                   "Ocean/",
                   "Snow/",
                   "Wetland/"]
    tag = []
    data = []
    # Parcourir les fichiers dans le dossier
    for folder in LIST_FOLDER:
        for fichier in os.listdir(DOSSIER+folder):
            # Vérifier si le fichier se termine par .img
            if fichier.endswith(".img"):
                # Ajouter le chemin complet du fichier à la liste
                chemin_fichier = os.path.join(DOSSIER+folder, fichier)
                tag.append(folder[0:-1])
                with rasterio.open(chemin_fichier) as src_hsi:
                    hsi_data = src_hsi.read()
                data.append(hsi_data)

    return data, tag
