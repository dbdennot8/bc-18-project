"""Function creates a new room when called and adds the name of the office
to the appropriate list below"""

class CreateRoom(object):
	def __init__(self, all_rooms=0, offices = [], living_spaces = [], room_types=["office", "living_spaces"]):
		"""	Initialize created offices to an empty list
	  	Initialize created living_spaces to an empty list
	  	Initialize count of all rooms to zero
	  	Specify available room types"""
		self.all_rooms = all_rooms
		self.offices = offices
		self.living_spaces = living_spaces
		self.room_types = room_types		

	def create_room(self, room_type, room_name):
		self.room_type = room_type
		self.room_name = room_name

		if room_type not in self.room_types:
			return "Room type is unavailable" 
		else:
			if room_type == "office":
				self.offices.append(room_name)
				#self.all_rooms += 1
			elif room_type == "living space":
				self.living_spaces.append(room_name)
				#self.all_rooms += 1
			return "The %s named %s has been created." % (room_type, room_name)

"""
demo = CreateRoom()
print()

print(demo.all_rooms)
print ()
print (demo.create_room("living space", "ya_kwanza"))
print()
print (demo.create_room("office", "ya_kwanza"))
print()	
# print (offices)	
print (demo.all_rooms)
print()

"""
