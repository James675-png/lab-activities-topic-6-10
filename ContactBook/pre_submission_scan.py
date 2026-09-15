import re
from pathlib import Path


FILES_TO_SCAN = [
    Path("contact_book.py"),
    Path("README.md"),
    Path("CODE_REVIEW.md"),
]

SECRET_PATTERNS = [
    r"sk_live_[A-Za-z0-9]+",
    r"sk_test_[A-Za-z0-9]+",
    r"AKIA[0-9A-Z]{16}",
    r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----",
]


def scan_file(file_path):
    """Scan one project file for common hard-coded secret patterns.

    Args:
        file_path (Path): The project file to scan.

    Returns:
        list: A list of flagged line numbers and matching text.
    """
    findings = []

    if not file_path.exists():
        return findings

    content = file_path.read_text(encoding="utf-8")

    for line_number, line in enumerate(content.splitlines(), start=1):
        for pattern in SECRET_PATTERNS:
            if re.search(pattern, line):
                findings.append((line_number, line.strip()))

    return findings


print("Pre-submission secret scan")
print("---------------------------")

total_findings = 0

for file_path in FILES_TO_SCAN:
    findings = scan_file(file_path)

    if findings:
        for line_number, line in findings:
            print(f"FLAGGED: {file_path}:{line_number}: {line}")
            total_findings += 1
    else:
        print(f"Checked: {file_path} - No secrets detected.")

print()

if total_findings == 0:
    print("No hard-coded secrets detected.")
else:
    print(f"Scan completed with {total_findings} flagged line(s).")