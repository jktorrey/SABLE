#creating directories

import os
path = "" #insert adventuretutorial later
try:
	os.mkdir(path)
except OSError:
	print ("Creation of the directory {0} failed".format(path))
else:
	print ("Successfully created the directory {0} ".format(path))
	

#creating global Item class
#TO-DO: create _init_.py file later, and module called items.py
class Item():
	"""The base class for all items"""
	def _init_(self, name, description, value):
		self.name = name
		self.description = description
		self.value = value
	
	def _str_(self):
		return "{0}\n=====\n{1}\nValue: {2}\n".format(self.name, self.description, self.value)

#Money class
class Money(Item):
	def _init_(self, description, amt):
		self.amt = amt
		super()._init_(name="Dolla Dolla Bills", description="Cash rules everything around me. You found ${0}.".format(str(self.amt)), value=self.amt)

class Money_10(Money):
	def _init_(self):
		super()._init_(name="$10", description="Yay, you found $10.", amt=10)

class Money_30(Money):
	def _init_(self):
		super()._init_(name="$30", description="OMG $30 was just lying on the floor? Score!", amt=30)
		
#Yarn parent class
class Yarn(Item):
	def _init_(self, name, description, value):
		self.value = value
		super()._init_(name, description, value)
	
	def _str_(self):
		return "{0}\n=====\n{1}\nvalue: {2}".format(self.name, self.description, self.value)

#Yarn sub classes
class Cotton(Yarn):
	def _init_(self):
		super()._init_(name="Verigated Cotton Yarn", description="200 yards of a sturdy, multi-color cotton yarn for dishcloths.", value=10)

class Wool(Yarn):
	def _init_(self):
		super()._init_(name="Merino Wool Yarn", description="400 yards of beautifully soft merino wool yarn.", value=25)
		
class Silk(Yarn):
	def _init_(self):
		super()._init_(name="Silk Yarn", description="150 yards of luxurious, 100% silk yarn.", value=35)

#Weapon parent class		
class Weapon(Item):
	def _init_(self, name, description, value, damage):
		self.damage = damage
		super()._init_(name, description, value)
	
	def _str_(self):
		return "{0}\n=====\n{1}\nValue: {2}\nDamage: {3}".format(self.name, self.description, self.value, self.damage)

#Weapons sub classes
class Str8_Needles(Weapon):
	def _init_(self):
		super()._init_(name="Straight Knitting Needles", description="A lovely pair of blue-green hardwood straight knitting needles.", value=0, damage=3)

class Circ_Needles(Weapon):
	def _init_(self):
		super()._init_(name="Circular Knitting Needles", description="A shiny pair of nickel-plated circular needles connected by a cable for knitting in the round.", value=0, damage=5)
		
class C_Hook(Weapon):
	def _init_(self):
		super()._init_(name="Faux Ivory Crochet Hook", description="A large white crochet hook made of imitation ivory.", value=3, damage=5)

class Scissors(Weapon):
	def _init_(self):
		super()._init_(name="Fabric Scissors", description="A pair of fabric scissors that degrade when used on paper. They are very sharp, run at your own risk.", value=10, damage=10)


#Enemies Module starts here
#TO-DO: create enemies.py module

class Enemy:
	def _init_(self, name, hp, damage):
		self.name = name
		self.hp = hp
		self.damage = damage
	
	def is_alive(self):
		return self.hp > 0

#Sub class enemies
class Cat(Enemy):
	def _init_(self):
		super()._init_(name="Mangey Cat", hp=10, damage=5)

class Sheep(Enemy):
	def _init_(self):
		super()._init_(name="Horned Sheep", hp=10, damage=10)

class Alpaca(Enemy):
	def _init_(self):
		super()._init_(name="Spitty Alpaca", hp=30, damage=15)


#Tile Module starts here
#TO-DO: create tiles.py

import items, enemies

class MapTile:
	def _init_(self, x, y):
		self.x = x
		self.y = y

def intro_text(self):
	raise NotImplementedError()

def modify_player(self, player):
	raise NotImplementedError()

#Sub class tiles
class StartingRoom(MapTile):
	def intro_text(self):
		return """You find yourself inside a deserted yarn shop. At least, you're pretty sure it's deserted. There's a sign on the door that says, \'Can only be opened when you've gathered enough yarn for a project.\' Seems like you'll need to find some money and some yarn. Shouldn't be too difficult, right?"""
	
	def modify_player(self, player):
		#room has no action on player
		pass

class LootRoom(MapTile):
	def _init_(self, x, y, item):
		self.item = item
		super()._init_(x, y)
	
	def add_loot(self, player):
		player.inventory.append(self.item)
	
	def modify_player(self, player):
		self.add_loot(player)

class EnemyRoom(MapTile):
	def _init_(self, x, y, enemy):
		self.enemy = enemy
		super()._init_(x, y)
	
	def modify_player(self, the_player):
		if self.enemy.is_alive():
			the_player.hp = the_player.hp - self.enemy.damage
			print("Enemy does {0} damage. You have {1} HP remaining.".format(self.enemy.damage, the_player.hp)


#Specific rooms listed here

class EmptyFloorPath(MapTile):
	def intro_text(self):
		return """Another unremarkable part of the shop. You must forge onwards."""
	
	def modify_player(self, player):
		#Room has no action on player
		pass
#Enemy rooms
class CatRoom(EnemyRoom):
	def _init_(self, x, y):
		super()._init_(x, y, enemies.Cat())
	
	def intro_text(self):
		if self.enemy.is_alive():
			return """A mangey cat jumps down from a shelf in front of you!"""
		else:
			return """The battered body of a dead cat rots on the ground."""

class SheepRoom(EnemyRoom):
	def _init_(self, x, y):
		super()._init_(x, y, enemies.Sheep())
	
	def intro_text(self):
		if self.enemy.is_alive():
			return """Something bumps your leg and bleats loudly. A sheep has appeared from the shadows!"""
		else:
			return """A sad sheep sits off to the side. It leaves you alone."""

class AlpacaRoom(EnemyRoom):
	def _init_(self, x, y):
		super()._init_(x, y, enemies.Alpaca())
	
	def intro_text(self):
		if self.enemy.is_alive():
			return """A wet blob of snot hits you in the face. An alpaca is towering over you."""
		else:
			return """The alpaca you defeated earlier eyes you suspiciously and backs away."""
#Loot Rooms
class FindScissorRoom(LootRoom):
	def _init_(self, x, y):
		super()._init_(x, y, items.Scissors())
	
	def intro_text(self):
		return """You notice something poking out of a basket It's a pair of scissors! You pick them up."""
		
class FindWoolRoom(LootRoom):
	def _init_(self, x, y):
		super()._init_(x, y, items.Wool())
	
	def intro_text(self):
		return """There's a cubby of wool yarn in front of you. It is soft and squishy. You cannot resist taking a skein."""
		
class FindCottonRoom(LootRoom):
	def _init_(self, x, y):
		super()._init_(x, y, items.Cotton())
	
	def intro_text(self):
		return """To the right, there is a pyramid of cotton yarn stacked on a table. You've always wanted to make a dishcloth so you grab some."""