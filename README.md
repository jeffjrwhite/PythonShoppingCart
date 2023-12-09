PythonShoppingCart is an example Object Oriented Python project

The project is a classic Shopping Cart application with the Python files divided into classes that encasulate 
the various business entities found in the problem domain.
The classes have Type helpers ("hints") and annotations to show the type of method parameters expected, 
these are tested for in the related unit tests.
Each class file provides "unittest" methods to exercise the Unit Tests of the class behaviour.
To run the unit tests for a class just run that class file in Python on the command line.
There is no application entry point, in the real world it is assumed the application will call these business processes as an API. 
The business processes are tested using the unit tests, these unit tests serve to document how to use the code API.
To run the unit tests for the full Shopping Cart application run the main class file ShoppingCart.py