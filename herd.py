from dinosuar import Dinosaur
from weapon import Weapon

class Herd:
  def __init__(self):
      self.dinosaurs = []
      pass

  def create_herd(self):
    create_herd = self.dinosaurs.append(Dinosaur(input('Name your dinosuar: ')))
    while len(self.dinosaurs) <= 2:
      self.dinosaurs = self.dinosaurs.append(create_herd)
      print(f'You have name a dinosuar! please name a total of 3 to complete the herd')
      return self.dinosaurs
    else:
      print(f'you have filled out your team {self.dinosaurs}')
    return  self.dinosaurs

  def generate_default_herd(self):
     self.dinosaurs =  [('Godzilla', 100, Weapon('laser eye', 20)), ('Mega Moth', 100, Weapon('sleep powered', 20)), ('Boar God of the Moutain', 100, Weapon('tusk attack', 20))]