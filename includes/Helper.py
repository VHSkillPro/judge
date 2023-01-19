def get_language(fileName: str) -> str :
    pos = fileName.rfind('.') 
    return None if pos == -1 else fileName[pos + 1::]

def get_name_without_extension(fileName: str) -> str :
    language = get_language(fileName)
    return fileName.removesuffix('.' + language)