# bc-18-project
## Repo for week two Project
### Building a Command Line application using Docopts
*By: Dennis Mithamo (GitHub- @dbdennot8)*

#### What the Repo Contains, and What each of those does

**main.py**
- This is the docopt file that governs the application's command line
usage. It is the function that is called when the application is run, 
and parses the user's input as arguments to the application, giving applicable output.
	
**dojo.py**
- Contains all the functionality used by this application. The three methods
that task_0 executes i.e.,
- create_room, 
- add_person and assign_room are contained here.
	
**test_cases.py**
- Herein are defined the various test cases that were written to govern the 
development of the methodology.
	
**person.py**
- This is the class that defines the parameters used to construct the subclasses:
- *fellow.py* -- for instantiating a person of type *fellow*,
- *staff.py*  -- for instantiating a person of type *staff*

**room.py**
- This is the class that defines the parameters used to construct the subclasses:
- *office.py* -- to intantiate a room of type *office*
- *living_space.py* -- to instantiate a room of type *living_space*
				
**init.py** 
- Initialization file that signals that the repo/directory contains python modules.
	
**Other files**
- *designs folder* -- Contains UML diagram showing relationship between classes
- *.gitignore file* -- Contains file types ignored by git while tracking my local directory
- *requirements.txt* -- A snapshot of the installations done during project development
		
#### A brief description of the methods
1. ***create_room***
		-This method uses the variables *room_type*(office, or living_space) and *room_name* 
			(a name chosen by the user) to create an ***instance of the class Room.***
		-The room is then appended to lists of offices/living_spaces as applicable. 

2. ***add_person***
		-This method takes variables *first_name, surname*, *person_type* (either *fellow* or *staff*)
			and creates an instance of the class person, appending them to the appropriate lists. It also 
			takes an **optional argument wants_accommodation** (choice between no, or yes) to determine whether 
			or not the person would like to be assigned **living_space**. This optional argument is default to "no",
			and remains no for **person_type staff**
2.1 ***assign_room** - A nested method within ***add_person*** that runs whenever add_person is 
			called, assigning a room (office and/or living_space) as applicable.
			
#### Constraints
- The application requires that a user input both first_name and surname to add a person.
- The application will only add a person if the person type is either fellow or staff
- The application will only create a room of type office or living space
- The application randomizes the room assignment, selecting a random room into which to affix a person.
- The application will only offer to assign living space to fellows. Staff cannot be assigned living space.
- The application's room assignment method caps maximum occupancy of rooms as below:
- *office* -- maximum six occupants
- *living space* -- maximum four occupants

*My Youtube channel with Demo of App running various scenarios*

[![Screencapture of Demo](http://img.youtube.com/vi/e2P5qsyqMCM/0.jpg)](http://www.youtube.com/watch?v=e2P5qsyqMCM)
			

##### PS: This is only version_0 of the system. An update with more functionality is in the works. Cheers.

**@dbdennot8**
			



