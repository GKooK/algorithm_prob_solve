class Hp():
    def __init__(self, mount):
        self.hp = mount

    def reduce_hp(self, damage):
        self.hp = self.hp - damage

class Warriror():
    def __init__(self, name, hp, strength):
        self.name = name

    def reduce_hp(self, damage):
        self.hp = self.hp - damage