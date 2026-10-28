from contact import Contact
from typing import override

class BusinessContact(Contact):
    def __init__(self, name, number,
                 company, rate):
        super().__init__(name, number)
        self.company = company
        self.rate = rate

    @override
    def describe(self):
        return "Business " + super().describe() + \
            f" @ {self.company} {self.rate}"

    def cost(self, hours: float):
        return self.rate * hours

    @override
    def __str__(self):
        #  return f"Contact {self._index}, {self._name}, {self._number}"
        return "Business " + super().__str__() + f" @ {self.company} {self.rate}"







