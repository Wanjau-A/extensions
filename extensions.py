def main():
    file_name = input("Text: ")
    file_media_type = media_type_of(file_name)
    print(file_media_type)


def media_type_of(file_name):
    """
    This function computes the file media type given file name 

    Arguements: 
        file_name (str) - the name of a file 

    Returns:
        media_type (str) -  the media type of the given file
    """
    file_name = file_name.lower().strip()
    if file_name.endswith(".jpg"):
        return "image/jpeg"
    elif file_name.endswith(".pdf"):
        return "application/pdf"
    elif file_name.endswith(".gif"):
        return "image/gif"
    elif file_name.endswith(".png"):
        return "image/png"
    elif file_name.endswith(".txt"):
        return "text/plain"
    elif file_name.endswith(".zip"):
        return "application/zip"
    elif file_name.endswith(".jpeg"):
        return "image/jpeg"
    
if __name__ == "__main__":
    main()
