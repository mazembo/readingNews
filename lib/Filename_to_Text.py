import getFiles
path = "/home/mavungu/Lecongolais.net/facebook"
myfiles = getFiles.allImages(path)
message_files = [f for f in myfiles if f.__contains__("-RDC-")]
print message_files
print len(message_files)
for f in message_files:
    date_published = f[:10]
    message = f[15:]
    filename = f
    
