def get_language(fileName: str) -> str :
    """
        Return :
            - None if file don't have extension
            - Else return extension of file
    """
    pos = fileName.rfind('.') 
    return None if pos == -1 else fileName[pos + 1::]

def get_name_without_extension(fileName: str) -> str :
    """
        Return filename without extension
    """
    language = get_language(fileName)
    return fileName.removesuffix('.' + language)