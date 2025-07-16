import os

from config import MAX_CHARS

def get_file_content(working_directory, file_path):
    absolute_working = os.path.abspath(working_directory)
    absolute_path = os.path.abspath(os.path.join(working_directory, file_path))
    if not absolute_path.startswith(absolute_working):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(absolute_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    try:
        with open(absolute_path,"r") as f:
            file_string = f.read(MAX_CHARS)
            if f.read(1):
                file_string += f'[...File "{file_path}" truncated at 10000 characters]'
            return file_string
    except Exception as e:
        return f'Error: {e}'