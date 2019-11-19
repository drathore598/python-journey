"""
Day 19: File I/O and Context Managers
Focus: Writing files, appending data, reading lines,
and using 'with open(...)' context managers safely.
"""
import os

sample_log_file = "sample_activity.log"

# 1. Writing to a file (mode='w' creates or overwrites)
print("--- Writing Log File ---")
initial_logs = [
    "[2019-11-19 09:00:15] [INFO] System initialized successfully.\n",
    "[2019-11-19 09:15:32] [INFO] Database connection established.\n",
    "[2019-11-19 10:02:11] [WARNING] High memory usage detected (78%).\n"
]

with open(sample_log_file, "w", encoding="utf-8") as f:
    f.writelines(initial_logs)
print(f"Wrote {len(initial_logs)} entries to '{sample_log_file}'.")

# 2. Appending to a file (mode='a')
print("\n--- Appending Entries ---")
with open(sample_log_file, "a", encoding="utf-8") as f:
    f.write("[2019-11-19 11:30:00] [INFO] Scheduled backup completed.\n")
print(f"Appended backup event to '{sample_log_file}'.")

# 3. Reading and Analyzing the File
print("\n--- Reading and Parsing File Contents ---")
total_lines = 0
warning_count = 0

with open(sample_log_file, "r", encoding="utf-8") as f:
    for line in f:
        total_lines += 1
        stripped = line.strip()
        print(f"Line {total_lines}: {stripped}")
        if "[WARNING]" in stripped:
            warning_count += 1

print(f"\nAnalysis Summary: {total_lines} total lines, {warning_count} warning(s).")

# Clean up temporary test file
if os.path.exists(sample_log_file):
    os.remove(sample_log_file)
    print(f"Cleaned up temporary log file '{sample_log_file}'.")
