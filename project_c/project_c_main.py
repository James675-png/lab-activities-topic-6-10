# project_c_main.py
# Demonstrates reusing the shared_package from Project C.

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from shared_package import format_currency, is_valid_password, slugify

print(format_currency(500))
print("Password valid:", is_valid_password("ProjectC123"))
print("Slug:", slugify("Project C Example"))
