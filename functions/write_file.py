import os

def write_file(working_directory, file_path, content):
    absolute_file = os.path.abspath(os.path.join(working_directory,file_path))
    absolute_working = os.path.abspath(working_directory)
    if not absolute_file.startswith(absolute_working):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(absolute_file):
        try:
            os.makedirs(os.path.dirname(absolute_file),exist_ok=True)
        except Exception as e:
            return f'Error: {e}'
    if os.path.exists(absolute_file) and os.path.isdir(absolute_file):
        return f'ErrorL "{file_path}" is a directory, not a file'
    try:
        with open(absolute_file,"w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error: {e}"