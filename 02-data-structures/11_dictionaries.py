"""
Day 11: Dictionaries and Key-Value Pairs
Focus: Dictionary creation, access, safe retrieval with get(),
methods (keys, values, items), and frequency counting.
"""

# 1. Creating and Accessing Dictionaries
developer = {
    "name": "Jordan",
    "role": "Backend Engineer",
    "experience_years": 4,
    "primary_language": "Python",
    "remote": True
}

print("--- Dictionary Access ---")
print(f"Developer Name: {developer['name']}")
print(f"Role: {developer['role']}")

# Safe access with .get(key, default)
salary = developer.get("salary", "Confidential")
print(f"Salary (safe lookup): {salary}")

# 2. Modifying and Adding Entries
developer["experience_years"] = 5           # Update value
developer["frameworks"] = ["Django", "FastAPI"]  # Add new key
print(f"\nUpdated Developer Profile:\n{developer}")

# 3. Iterating over Dictionaries
print("\n--- Iterating with .items() ---")
for key, value in developer.items():
    print(f"  {key:<18}: {value}")

# 4. Dictionary Practical Exercise: Word Frequency Counter
sample_text = "python is fun and python is versatile and fast"
words = sample_text.split()
frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

print("\n--- Word Frequency Counter ---")
print(f"Sample text: '{sample_text}'")
for word, count in sorted(frequency.items(), key=lambda item: item[1], reverse=True):
    print(f"  '{word}': {count} time(s)")

# 5. Nested Dictionaries
servers = {
    "srv-web-01": {"ip": "192.168.1.10", "status": "active", "cpu_percent": 34.2},
    "srv-db-01":  {"ip": "192.168.1.20", "status": "active", "cpu_percent": 78.5},
    "srv-cache-01": {"ip": "192.168.1.30", "status": "maintenance", "cpu_percent": 0.0}
}

print("\n--- Nested Dictionary Inspection ---")
for host, info in servers.items():
    print(f"Host: {host:<14} | IP: {info['ip']:<14} | Status: {info['status']}")
