try:
    from typing import override
except ImportError:   # Python < 3.12
    def override(func):
        return func


class Vehicle:

    total_built: int = 0   # class-member. Vehicle.total_built

    def __init__(self, model, plate):
        # instance members
        self._model = model    # protected
        self._plate = plate    # protected
        Vehicle.total_built += 1   # NOT self.total_built!!!!
        self._serial = Vehicle.total_built
        self.paint = "grey"    # public
        self.odometer = 0.0    # public

    @property
    def model(self):
        return "<" + self._model + ">"

    @model.setter
    def model(self, value):
        value = value.strip()
        if value:
            self._model = value
        else:
            raise ValueError("Model cannot be empty")

    @property
    def plate(self):
        return "(" + self._plate + ")"

    @plate.setter
    def plate(self, value):
        value = value.strip()
        if value:
            self._plate = value
        else:
            raise ValueError("Plate cannot be empty")

    def summary(self, verbose: bool = False):
        text = f"{self._serial} {self._model} {self._plate}"
        if verbose:
            text += f" | {self.paint} | {self.odometer} km"
        return text

    def drive(self, km: float):
        if km < 0:
            raise ValueError("Distance cannot be negative")
        self.odometer += km
        return self.odometer

    def repaint(self, new_paint: str):
        self.paint = new_paint

    @classmethod
    def parse(cls, line: str, sep: str = ";"):
        # Corolla;12-345-67
        model, plate = line.strip().split(sep)
        return cls(model.strip(), plate.strip())

    @override
    def __str__(self):
        return f"Vehicle {self._serial}, {self._model}, {self._plate}"
