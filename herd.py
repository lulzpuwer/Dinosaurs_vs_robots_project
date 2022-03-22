from dinosuar import Dinosaur

class Herd:
  def __init__(self):
      self.dinosaurs = []
      pass

  def create_herd(self):
    create_herd = self.dinosaurs.append(Dinosaur(input('Name your dinosuar: ')))
    while len(self.dinosaurs) <= 3:
      dinosaurs = self.dinosaurs.append(create_herd)
      print(f'You have name a dinosuar! please name a total of 3 to complete the herd')
      return dinosaurs
    else:
      print(f'you have filled out your team {self.dinosaurs}')
      
