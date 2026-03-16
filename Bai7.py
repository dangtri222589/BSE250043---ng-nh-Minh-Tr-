class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, info_str):
        name, age = info_str.split('-')
        return cls(name, int(age))
person_info = "nam-20"
person = Person.from_string(person_info)
print(f"Name: {person.name}, Age: {person.age}")