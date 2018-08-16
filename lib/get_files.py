import os


path = "/home/mavungu/Lecongolais.net/facebook"
filenames = next(os.walk(path))[2]
today = "2017-04-28"
len(filenames)
filenames_today = [f for f in filenames if f.startswith(today)]
filenames_today_pictures = [f for f in filenames_today if f.endswith((".jpg", ".jpeg", ".gif", ".png"))]
