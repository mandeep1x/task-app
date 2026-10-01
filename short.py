links = {
    "a" : "https://youtube.com/long-video-link",
    "b" : "https://www.youtube.com/@Apple"
}

for each_key, each_value in links.items():
    print(each_key, each_value)

long_link= input("Type url link of any website: ")
clean_long= long_link.strip()

if clean_long == "":
    print("Link cannot be empty")
else:
    links["c"] = clean_long
    for each_key, each_value in links.items():
        print(each_key, each_value)

    