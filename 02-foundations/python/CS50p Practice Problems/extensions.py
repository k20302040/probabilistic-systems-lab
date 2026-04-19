input = input("Enter file: ").lower()

if ".gif" in input:
    print("image/gif")
elif ".jpg" in input or ".jpeg" in input:
    print("image/jpeg")
elif ".png" in input:
    print("image/png")
elif ".pdf" in input:
    print("application/pdf")
elif ".txt" in input:
    print("text/plain")
elif ".zip" in input:
    print("application/zip")
else:
    print("application/octet-stream")
