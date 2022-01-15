Strategy Pattern
================

Definition
-----------
Strategy is a behavioral design pattern that lets you define a family of algorithms,
put each of them into a separate class, and make their objects interchangeable.

[Read More...](https://refactoring.guru/design-patterns/strategy)

Python Example
--------------
The example handles a processing support ticket system with different processing
types. Initially all the processing types were implemented inside a method
preventing the class to properly extended. With the strategy pattern an interface
is created to handle all processing types and if a new type is required in future
we only need to create a new class implementing the interface method without 
modifying the other classes.




