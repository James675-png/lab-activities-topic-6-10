# Topic8_3_p2.py
# Demonstrates reusing the truncate() function with a different length.

import text_utils

text = "Python reusable modules make programming easier."

print("Original:", text)
print("Truncated:", text_utils.truncate(text, 30))
