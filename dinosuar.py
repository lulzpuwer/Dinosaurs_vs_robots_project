import random
from weapon import Weapon

class Dinosaur:
  def __init__(self, name):
    self.name = name
    self.atk_power = Weapon(input(' Pick your attack!: '), random.randrange(20, 35))
    self.health = 100
    pass

  def attack(self):
    if self.atk_power > 0:
      print(f'You deal {self.atk_power}. ')
    else:
      print(f'You dealt NO damage! ')
    return self.atk_power


  def damage_recieved(self, damage):
    self.health -= damage
    print(f'{self.name} has recieved this amount of damage {damage}!')

