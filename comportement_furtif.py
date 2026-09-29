from models.comportement import Comportement


class ComportementFurtif(Comportement):

    def __init__(self) -> None:
        self._tour = 0   # ← valeur initiale ?

    def agir(self, ennemi) -> str:
        self._tour += 1
        if self._tour % 2 == 0:
            return "defend"
        return "attaque"

    def __str__(self):
        return"ComportementFurtif"