 `Subject:` Object-Oriented Programming (2)
  `Date:` 17 Aug 22 `No.` 08

### Session content:

- **OOP Basic Concepts** (Inheritance, Polymorphism, Composition).


### Notes:

- #### **OOP Basic Concepts:**

    1. Abstraction

    2. Encapsulation

    3. **Inheritance**

       - The new class inherits all **public** (attributes / functions) only.

       - Any function in `Class` can access anything (either private or public), **So I can inherit private attributes through inheriting the public function that accesses those private attributes in the main `class`.**

       - If you make a constructor in a subclass it **eliminates** the super-class constructor.

       - To invoke the super constructor in Python:`super().__init__()`

         **Example:**

         ```python
         class A(object):
             def __init__(self):
                 print("world")
         
         class B(A):
             def __init__(self):
                 print("hello")
                 super().__init__()
             
         B()  
         ```
         **output:**
         
         ```
          hello
          world
         ```
         
       - **Inheritance Types:**

         - Single inheritance.
         - Multiple inheritance.

       - **Inheritance** in:

         - Java --> Can inherit from **only 1 Class**.
         - C++ --> Have Multiple inheritance.
         - Python --> Have Multiple inheritance.
       - **Multiple inheritance problems:**

         - Common attributes/functions.

         

    4. **Polymorphism**

       - The word polymorphism means having many forms. **In programming, polymorphism means the same function name but different functionality.**
       - In the case of making 2 functions having the same name, the first function is **canceled**, although if there are different parameters:

         - In python, we can **override** a function only (edit/pass), There is no **overloading**.
         -  In C++, we can make it works, by changing parameters or data types, because C++ is typed language.

       

    5. **Composition**

       - Make OOP more flexible.
       
       - Consider we have the following problem:
       
       ```python
         class Bird --> fly
         |
         class Chicken --> no fly
       ```
       
         We can pass function fly in `Chicken` class, **But the `flying function` affects other functions**.
         So, we'll divide `class Bird`  into two Classes
       
         ```python
         class flying bird
         class nonflying bird
         ```
       
         **But there are swimming birds, also `swim function` affects other functions**. So, we'll divide **class** `flying bird` into two Classes,  and divide **class** `non-flying bird` into two Classes.
       
         So, we'll have **4** Classes now:
       
         ```python
         class Flyingbird_Swimmingbird
         class Flyingbird_nonSwimmingbird
         class NonFlyingbird_Swimmingbird
         class NonFlyingbird_nonSwimmingbird
         ```
       
       and so on!, But **Composition** fixes this problem.
       
       By using this code:
       
       ```python
       class composition:
       
           def __init__(self):
               self.__att = dict()
               self.__methods = dict()
       
           def addatt(self, attname, attvalue):
               self.__att[attname] = attvalue
       
           def removeatt(self, attname):
               del self.__att[attname]
       
           def printatt(self, attname):
               print(self.__att[attname])
       
           def printallatt(self):
               for i in self.__att:
                   print(i)
       
           def addmethod(self, methname, method):
               self.__methods[methname] = method
       
           def removemethod(self, methodname):
               del self.__methods[methodname]
       
           def callmethod(self, methname):
               self.__methods[methname]()
       
           def printallmethods(self):
               for i in self.__methods:
                   print(i)
       ```
       
       We can **Add**, **Remove**, **Call**, **Print** attributes and methods.
       
       - To add new functions:
         1. Define the function.
         2. Add it by `addmethod()` function.
       - All Attributes, Methods are into the **object** only, But **the Class itself is empty**.
       
        

- ### **Tips:**
    - `__` also works for **functions** not only attributes.
    
      


### Code:

- [Notebook](https://github.com/AhmedUZaki/INSTANT-AI/blob/main/Track%201_%20Python%20for%20Data%20science/Session%2008/Session%208%20Notebook.ipynb)

### Tasks:

1. Why and how to use Access Modifiers **[protected]** in python. 
2. How do you access a private member from a super-class in a sub class?

### Solution:

- [Notebook](https://github.com/AhmedUZaki/INSTANT-AI/blob/main/Track%201_%20Python%20for%20Data%20science/Session%2008/Session%208%20Tasks.ipynb)




