import json

list = {
    "name": "Mandeep singh",
    "age": "24",
    "country": "India",
    "Graduation": "BCA",
    "skills": ["python", "advance python", "mysql", "postgresql", "django"],
    "college": "Guru gobind singh college"
}
with open("demo.json", "w") as file:
    json.dump(list, file, indent= 4)

with open("demo.json", "r") as file:
    file_read = json.load(file)

print(file_read)
