#-*- code: utf-8 -*-
def main():
    filename, extension = input("Enter the file name: ").lower().rsplit(".")
    print(matchExtension(extension))

def matchExtension(extension):
    
    mediatypes = {"gif": "image/gif",
                  "jpg": "image/jpeg",
                  "jpeg": "image/jpeg",
                  "png": "image/png",
                  "pdf": "application/pdf",
                  "txt": "text/plain",
                  "zip": "application/zip"}
    
    if extension in mediatypes:
        return (mediatypes[extension])
    else:
        return ("application/octet-stream")

main()
