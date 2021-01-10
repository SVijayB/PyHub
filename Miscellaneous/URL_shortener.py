import pyshorteners

# Single URL
s = pyshorteners.Shortener()
print(s.tinyurl.short("https://www.wallpapertip.com/wmimgs/104-1041715_itachi-uchiha-wallpaper-4k.jpg"))

# Multiple URLS
list_of_links = ["https://wallpaperaccess.com/full/872451.jpg",
                "https://i.pinimg.com/originals/a0/5a/50/a05a50b78e78669c98adaa38c50eb149.jpg",
                "https://image.wallpapercome.com/360/24360.jpg"]

for x in list_of_links:
    print(s.tinyurl.short(x))
