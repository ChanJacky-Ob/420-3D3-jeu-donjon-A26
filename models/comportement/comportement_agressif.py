from comportement import Comportement


class ComportementAgressif(Comportement):

    def agir(self, ennemi) -> str:
        return "attaque"
    def __str__(self):
        return"ComportementAgressif"