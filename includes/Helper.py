def get_language(fileName: str) -> str :
    return fileName[fileName.rfind('.') + 1::]

def get_name_without_extension(fileName: str) -> str :
    language = get_language(fileName)
    return fileName.removesuffix('.' + language)