# Boutique SPEED TECH

class Article:

    def __init__(self, titre, prix=100):
        self.titre = titre
        self.prix = prix

    def __str__(self) -> str:
        return self.titre


articles = [
    Article("Bananes", 300),
    Article("Mangues", 150),
    Article("Oranges"),
    Article("Avocats", 500),
    Article("Tomates", 50),
]

nom_du_client = input("Mettez votre nom:  ")

# Pour mettre de l'espace
print("\n\n")

for index, article in enumerate(articles, start=1):
    print(f"{index}. {article}")


premier_article = articles[0]

article_index = None


def get_valid_number(title, errorMessage, condition=None):
    valid_number = None
    while True:
        # Pour mettre de l'espace
        print("\n\n")
        print(title)
        index = input("")
        try:
            index = int(index)
            if condition:
                if condition(index):
                    valid_number = index
                    break
                else:
                    print(errorMessage)
        except Exception as e:
            print(errorMessage)
    return valid_number


article_index = get_valid_number("Choississez un article en mettant le chiffre correspondant entre 2-5: ",
                                 "\nVeuillez entrer un nombre valide !!!!!!",
                                 lambda x: x <= 5 and x >= 2,
                                 )

deuxieme_article = articles[article_index]

# Afficher le premier produit et son prix
# demander à l'utilisateur de mettre la quantité qu'il veut.

qte_1 = get_valid_number(f"Mettez la quantité de {premier_article} que vous voulez sachant que ça coûte {premier_article.prix} l'unité.",
    "\nVeuillez entrer un nombre valide !!!!!!",
    lambda x: x >= 1
)

qte_2 = get_valid_number(f"Mettez la quantité de {deuxieme_article} que vous voulez sachant que ça coûte {deuxieme_article.prix} l'unité.",
    "\nVeuillez entrer un nombre valide !!!!!!",
    lambda x: x >= 1
)

prix_total_1 = qte_1 * premier_article.prix

prix_total_2 = qte_2 * deuxieme_article.prix

if prix_total_1 + prix_total_2 > 10000:
    print(f"Le prix total est de {prix_total_1 + prix_total_2}, nous faisons une réduction de 20%.")
else:
    print(f"Le prix total est de {prix_total_1 + prix_total_2}.")

print("\n\n")

# afficher le nom du client
print("Nom du client: ", nom_du_client)

# afficher le premier produit commandé
print("Premier article: ", premier_article, f" Prix: {premier_article.prix}")

# afficher le deuxième produit commandé
print("Deuxième article: ", deuxieme_article, f" Prix: {deuxieme_article.prix}")

# afficher le total
if prix_total_1 + prix_total_2 > 10000:
    print("Total avant réduction: ", prix_total_1 + prix_total_2)

    print("Total avant réduction: ", (prix_total_1 + prix_total_2) * 0.8)
else:
    print("Total: ", prix_total_1 + prix_total_2)