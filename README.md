AirBnb Command Interpreter:

	- This project is the first step towards building an AirBnB clone web page. This will be a shell-like interface that permits users to manage objects in the AirBnB project

	- Description of the command interpreter:

		- To start the interpreter run "./console.py"

		- The interpreter supports these commands:

		'create': Creates new object of specified class

		'show': Displays the details of a specific object

		'all': Shows all objects of a specified class or all objects if no class is provided

		'update': Updates the attributes of a specific object

		'destroy': Deletes a specific object

		'count': Counts the number of objects of a specified class

		get more info about commands with 'help'

		- Examples

		Create a new User object:
			(hbnb) create User
			
		Show the details of a User object with ID 123:
			(hbnb) show User 123

		Show all objects of the City class:
			(hbnb) all City

		Update the email attribute of a User object with ID 123:
			(hbnb) update User 123 email test@example.com

		Destroy a Place object with ID 456:
			(hbnb) destroy Place 456

		Count the number of objects of the Review class:
			(hbnb) count Review

	You can also use the command interpreter in non-interactive mode by passing commands through a file or by using pipes. 
		For example:
			$ echo "create User" | ./console.py

Authors: Can be found on AUTHORS page
