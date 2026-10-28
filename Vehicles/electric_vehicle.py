from vehicle import Vehicle
try:
    from typing import override
except ImportError:   # Python < 3.12
    def override(func):
        return func


class ElectricVehicle(Vehicle):
    def __init__(self, model, plate,
                 battery_kwh: float = 60.0, efficiency: float = 6.0,
                 paint: str = "white"):
        super().__init__(model, plate)
        self.battery_kwh = battery_kwh
        self.efficiency = efficiency   # km per kWh
        self.charge_pct = 50.0         # 0..100
        self.paint = paint

    @override
    def summary(self, verbose: bool = False, unit: str = "km"):
        rng = self.max_range()
        if unit == "mi":
            rng *= 0.621371
        return (super().summary(verbose) +
                f" | {self.charge_pct:.0f}% | {rng:.0f} {unit}")

    @override
    def drive(self, km: float, eco: bool = False):
        if km < 0:
            raise ValueError("Distance cannot be negative")
        energy = km / self.efficiency
        if eco:
            energy *= 0.85
        needed_pct = energy / self.battery_kwh * 100
        if needed_pct > self.charge_pct:
            raise ValueError("Not enough charge for this trip")
        self.charge_pct -= needed_pct
        return super().drive(km)

    def max_range(self):
        return self.battery_kwh * self.efficiency * self.charge_pct / 100

    def plug_in(self, hours: float, kw: float = 7.4):
        added_pct = kw * hours / self.battery_kwh * 100
        self.charge_pct = min(100.0, self.charge_pct + added_pct)
        return self.charge_pct

    @override
    def __str__(self):
        return ("Electric " + super().__str__() +
                f", {self.battery_kwh} kWh, {self.charge_pct:.0f}%")
