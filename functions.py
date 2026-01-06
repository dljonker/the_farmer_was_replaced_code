def clean():
	x = get_pos_x()
	y = get_pos_y()
	r = get_world_size()

	if x != 0:
		move_x = r - x
		for i in range(move_x):
			move(East)
	if y != 0:
		move_y = r - y
		for i in range(move_y):
			move(North)
	for i in range(r):
		for i in range(r):
			harvest()
			if get_ground_type() == Grounds.Soil:
				till()
			move(North)
		move(East)

def origin():
	x = get_pos_x()
	y = get_pos_y()
	r = get_world_size()

	if x != 0:
		move_x = r - x
		for i in range(move_x):
			move(East)
	if y != 0:
		move_y = r - y
		for i in range(move_y):
			move(North)

def new_harvest():
	r = get_world_size()
	for i in range(r):
		if get_entity_type() == Entities.Dead_Pumpkin:
			harvest()
		else:
			if can_harvest():
				harvest()
		move(North)
			
def planting(plants):
	r = get_world_size()
	half = r/2
	if plants == "wood":
		for i in range(half): 
			if get_entity_type() == Entities.Grass and can_harvest():
				harvest()
			plant(Entities.Tree)
			move(North)
			plant(Entities.Bush)
			move(North)
		move(East)
	elif plants == "sunflower":
		for i in range(half): 
			if get_entity_type() == Entities.Grass and can_harvest():
				harvest()
			plant(Entities.Tree)
			move(North)
			if get_ground_type() != Grounds.Soil:
				till()
			if get_water() < 0.5:
				use_item(Items.Water)
			plant(Entities.Sunflower)
			move(North)
		move(East)
	elif plants == "carrot":
		for i in range(r):
			if get_ground_type() != Grounds.Soil:
				till()
			if get_water() < 0.5:
				use_item(Items.Water)
			plant(Entities.Carrot)
			move(North)
		move(East)
	elif plants == "pumpkin":
		for i in range(r):
			if get_ground_type() != Grounds.Soil:
				till()
			if get_water() < 0.5:
				use_item(Items.Water)
			plant(Entities.Pumpkin)
			move(North)
		check()
		move(East)
	elif plants == "grass":
		for i in range(r):
			if get_entity_type() == Entities.Grass and can_harvest():
					harvest()
			if get_ground_type() == Grounds.Soil:
					till()
			move(North)
		move(East)

def check():
	r = get_world_size()
	for i in range(4):
		check = False
		while check == False:
			for i in range(r):
				if get_entity_type() == Entities.Dead_Pumpkin:
					harvest()
					if get_water() < 0.5:
						use_item(Items.Water)
					plant(Entities.Pumpkin)
				else:
					move(North)
				check = True
		y = get_pos_y()
		if y != 0:
			move_y = r - y
			for i in range(move_y):
				move(North)
				
def waterrrr():
	r = get_world_size()
	for i in range(r):
		for i in range(r):
			use_item(Items.Water)
			move(North)
		move(East)