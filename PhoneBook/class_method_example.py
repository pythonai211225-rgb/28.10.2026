class Parent:
    @classmethod
    def identify(cls):
        # cls dynamically adapts to whoever called it
        print(f"This method is bound to: {cls}")

class Child(Parent):
    pass

Parent.identify()
Child.identify()
