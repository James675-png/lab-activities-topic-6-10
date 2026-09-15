# Privacy-Audited Contact Book

## Description

The Privacy-Audited Contact Book is a Python application that demonstrates object-oriented programming, documentation, privacy protection, Git workflow, and secure software development practices.

The application provides a Contact class for storing contact information and a ContactBook class for managing multiple contacts.

The system supports:

- Adding contacts
- Removing contacts by exact name
- Finding contacts using all or part of a name
- Displaying contact information
- Masking email addresses to protect privacy

## Usage

Run the application from the project directory using:

python contact_book.py

The program creates two sample contacts and demonstrates adding contacts, searching for Kofi, and displaying the search result using a privacy-safe masked email address.

Example output:

Added contact: Amelia Turner
Added contact: Kofi Mensah
Search result for Kofi: Kofi Mensah | k**i@example.com | +675 7XX XXX XXX

## Testing

The application can be tested by running:

python contact_book.py

The test confirms that:

1. Contacts can be created successfully.
2. Contacts can be added to the contact book.
3. Contacts can be found using part of a name.
4. Contact information can be displayed.
5. Email addresses are masked in the privacy-safe view.

The code was reviewed after each major development stage to confirm that new changes did not break existing functionality.

## License

This project is distributed under the MIT License.

## AI Use Disclosure

An AI coding assistant was used to support development of this project, including suggestions for code structure, documentation, privacy masking logic, testing approaches, and README wording.

All AI-assisted suggestions were reviewed, tested, and edited by Clement James. The completed code and documentation were checked by the developer before being included in the project.
