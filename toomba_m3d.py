toomba_m3d.py
import random
import datetime

print("===================================")
print("       🤖 TOOMBA M3D")
print("   Votre assistant intelligent")
print("===================================")

print("\nBonjour ! Je suis TOOMBA M3D.")
print("Pose-moi une question pour commencer.")
print("Tape 'quitter' pour arrêter.\n")


def repondre(message):

    message = message.lower().strip()

    # Salutations
    if any(mot in message for mot in ["bonjour", "salut", "bonsoir"]):
        return random.choice([
            "Bonjour ! Comment vas-tu ?",
            "Salut ! Bienvenue sur TOOMBA M3D.",
            "Bonsoir ! Que puis-je faire pour toi ?"
        ])

    # Identité du robot
    elif "ton nom" in message or "tu t'appelles" in message:
        return "Je m'appelle TOOMBA M3D, ton assistant virtuel."

    # Créateur
    elif "créateur" in message or "qui t'a créé" in message:
        return "J'ai été créé par Toomba King Officiel."

    # Fonctionnement
    elif "que peux-tu faire" in message:
        return "Je peux discuter avec toi, répondre à tes questions et t'aider."

    # Heure
    elif "heure" in message:
        heure = datetime.datetime.now().strftime("%H:%M")
        return f"Il est actuellement {heure}."

    # Date
    elif "date" in message:
        date = datetime.datetime.now().strftime("%d/%m/%Y")
        return f"Nous sommes le {date}."

    # Remerciements
    elif "merci" in message:
        return "Avec plaisir ! TOOMBA M3D est toujours là pour toi."

    # Humeur
    elif "comment vas-tu" in message:
        return "Je vais très bien ! Merci de me demander."

    # Au revoir
    elif "au revoir" in message:
        return "Au revoir ! À bientôt sur TOOMBA M3D."

    # Réponse inconnue
    else:
        return (
            "Je ne connais pas encore la réponse à cette question. "
            "Je suis TOOMBA M3D et je suis en cours d'amélioration !"
        )


# Boucle de conversation
while True:

    question = input("👤 Vous : ")

    if question.lower().strip() == "quitter":
        print("🤖 TOOMBA M3D : Merci d'avoir discuté avec moi !")
        break

    reponse = repondre(question)

    print("🤖 TOOMBA M3D :", reponse)