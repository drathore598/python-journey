"""
Day 12: Sets and Set Operations
Focus: Set creation, uniqueness guarantee, adding/removing items,
and mathematical set operations (union, intersection, difference).
"""

# 1. Uniqueness Guarantee and Deduplication
raw_ids = [101, 102, 103, 101, 104, 102, 105]
unique_ids = set(raw_ids)

print("--- Set Basics ---")
print(f"Raw list with duplicates: {raw_ids}")
print(f"Unique set: {unique_ids}")
print(f"Total: {len(raw_ids)}, Unique: {len(unique_ids)}")

# 2. Modifying Sets
tech_stack = {"Python", "Git", "Docker"}
tech_stack.add("PostgreSQL")       # Add single item
tech_stack.update(["Redis", "AWS"]) # Add multiple items
tech_stack.discard("Git")          # Discard does not raise KeyError if item missing
print(f"\nUpdated Tech Stack: {tech_stack}")

# 3. Mathematical Set Operations
frontend_skills = {"HTML", "CSS", "JavaScript", "React", "TypeScript"}
backend_skills  = {"Python", "PostgreSQL", "Docker", "JavaScript", "TypeScript"}

# Union (|): All skills
all_skills = frontend_skills | backend_skills
# Intersection (&): Skills needed by both frontend and backend
fullstack_overlap = frontend_skills & backend_skills
# Difference (-): Skills unique to frontend
only_frontend = frontend_skills - backend_skills
# Symmetric Difference (^): Skills in either, but NOT in both
specialized_skills = frontend_skills ^ backend_skills

print("\n--- Set Operations ---")
print(f"Union (All Skills):\n  {sorted(all_skills)}")
print(f"Intersection (Overlap):\n  {sorted(fullstack_overlap)}")
print(f"Frontend Only Difference:\n  {sorted(only_frontend)}")
print(f"Symmetric Difference:\n  {sorted(specialized_skills)}")

# 4. Subset and Superset Checks
required_skills = {"HTML", "CSS"}
print(f"\nIs required_skills subset of frontend_skills? {required_skills.issubset(frontend_skills)}")
print(f"Is frontend_skills superset of required_skills? {frontend_skills.issuperset(required_skills)}")
