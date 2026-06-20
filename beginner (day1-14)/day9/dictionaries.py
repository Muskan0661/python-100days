info = {
    "key": "value",
    "name": "muskan makhija",
    "learning": "coding",
    "age": "20",
    "is_adult": True,
    "subjects": {
        "phy": 80,
        "chem": 70,
        "math": 75
    }
}

info["name"] = "muskan"      # Update existing value
info["surname"] = "makhija"  # Add new key-value pair

print(info)  # We can modify dictionaries and lists, but tuples are immutable.

print("\nmethods\n")

print(len(info))             # Number of keys in dictionary
print(info.keys())           # Returns all keys
print(list(info.keys()))     # Convert keys to a list
print(info.values())         # Returns all values
print(info.items())          # Returns all (key, value) pairs as tuples
print(info.get("name"))      # Returns value of key "name"
info.update({"degree": "bscs"})  # Adds/updates key-value pair
print(info)
