import os 
import subprocess

from google.genai import types


def run_python_file(working_directory, file_path, args=[]):
    absolute_path=os.path.abspath(os.path.join(working_directory,file_path))
    absolute_working=os.path.abspath(working_directory)
    if not absolute_path.startswith(absolute_working):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(absolute_path):
        return f'Error: File "{file_path}" not found.'
    if not absolute_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    try:
        command = ["uv", "run", absolute_path] + args
        completed_process = subprocess.run(command,timeout=30,capture_output=True,cwd=absolute_working,text=True)
        output = f"STDOUT: {completed_process.stdout}\nSTDERR: {completed_process.stderr}"
        if completed_process.stdout.strip() == "" and completed_process.stderr.strip() == "":
            return "No output produced."
        if completed_process.returncode != 0:
            output += f"\nProcess exited with code {completed_process.returncode}"
        return output.strip()
    except Exception as e:
        return f"Error: executing Python file: {e}"
    
schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes a Python file within the working directory and returns the output from the interpreter.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the Python file to execute, relative to the working directory.",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(
                    type=types.Type.STRING,
                    description="Optional arguments to pass to the Python file.",
                ),
                description="Optional arguments to pass to the Python file.",
            ),
        },
        required=["file_path"],
    ),
)
