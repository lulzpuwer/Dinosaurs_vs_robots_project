import weapon


class Robot:
  def __init__(self, name):
      self.name = name
      self.health = 100
      self.weapon = weapon.Weapon()
    
  def attak(self, atk_power):
    pass