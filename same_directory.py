import hashlib
import os
import sys

# Récupération des deux répertoires passés en paramétre
first_directory = sys.argv[1]
second_directory = sys.argv[2]

# Récupération de l'ensemble des fichiers de chaque répertoire
first_list_files = os.listdir(first_directory)
second_list_files = os.listdir(second_directory)

# Calcul du checksum de l'ensemble des fichiers
first_checksums = [
    hashlib.sha1(open(first_directory + '/' + file, 'rb').read()).hexdigest() for file in os.listdir(first_directory)
]
second_checksums = [
    hashlib.sha1(open(second_directory + '/' + file, 'rb').read()).hexdigest() for file in os.listdir(second_directory)
]

# Tri des listes de checksum
first_checksums.sort()
second_checksums.sort()

# Comparaison des deux listes
if first_checksums == second_checksums:
    print("Le contenu des répertoires {0} et {1} est identique".format(first_directory, second_directory))
else:
    print("Le contenu des répertoires n'est pas identique.")
