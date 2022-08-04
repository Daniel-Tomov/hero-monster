import random
import time
fighting = True

class Hero():  
  def __init__(self, weapon, health):
    self.weapon = weapon
    self.health = health
    self.potion = True
    
  def attack(self, attacked):
  	attacked.attacked(self.weapon)
    
  def attacked(self, weapon):
    self.health = self.health - weapon
    if self.health <= 5 and self.potion:
      self.heal()
  
  def heal(self):
    self.health = self.health + 5
    self.potion = False
    print("The Hero has healed")
    
class Monster():
  def __init__(self, strength, health):
    self.strength = strength
    self.health = health
  
  def attack(self, attacked):
    print("RRROOOOAAAAARRR")
    attacked.attacked(self.strength)
    
  def attacked(self, weapon):
    self.health = self.health - weapon
    
hero = Hero(3, 10)
monster = Monster(2, 15)

while fighting:
  rand = random.randint(0,1)
  print("\nAttacking")
  time.sleep(0.5)
  if rand == 0:
    hero.attack(monster)
    print(f'The Hero has attacked and the Monster has {monster.health} health remaining')
  elif rand == 1:
    monster.attack(hero)    
    print(f'The Monster has attacked and the Hero has {hero.health} health remaining')
  if hero.health <= 0: fighting = False
  elif monster.health <= 1: fighting = False
    
if hero.health <= 0: print("The Hero has died")
elif monster.health <= 0: print("The Monster has died")
elif monster.health == 1: print("The Monster ran away")
