import os


def print_directory_contents(s_path:str) -> None:
    """
    This function takes the name of a directory 
    and prints out the paths files within that 
    directory as well as any files contained in 
    contained directories. 
    This function is similar to os.walk. Please don't
    use os.walk in your answer. We are interested in your 
    ability to work with nested structures. 
    """
    for item in os.listdir():
        print(os.path.abspath(item))
        if isinstance(item, os.path.directory):
            return print_directory_contents(item)
