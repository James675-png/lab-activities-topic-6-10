# text_utils.py
# A reusable module for text utility functions.

def truncate(text, max_length):
    """Return text unchanged if it fits, otherwise truncate and add '...'."""
    if len(text) <= max_length:
        return text
    return text[:max_length] + "..."
