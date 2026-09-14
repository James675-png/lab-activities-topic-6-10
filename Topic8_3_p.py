# Topic8_3_p.py
# Demonstrates the reusable truncate() function.

import text_utils

text = "Python reusable modules make programming easier."

print("Original:", text)
print("Truncated:", text_utils.truncate(text, 20))
