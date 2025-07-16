from functions.get_files_info import get_files_info
from functions.get_files_content import get_file_content

#print("Results for current directory:")
#print(get_files_info("calculator",".")+"\n")

#print("Results for 'pkg' directory:")
#print(get_files_info("calculator", "pkg")+"\n")

#print("Results for '/bin' directory:")
#print(get_files_info("calculator","/bin")+"\n")

#print("Results for '../' directory:")
#print(get_files_info("calculator","../")+"\n")

#print(get_file_content("calculator", "lorem.txt"))

print(get_file_content("calculator", "main.py")+"\n")
print(get_file_content("calculator", "pkg/calculator.py")+"\n")
print(get_file_content("calculator", "/bin/cat")+"\n")
print(get_file_content("calculator", "pkg/does_not_exist.py")+"\n")