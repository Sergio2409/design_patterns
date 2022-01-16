 Interface Segregation Principle
===============================

Definition
-----------

Many client specific interfaces are better than one general purpose interface

The ISP is another one of the enabling technologies supporting component
substrates such as COM. Without it, components and classes would be much
less useful and portable.

The essence of the principle is quite simple. If you have a class that has
several clients, rather than loading the class with all the methods that
the clients need, create specific interfaces for each client and multiply
inherit them into the class. 


[Read More...]([Read More...](http://staff.cs.utu.fi/~jounsmed/doos_06/material/DesignPrinciplesAndPatterns.pdf))