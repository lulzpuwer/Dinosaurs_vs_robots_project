import random
import weapon
from herd import Herd

class Robot:
  def __init__(self, name):
      self.name = name
      self.health = 100
      self.weapon = weapon.Weapon(input('Name your weapon!: '), random.randrange(0, 35))
      pass
    
  
  def attak(self, atk_power):
    opponent_health = Herd
    damage = atk_power
    if damage > 0:
      opponent_health -= damage
      print(f'You deal {damage}. Your opponenet is at {opponent_health} current HP')
    else:
      print(f'You dealt NO damage! Your opponenet is at {opponent_health} current HP')