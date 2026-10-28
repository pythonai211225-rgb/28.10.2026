from PhoneBook.contact import Contact
from PhoneBook.business_contact import BusinessContact

def main() -> None:
    # Create a few regular contacts directly.
    contact_1 = Contact("Alice", "050-1111111")
    contact_2 = Contact("Bob", "050-2222222")

    # Create contacts from string factory constructors.
    contact_3 = Contact.from_string("Charlie:050-3333333")

    # ERROR
    # contact_5 = BusinessContact.from_string("Charlie:050-3333333")

    contact_4 = Contact.from_str("Dana:050-4444444")

    print("=== Contact examples ===")
    print(contact_1.describe())
    print(contact_2.describe())
    print(contact_3)
    print(contact_4)

    # Create business contacts and demonstrate business-specific behavior.
    consultant_1 = BusinessContact("Eve", "050-5555555", "Acme", 250)
    consultant_2 = BusinessContact("Frank", "050-6666666", "Globex", 320)

    print("\n=== Business contact examples ===")
    print(consultant_1.describe())
    print(consultant_2.describe())
    print(f"{consultant_1.name} cost for 3.5 hours: {consultant_1.cost(3.5)}")
    print(f"{consultant_2.name} cost for 2 hours: {consultant_2.cost(2)}")
    print(consultant_1)
    print(consultant_2)

if __name__ == "__main__":
    main()
