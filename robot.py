import random
import weapon


class Robot:
  def __init__(self, name):
      self.name = name
      self.health = 100
      self.weapon = weapon.Weapon(input('Name your weapon!: '), random.randrange(20, 35))
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
