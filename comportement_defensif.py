from models.comportement import Comportement


class ComportementDefensif(Comportement):

    def agir(self, ennemi) -> str:
        if ennemi.hp < ennemi.hp_max * 0.5:
            return "defend"
        return "attaque"

    def __str__(self):
        return"ComportementDefensif"