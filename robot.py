import weapon
from dinosuar import Dinosaur

class Robot:
  def __init__(self, name):
      self.name = name
      self.health = 100
      self.weapon = weapon.Weapon('sword', 20)
      pass
    
  
  def attak(self, atk_power):
    opponent_health = Dinosaur.__init__[0 or 1 or 2]
    damage = atk_power
    if damage > 0:
      opponent_health -= damage
      print(f'You deal {damage}. Your opponenet is at {opponent_health} current HP')
    else:
      print(f'You dealt NO damage! Your opponenet is at {opponent_health} current HP')