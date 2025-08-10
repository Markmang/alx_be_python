class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def create_child(name):
        return Person(name, 0)
    def __str__(self):
        return f"Person(name={self.name}, age={self.age})"

person1 = Person.create_child("Alice")
person2 = Person("Bob", 30)
print(person1)  # Output: Person(name=Alice, age=0)
print(person2)  # Output: Person(name=Bob, age=30)