#créer ube variable chaine
chaine = "Il fait beau aujourd'hui. Je veux en profiter. "
print(chaine)
#remplacer les points par point d'exclamation
chaine = chaine.replace('.', '!')
print(chaine)  # Résultat : "Il fait beau aujourd'hui ! Je veux en profiter ! "
#mettre toute la chaine en minscule
chaine_minuscule = chaine.lower()
print(chaine_minuscule)  # Résultat : "il fait beau aujourd'hui ! je veux en profiter ! "
#en majescul
chaine_majuscule = chaine.upper()
print(chaine_majuscule)  # Résultat : "IL FAIT BEAU AUJOURD'HUI ! JE VEUX EN PROFITER ! "
#trouver l'indice de caractére b
indice_b = chaine.find('b')
print(indice_b)  # Résultat : 8
def premierMot(chaine):
    # Supprimer les espaces en début et fin de chaîne
    chaine = chaine.strip()
    # Diviser la chaîne en mots en utilisant les espaces comme séparateurs
    mots = chaine.split()
    # Retourner le premier mot s'il y en a, sinon retourner une chaîne vide
    return mots[0] if mots else ""

# Exemple d'utilisation
chaine = "samedi soir, je vais au cinéma"
print(premierMot(chaine))  # Résultat : "samedi"
def majuscule_mot(chaine):
    # Utiliser la méthode title() qui met en majuscule la première lettre de chaque mot
    return chaine.title()

# Exemple d'utilisation
chaine = "je mange du fromage"
print(majuscule_mot(chaine))  # Résultat : "Je Mange Du Fromage"
def inverser_phrase(phrase):
    # Diviser la phrase en mots
    mots = phrase.split()
    # Inverser l'ordre des mots
    mots_inverses = mots[::-1]
    # Rejoindre les mots inversés en une nouvelle phrase
    phrase_inversee = " ".join(mots_inverses)
    return phrase_inversee

# Exemple d'utilisation
phrase = "J’en suis tout retourné"
print(inverser_phrase(phrase))  # Résultat : "retourné tout suis J’en"
def image(mot):
    """
    Génère le terme suivant de la suite "look-and-say" à partir du terme donné.
    """
    resultat = ""
    i = 0

    while i < len(mot):
        # Compter le nombre de répétitions consécutives du chiffre courant
        count = 1
        while i + 1 < len(mot) and mot[i] == mot[i + 1]:
            count += 1
            i += 1

        # Ajouter le nombre et le chiffre au résultat
        resultat += str(count) + mot[i]
        i += 1

    return resultat


def afficher_termes_conway(n):
    """
    Affiche les n premiers termes de la suite de Conway.
    """
    terme = "1"  # Premier terme de la suite
    print(terme)

    for _ in range(n - 1):
        terme = image(terme)
        print(terme)


# Afficher les 20 premiers termes
afficher_termes_conway(20)
