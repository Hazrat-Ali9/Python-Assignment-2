# 1

In Python, both class methods and static methods are different types of methods that can be defined within a class. They have distinct purposes and behaviors. Here are the differences between class methods and static methods, along with examples:

                                          1. Definition and Access:
Class Method: A class method is a method that is bound to the class and not the instance of the class. It is defined using the @classmethod decorator and takes the class itself (usually represented by the parameter cls) as the first argument.
class MyClass:
    @classmethod
    def class_method(cls, x):
        print("Class method called with", x)

MyClass.class_method(5)

Static Method: A static method is a method that is not bound to either the class or the instance. It is defined using the @staticmethod decorator and does not receive any automatic first parameter like self or cls.
class MyClass:
    @staticmethod
    def static_method(x):
        print("Static method called with", x)

MyClass.static_method(5)

                      2. Usage and Access to Class Members:

Class Method: Class methods have access to the class itself and can modify class-level variables or call other class methods.
class MyClass:
    class_var = 0

    @classmethod
    def increment_class_var(cls):
        cls.class_var += 1

MyClass.increment_class_var()
print(MyClass.class_var)  # Output: 1

Static Method: Static methods do not have access to the class or instance-specific variables. They can only access other static members (variables or methods) defined within the class.
class MyClass:
    static_var = 0

    @staticmethod
    def increment_static_var():
        MyClass.static_var += 1

MyClass.increment_static_var()
print(MyClass.static_var)  # Output: 1

                               3. Inheritance and Polymorphism:
Class Method: Class methods are inherited by subclasses and can be overridden. When a subclass calls a class method, the subclass itself is passed as the first argument (cls).
class ParentClass:
    @classmethod
    def my_method(cls):
        print("Parent class method")

class ChildClass(ParentClass):
    @classmethod
    def my_method(cls):
        print("Child class method")

ChildClass.my_method()  # Output: Child class method

Static Method: Static methods are also inherited by subclasses but cannot be overridden. When a subclass calls a static method, the class in which the method is defined is used, not the subclass.
class ParentClass:
    @staticmethod
    def my_method():
        print("Parent static method")

class ChildClass(ParentClass):
    pass

ChildClass.my_method()  # Output: Parent static method


            
# 2

Polymorphism is a concept in object-oriented programming that allows objects of different types to be treated as if they belong to a common superclass. In Python, polymorphism enables you to write code that can work with objects of different classes, as long as they share a common interface or superclass.

The primary goal of polymorphism is to provide a unified interface to different objects, allowing them to be used interchangeably. This enhances code reusability, flexibility, and maintainability.


                                          Example:

class Animal:
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Woof!"

class Cat(Animal):
    def sound(self):
        return "Meow!"

class Cow(Animal):
    def sound(self):
        return "Moo!"


dog = Dog()
cat = Cat()
cow = Cow()

print(dog.sound())
print(cat.sound())
print(cow.sound())


# 4
Multi-level inheritance can be defined as where a subclass inherits from the single subclass and then another subclass inherits from the first subclass. By this, the second subclass can access all the attributes and methods from both the first subclass and the superclass.

Let's understand with an example showing multi-level inheritance.

# Base Class
class GrandPa:
    def __init__(self):
        self.age = 100

# Derived CLass
class Parent(GrandPa):
    def __init__(self):
        self.name = "Geek"
        GrandPa.__init__(self)

# Derived Class
class GrandChild(Parent):
    def __init__(self):
        self.hobby = "Gaming"
        Parent.__init__(self)

    def display(self):
        print("Grandpa:", self.age)
        print("Parent:", self.name)
        print("Grandchild:", self.hobby)

obj = GrandChild()
obj.display()
In the above code, the subclass Parent inherits from the superclass GrandPa and now the first subclass Parent has access to the methods of the superclass GrandPa.

Then another subclass GrandChild inherited from the first subclass Parent and it has access to the methods that both the first subclass and superclass have.


Grandpa: 100
Parent: Geek
Grandchild: Gaming


# 5 

Inner functions, as the name suggests, are Python functions that are created inside other Python functions. 
Besides its own scope, the inner function has access to the objects available in the scope of the outer 
function. The inner function can be termed as a single Python object with its own data and variables. 
This inner function is protected by the outer function and cannot be called or referred from the global scope.
 This way the inner function acts as a hidden entity that works within the boundaries of outer function only 
 and global scope remains unaware of it. This process is also known as “encapsulation” in programming. Here 
 is an example of a nested function in Python.

 def visibile_outer_function(name):
    def  hidden_inner_function():
        print (name)
    hidden_inner_function()

visibile_outer_function("John")
hidden_inner_function()

The use cases of inner functions

The outer function takes one mandatory argument called “name”. The inner function has access to the scope of 
the outer function so it can make use of the name variable. A call to the inner function is then made in the 
outer function. Next, a call to both inner and outer functions is made in the global scope

Data Validation: When validating input data within a class method, you can define an inner function to 
perform the validation logic. This helps in separating the validation code from the main method, making 
it more readable and organized

Sorting or Filtering: When sorting or filtering a collection of objects within a method, you can define an 
inner function to specify the sorting or filtering criteria. This improves code readability and allows you 
to encapsulate the specific sorting or filtering logic.


Callback Functions: When working with callback functions, you can define an inner function to handle the 
callback logic. This keeps the main method clean and focused on its primary purpose. It also allows you 
to reuse the callback function within multiple methods if needed

Complex Calculations: When a method involves complex calculations or multiple steps, you can break down 
the process into smaller subtasks using inner functions. Each inner function can handle a specific 
calculation or step, improving code organization and readability.