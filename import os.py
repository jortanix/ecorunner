import os
import pyglet

# Chemin absolu (modifie si nécessaire)
font_path = r'C:\Users\laura\Projets\exercice_licence_info\BebasNeue-Regular.ttf'

# Vérifie si le fichier existe
if os.path.exists(font_path):
    print(f"Chemin correct : {font_path}")
    pyglet.font.add_file(font_path)
else:
    print(f"Erreur : fichier introuvable à {font_path}")