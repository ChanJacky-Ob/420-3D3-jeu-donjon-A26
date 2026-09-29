
from models.ennemi import Ennemi
from models.comportements.ComportementBerseker import ComportementBerseker
from models.comportements.comportement_agressif import ComportementAgressif
from models.comportements.comportement_defensif import ComportementDefensif
from models.comportements.comportement_aleatoire import ComportementAleatoire
from models.comportements.comportement_furtif import ComportementFurtif
from models.comportements.boss import ComportementBoss
from models.actions.action_defense import ActionDefense
class Jeu:
    def __init__(self):
        self.heros_hp = 200
        self.heros_hp_max = 200
        self.heros_attaque = 30
        

        self.ennemis = [#falcutatif si ordre est respecter
            Ennemi(nom="Goblin", hp=50, attaque=10, comportement=ComportementBerseker()),
            Ennemi("Dragon", 100, 20,ComportementDefensif()),
            Ennemi("Voleur", 30, 15,ComportementFurtif() ),
            Ennemi("Spectre", 40, 10,ComportementAleatoire() ),
            Ennemi("Demon", 90, 30,ComportementBoss() ),
        ]

    def ennemis_vivants(self):
        return [e for e in self.ennemis if e.est_vivant()]

    def demarrer(self):
        print("\n===========================================")
        print("        LE DONJON DES ALGORITHMES")
        print("===========================================\n")

        tour = 1

        while self.heros_hp > 0 and self.ennemis_vivants():
            # Afficher l'état
            print(f"Tour {tour} — Héros (HP: {self.heros_hp}/{self.heros_hp_max})")
            print("\nEnnemis :")
            vivants = self.ennemis_vivants()
            for i, ennemi in enumerate(vivants, 1):
                print(f"  [{i}] {ennemi.nom} (HP: {ennemi.hp}/{ennemi.hp_max}) — {ennemi.get_comportement()}")
            print()

            # Demander l'action du héros
            while True:
                action = input("Votre action ? (a)ttaquer / (d)éfendre : ").strip().lower()
                if action in ["a", "d"]:
                    break
                print("Choix invalide.")
            action_heros = "attaque" if action == "a" else "defend"

            # Demander la cible si attaque
            cible = None
            if action_heros == "attaque":
                if len(vivants) == 1:
                    cible = vivants[0]
                else:
                    while True:
                        try:
                            choix = int(input(f"Quel ennemi ? (1-{len(vivants)}) : "))
                            if 1 <= choix <= len(vivants):
                                cible = vivants[choix - 1]
                                break
                        except ValueError:
                            pass
                        print("Choix invalide.")

            # Chaque ennemi décide de son action
            actions_ennemis = {e: e.agir() for e in vivants}

            print("--- Résultats ---")

            # Résoudre l'attaque du héros
            if action_heros == "attaque" and cible:
                
                if type(actions_ennemis.get(cible)) == ActionDefense: ###to work
                    degats = self.heros_attaque // 2
                    print(f"Vous attaquez {cible.nom} — il se défend ! Seulement {degats} dégâts infligés.")
                else:
                    degats = self.heros_attaque
                    print(f"Vous attaquez {cible.nom} pour {degats} dégâts !")
                cible.recevoir_degats(degats)

            # Résoudre les actions des ennemis
            for ennemi, action_ennemi in actions_ennemis.items():
                if not ennemi.est_vivant():
                    continue
                
                self.heros_hp, message = action_ennemi.appliquer(
                ennemi,
                self.heros_hp,
                action_heros
                )
                print(message)
                

            # Adaptation des comportements
            for ennemi in self.ennemis_vivants():
                if ennemi.hp < ennemi.hp_max * 0.3  :
                    ennemi.set_comportement(ComportementDefensif())
                    print(f"  ⚡ {ennemi.nom} change de tactique — il devient Défensif !")
                

            print()
            tour += 1
        if not cible.est_vivant():
            print(f"💀 {cible.nom} est vaincu !")    

        if self.heros_hp > 0 or cible.nom == "Demon" :
            print("\n===========================================")
            print("  🏆 VICTOIRE ! Tous les ennemis sont vaincus !")
            print("===========================================\n")
        else:
            print("\n===========================================")
            print("  💀 DÉFAITE ! Le héros est tombé...")
            print("===========================================\n")
