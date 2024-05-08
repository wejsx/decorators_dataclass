from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int
    city: str

    def __eq__(self, value: 'Person') -> bool:
        return self.age == value.age

    def __hash__(self) -> int:
        return hash(self.age)


peson1 = Person('alisa', 19, 'moscow')
person2 =  Person('goose', 19, 'new york')

print(peson1 == person2) # true
check_hash = {peson1, person2} #print -> person1