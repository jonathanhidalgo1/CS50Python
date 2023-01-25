x = input("File name:").split(".")
extentions = ["gif" , "jpg" , "jpeg" , "pdf" , "txt", "zip"]
if x[1] in extentions:
    print("image/" + x[1])
else:
    print("application/octet-stream")
    

