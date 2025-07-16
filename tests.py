from functions.get_files_info import get_files_info
from functions.get_files_content import get_file_content
from functions.write_file import write_file

#print("Results for current directory:")
#print(get_files_info("calculator",".")+"\n")

#print("Results for 'pkg' directory:")
#print(get_files_info("calculator", "pkg")+"\n")

#print("Results for '/bin' directory:")
#print(get_files_info("calculator","/bin")+"\n")

#print("Results for '../' directory:")
#print(get_files_info("calculator","../")+"\n")

#print(get_file_content("calculator", "lorem.txt"))

#print(get_file_content("calculator", "main.py")+"\n")
#print(get_file_content("calculator", "pkg/calculator.py")+"\n")
#print(get_file_content("calculator", "/bin/cat")+"\n")
#print(get_file_content("calculator", "pkg/does_not_exist.py")+"\n")


print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")+"\n")
print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")+"\n")
print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed")+"\n")