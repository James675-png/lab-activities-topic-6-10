# utilities.py
# A reusable, self-contained module with no dependency on any specific project.

def format_currency(amount, currency_symbol="$"):
    """Return a formatted currency string, e.g. '$1,250.00'."""
    return f"{currency_symbol}{amount:,.2f}"


def validate_email(email):
    """Return True if the email contains exactly one '@' and at least one '.' after it."""
    if email.count("@") != 1:
        return False
    local_part, domain_part = email.split("@")
    return "." in domain_part


def is_valid_password(password):
    """Return True if the password is at least 8 characters long."""
    return len(password) >= 8


def slugify(text):
    """Convert text into a lowercase, hyphen-separated slug."""
    return text.lower().replace(" ", "-")
