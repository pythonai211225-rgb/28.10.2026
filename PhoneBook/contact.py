from typing import override

class Contact:

    count: int = 0   # class-member. Contact.count

    def __init__(self, name, number):
        # instance member
        self._name = name      # protected
        self._number = number  # protected
        Contact.count += 1     # NOT self.count!!!!
        self._index = Contact.count
        self.color = 'yellow'  # public

    @property
    def name(self):
        return "** " + self._name + " **"

    @name.setter
    def name(self, value):
        value = value.strip()
        if value:
            self._name = value
        else:
            raise ValueError("Name cannot be empty")

    @property
    def number(self):
        return "[" + self._number + "]"

    @number.setter
    def number(self, value):
        value = value.strip()
        if value:
            self._number = value
        else:
            raise ValueError("Number cannot be empty")

    def describe(self):
        return f"{self._index} {self._name}: {self._number}"

    @classmethod
    def from_string(cls, txt):
        # Lee:+972 52 000 1111
        name, number = txt.strip().split(":")
        return cls(name, number)

    @classmethod
    def from_str(cls, txt):
        # Friendly alias for callers who expect from_str naming.
        return cls.from_string(txt)

    @override
    def __str__(self):
        return f"Contact {self._index}, {self._name}, {self._number}"

danny = Contact("Danny", "050-2372361")
print(danny.name)
danny.name = "Danny!"
danny.number = "050-2372361"
print(danny.describe())

lee = Contact.from_string("Lee: 050-2372361")
