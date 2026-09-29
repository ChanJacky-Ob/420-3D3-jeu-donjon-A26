from comportement import Comportement


class ComportementBerseker(Comportement):

    def agir(self, ennemi) -> str:
        if ennemi.hp < ennemi.hp_max * 0.5:
            ennemi.attaque*=2
        return "attaque_double"
    def __str__(self):
        return"ComportementBerseker"

    