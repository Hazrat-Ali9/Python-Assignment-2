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


