# Programme pour afficher "Bonjour le Monde"
print("Bonjour le Monde")
# Programme pour calculer l'âge
# Demander l'année de naissance de l'utilisateur
annee_naissance = int(input("Entrez votre année de naissance : "))

# Calculer l'année actuelle
from datetime import datetime
annee_actuelle = datetime.now().year

# Calculer l'âge
age = annee_actuelle - annee_naissance

# Afficher l'âge
print(f"Vous avez {age} ans.")
# Programme pour vérifier si un nombre est pair ou impair

# Demander à l'utilisateur de saisir un nombre
nombre = int(input("Entrez un nombre : "))

# Vérifier si le nombre est pair ou impair
if nombre % 2 == 0:  # Utilisation de l'opérateur modulo
    print("Le nombre est pair.")
else:
    print("Le nombre est impair.")
    # Programme pour calculer la somme des nombres de 1 à n

# Demander à l'utilisateur de saisir un nombre
n = int(input("Entrez un nombre entier positif : "))

# Initialiser la variable pour la somme
somme = 0

# Utiliser une boucle pour calculer la somme des nombres de 1 à n
for i in range(1, n + 1):  # La boucle commence à 1 et va jusqu'à n inclus
    somme += i  # Ajouter i à la somme

# Afficher le résultat
print(f"La somme des nombres de 1 à {n} est : {somme}")
# Programme pour afficher les tables de multiplication de 1 à 10

# Boucle pour les nombres de 1 à 10
for i in range(1, 11):  # Première boucle pour les lignes
    print(f"Table de {i} :")  # Titre de chaque table
    for j in range(1, 11):  # Deuxième boucle pour les colonnes
        resultat = i * j  # Calcul de la multiplication
        print(f"{i} x {j} = {resultat}")  # Affichage du résultat
    print()  # Ligne vide pour séparer les tables
    # Programme pour trouver le plus grand nombre parmi 5 nombres

# Initialiser une liste pour stocker les nombres
nombres = []

# Demander à l'utilisateur de saisir cinq nombres
print("Veuillez entrer 5 nombres :")
for i in range(5):
    nombre = float(input(f"Nombre {i + 1} : "))  # Convertir en float pour accepter les décimaux
    nombres.append(nombre)  # Ajouter le nombre à la liste

# Trouver le plus grand nombre
plus_grand = max(nombres)

# Afficher le plus grand nombre
print(f"Le plus grand nombre parmi {nombres} est : {plus_grand}")
# Programme pour compter les voyelles dans une phrase

# Demander à l'utilisateur de saisir une phrase
phrase = input("Entrez une phrase : ")

# Définir les voyelles
voyelles = "aeiouAEIOU"

# Initialiser le compteur de voyelles
compteur = 0

# Parcourir chaque caractère de la phrase
for caractere in phrase:
    if caractere in voyelles:  # Vérifier si le caractère est une voyelle
        compteur += 1  # Incrémenter le compteur

# Afficher le résultat
print(f"Le nombre de voyelles dans la phrase est : {compteur}")
# Programme pour inverser une chaîne

# Demander à l'utilisateur de saisir une chaîne
chaine = input("Entrez une chaîne de caractères : ")

# Inverser la chaîne en utilisant le slicing
chaine_inversee = chaine[::-1]

# Afficher la chaîne inversée
print(f"La chaîne inversée est : {chaine_inversee}")
# Programme pour vérifier si un mot est un palindrome

# Demander à l'utilisateur de saisir un mot
mot = input("Entrez un mot : ")

# Supprimer les espaces et convertir en minuscules pour uniformiser
mot = mot.replace(" ", "").lower()

# Vérifier si le mot est égal à son inverse
if mot == mot[::-1]:  # Comparaison avec la chaîne inversée
    print(f"Le mot '{mot}' est un palindrome.")
else:
    print(f"Le mot '{mot}' n'est pas un palindrome.")
    # Définir une fonction récursive pour calculer la factorielle
def factorielle(n):
    if n == 0 or n == 1:  # Condition de base : la factorielle de 0 ou 1 est 1
        return 1
    else:
        return n * factorielle(n - 1)  # Appel récursif

# Demander à l'utilisateur de saisir un nombre entier
n = int(input("Entrez un nombre entier positif : "))

# Vérifier si le nombre est valide
if n < 0:
    print("La factorielle n'est pas définie pour les nombres négatifs.")
else:
    resultat = factorielle(n)
    print(f"La factorielle de {n} est : {resultat}")
