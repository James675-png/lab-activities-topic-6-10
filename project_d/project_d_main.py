# project_d_main.py
# Demonstrates reusing the shared_package from Project D.

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from shared_package import validate_email, format_currency, slugify

print("Email valid:", validate_email("student@university.edu"))
print("Amount:", format_currency(1250.75))
print("Slug:", slugify("Project D Example"))
