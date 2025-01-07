
def read_from_file(filepath: str):
    
    with open(filepath, "r+") as f:
        data = f.readlines()

    return data