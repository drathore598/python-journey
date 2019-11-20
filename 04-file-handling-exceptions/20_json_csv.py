"""
Day 20: Working with JSON and CSV Data
Focus: json.dump/dumps, json.load/loads, csv.writer, and csv.DictReader.
"""
import os
import json
import csv

# 1. JSON Serialization & Deserialization
students_data = [
    {"id": 1, "name": "Elena Rostova", "major": "Computer Science", "gpa": 3.92},
    {"id": 2, "name": "Marcus Vance", "major": "Data Analytics", "gpa": 3.75},
    {"id": 3, "name": "Amina Said", "major": "Software Engineering", "gpa": 3.88}
]

json_file = "students.json"
csv_file = "students.csv"

# Writing JSON to file
with open(json_file, "w", encoding="utf-8") as f:
    json.dump(students_data, f, indent=2)
print("--- JSON Output ---")
print(f"Saved student records to '{json_file}'.")

# Reading JSON back
with open(json_file, "r", encoding="utf-8") as f:
    loaded_students = json.load(f)
print(f"Loaded {len(loaded_students)} records from JSON. Sample student: {loaded_students[0]['name']}")

# 2. CSV Writing and Reading
print("\n--- CSV Processing ---")
with open(csv_file, "w", newline="", encoding="utf-8") as f:
    fieldnames = ["id", "name", "major", "gpa"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(students_data)
print(f"Exported data to '{csv_file}'.")

# Reading CSV with csv.DictReader
parsed_from_csv = []
with open(csv_file, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        parsed_from_csv.append(row)

print("Parsed CSV records:")
for row in parsed_from_csv:
    print(f"  ID {row['id']}: {row['name']} ({row['major']}) - GPA: {row['gpa']}")

# Clean up generated files
for path in [json_file, csv_file]:
    if os.path.exists(path):
        os.remove(path)
