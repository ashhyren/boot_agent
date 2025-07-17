import os 
import subprocess


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
