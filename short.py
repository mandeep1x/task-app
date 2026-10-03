links = {
    "a" : "https://youtube.com/long-video-link",
    "b" : "https://www.youtube.com/@Apple",
    "c" : "https://www.facebook.com"
}

long_link= input("Type url link of any website: ")
clean_long= long_link.strip()

if clean_long == "":
    print("Link cannot be empty")
else:
    count = len(links)
    auto_number = f"s{count + 1}"
    links[auto_number] = clean_long
    for each_key, each_value in links.items():
        print(each_key, each_value)

choose_url= input("Choose the index name of URL: ")
if choose_url in links:
    print(choose_url, links[choose_url])
else:
    print("Not found")