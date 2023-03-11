import shutil
import os

source_dir = "C:/Users/{user}/Desktop/source/"
destination_dir = "C:/Users/{user}/Desktop/destination/"


def move_files(source_directory: str, destination_directory: str, extension: str) -> str:
    """
    Move files from one folder to another based on extension.
    :param source_directory: str - is the source directory that contains the files that need to be moved
    :param destination_directory: str - is the destination directory, the place where the files will arrive
    :param extension: str -  is the type of file that will be moved
    :return: str - destination path
    """
    for file_name in os.listdir(source_directory):
        source = source_directory + file_name
        destination = destination_directory + file_name
        if os.path.isfile(source) and file_name.endswith(extension):
            shutil.move(source, destination)
            print(f"Moved {file_name} from {source_directory} to {destination_directory}.")
        else:
            print(f"{file_name} is not a file.")
    return destination_directory


print(move_files(source_directory=source_dir, destination_directory=destination_dir, extension=".txt"))
