import json

data = {
    "name": "Mandeep",
    "age": 24,
    "Country": "India",
    "skills": ["Python", "Data Analysis"]
}

# Save data to a JSON file (json.dump)
with open("demo.json", "w") as file:
    json.dump(data, file, indent= 4)

print("Data successfully written to data.json")


# Read data from the JSON file (json.load)
with open("demo.json", "r") as file:
    loaded_data = json.load(file)

print("\nData successfully read from data.json:")
print(loaded_data)
print(f"Type: {type(loaded_data)}")
