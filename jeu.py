from ennemi_old import Ennemi

class Jeu:
    def __init__(self):
        self.heros_hp = 100
        self.heros_hp_max = 100
        self.heros_attaque = 20
        

        self.ennemis = [
            Ennemi("Goblin", 50, 10, "agressif"),
            Ennemi("Dragon", 100, 20, "defensif"),
            Ennemi("Voleur", 30, 15, "furtif"),
        ]

    def ennemis_vivants(self):
        return [e for e in self.ennemis if e.est_vivant()]

    def demarrer(self):
        print("\n===========================================")
        print("        LE DONJON DES ALGORITHMES")
        print("===========================================\n")

        tour = 1










    for ennemi, action_ennemi in actions_ennemis.items():
        if not ennemi.est_vivant():
            continue
        if action_ennemi == "attaque":
            if action_heros == "defend":
                degats = ennemi.attaque // 2
                print(f"  → {ennemi.nom} attaque — vous vous défendez ! Seulement {degats} dégâts reçus.")
            else:
                degats = ennemi.attaque
                print(f"  → {ennemi.nom} vous attaque pour {degats} dégâts !")
            self.heros_hp = max(0, self.heros_hp - degats)
        elif action_ennemi == "attaque_double":          # ← nouveau cas pour Berserker
            degats = ennemi.attaque * 2
            if action_heros == "defend":
                degats = degats // 2
                print(f"  → {ennemi.nom} attaque en BERSERK — vous vous défendez ! Seulement {degats} dégâts reçus.")
            else:
                print(f"  → {ennemi.nom} attaque en BERSERK pour {degats} dégâts !")
            self.heros_hp = max(0, self.heros_hp - degats)
        else:
            print(f"  → {ennemi.nom} se défend.")