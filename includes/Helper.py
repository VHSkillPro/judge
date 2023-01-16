def get_type(fileName: str) -> str :
    pos = fileName.rfind('.')
    return fileName[pos + 1::]
