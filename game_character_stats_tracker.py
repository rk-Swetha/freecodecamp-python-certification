# Build a Game Character Stats Tracker - Lab

class GameCharacter:
    def __init__(self, name):
        self._name = name
        self._health = 100
        self._mana = 50
        self._level = 1

    @property
    def name(self):
        return self._name

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, health_value):
        if health_value < 0:
            self._health = 0
        elif health_value > 100:
            self._health = 100
        else:
            self._health = health_value

    @property
    def mana(self):
        return self._mana

    @mana.setter
    def mana(self, mana_value):
        if mana_value < 0:
            self._mana = 0
        elif mana_value > 50:
            self._mana = 50
        else:
            self._mana = mana_value

    @property
    def level(self):
        return self._level

    def level_up(self):
        self._level += 1
        self.health = 100
        self.mana = 50
        print(f"{self.name} leveled up to {self.level}!")

    def __str__(self):
        return (
            f"Name: {self.name}\n"
            f"Level: {self.level}\n"
            f"Health: {self.health}\n"
            f"Mana: {self.mana}"
        )


hero = GameCharacter('Kratos')
print(hero)
print()

hero.health -= 30
hero.mana -= 10
print(hero)
print()

hero.level_up()
print(hero)
