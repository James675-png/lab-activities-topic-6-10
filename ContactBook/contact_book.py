class Contact:
    """Represent a person's contact information."""

    def __init__(self, name, email, phone):
        """Initialize a Contact object.

        Args:
            name (str): The contact's full name.
            email (str): The contact's email address.
            phone (str): The contact's phone number.
        """
        self.name = name
        self.email = email
        self.phone = phone

    def __str__(self):
        """Return the contact's basic details as a string.

        Returns:
            str: The contact's name, email, and phone number.
        """
        return f"{self.name} | {self.email} | {self.phone}"

    def masked_view(self):
        """Return contact details with the email address partially masked.

        Returns:
            str: The contact's name, masked email, and phone number.
        """
        local_part, domain = self.email.split("@")

        if len(local_part) <= 2:
            masked_email = self.email
        else:
            masked_middle = "*" * (len(local_part) - 2)
            masked_email = (
                local_part[0]
                + masked_middle
                + local_part[-1]
                + "@"
                + domain
            )

        return f"{self.name} | {masked_email} | {self.phone}"


class ContactBook:
    """Manage a collection of Contact objects."""

    def __init__(self):
        """Initialize an empty contact book."""
        self.contacts = []

    def add_contact(self, contact):
        """Add a contact to the contact book.

        Args:
            contact (Contact): The Contact object to add.
        """
        self.contacts.append(contact)
        print(f"Added contact: {contact.name}")

    def remove_contact(self, name):
        """Remove a contact by exact name.

        Args:
            name (str): The full name of the contact to remove.

        Returns:
            bool: True if a contact was removed, otherwise False.
        """
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                self.contacts.remove(contact)
                return True

        return False

    def find_contact(self, name):
        """Find a contact using part or all of the name.

        Args:
            name (str): The name or part of the name to search for.

        Returns:
            Contact or None: The matching contact, or None if no
            matching contact is found.
        """
        for contact in self.contacts:
            # Convert both names to lowercase for case-insensitive searching.
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
    print(f"Search result for 'Kofi': {result.masked_view()}")