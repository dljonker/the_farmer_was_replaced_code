import functions

change_hat(Hats.Brown_Hat)
r = get_world_size()
#functions.clean()
functions.origin()
for i in range(r):
	functions.new_harvest()
	move(East)
	
crops = ["sunflower", "grass", "grass", "grass", "grass", "sunflower", "grass", "grass", "carrot", "carrot", "sunflower", "carrot", "carrot", "carrot", "sunflower", "carrot"]




def main():
	functions.origin()
	count = 0
	for i in range(len(crops)):
		functions.planting(crops[count])
		count += 1
	functions.origin()
	for i in range(r):
		functions.new_harvest()
		move(East)
	
while True:
	main()