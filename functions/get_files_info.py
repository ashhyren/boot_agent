import os
from google.genai import types

def get_files_info(working_directory, directory="."):
    full_path = os.path.abspath(os.path.join(working_directory, directory))
    if not full_path.startswith(os.path.abspath(working_directory)):
        return f"Error: Cannot list '{directory}' as it is outside the permitted working directory"
    if not os.path.isdir(full_path):
        return f'Error: "{directory}" is not a directory'
    try:
        path_list = []
        for i in os.listdir(full_path):
            path_list.append(f'- {i}: file_size={os.path.getsize(os.path.join(full_path,i))} bytes, is_dir={os.path.isdir(os.path.join(full_path,i))}')
        return "\n".join(path_list)
    except Exception as e:
        return f"Error: {e}"
    
schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)

available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
    ]
)