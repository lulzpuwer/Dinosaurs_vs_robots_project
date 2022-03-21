from fleet import Fleet

class Dinosaur:
  def __init__(self, name, atk_power):
    self.name = name
    self.atk_power = atk_power
    self.health = 100
    pass

  def attak(self, atk_power):
    opponent_health = Fleet.__init__[0 or 1 or 2]
    damage = atk_power
    if damage > 0:
      opponent_health -= damage
      print(f'You deal {damage}. Your opponenet is at {opponent_health} current HP')
    else:
      print(f'You dealt NO damage! Your opponenet is at {opponent_health} current HP')
