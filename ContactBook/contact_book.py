class Contact:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone


class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print(f"Added contact: {contact.name}")

    def remove_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                self.contacts.remove(contact)
                return True

        return False

    def find_contact(self, name):
        for contact in self.contacts:
            if name.lower() in contact.name.lower():
                return contact

        return None


# Basic test of the core contact-book functionality
contact_book = ContactBook()

amelia = Contact(
    "Amelia Turner",
    "amelia@example.com",
    "+675 7XX XXX XXX"
)

kofi = Contact(
    "Kofi Mensah",
    "kofi@example.com",
    "+675 7XX XXX XXX"
)

contact_book.add_contact(amelia)
contact_book.add_contact(kofi)

result = contact_book.find_contact("Kofi")

if result:
    print(
        f"Search result for 'Kofi': "
        f"{result.name} | {result.email} | {result.phone}"
    )