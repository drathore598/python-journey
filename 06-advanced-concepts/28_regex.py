"""
Day 28: Regular Expressions and Pattern Matching
Focus: re module, regex syntax, search, findall, sub, and data validation patterns.
"""
import re

sample_text = """
Contact support team at support@pythonjourney.dev or sales-inquiries@learncode.io.
Office direct phone numbers: (555) 234-5678, 555-876-5432, or +1-555-901-2345.
Order logs: [2019-11-28] #ORD-8921 processed, [2019-11-29] #ORD-8922 pending.
"""

# 1. Extracting Email Addresses
email_pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
emails_found = re.findall(email_pattern, sample_text)
print("--- Extracted Emails ---")
for email in emails_found:
    print(f"  * {email}")

# 2. Extracting Order Numbers (#ORD-XXXX)
order_pattern = r'#ORD-\d{4}'
orders_found = re.findall(order_pattern, sample_text)
print("\n--- Extracted Orders ---")
print(f"Orders: {orders_found}")

# 3. Validating Phone Numbers with Regex Match
def is_valid_phone(phone: str) -> bool:
    # Matches patterns like 555-123-4567 or (555) 123-4567
    pattern = r'^\(?\d{3}\)?[- ]?\d{3}[- ]?\d{4}$'
    return bool(re.match(pattern, phone.strip()))

test_numbers = ["555-123-4567", "(555) 987-6543", "12345", "555-INVALID"]
print("\n--- Phone Validation ---")
for p in test_numbers:
    print(f"  {p:<16} -> Valid: {is_valid_phone(p)}")

# 4. Substitution: Redacting Sensitive Digits
raw_notes = "Credit account 4111-2222-3333-4444 approved for client."
# Replace middle card digits with XXXX
redacted = re.sub(r'\d{4}-\d{4}-\d{4}', 'XXXX-XXXX-XXXX', raw_notes)
print("\n--- Text Sanitization (re.sub) ---")
print(f"Original: {raw_notes}")
print(f"Redacted: {redacted}")
