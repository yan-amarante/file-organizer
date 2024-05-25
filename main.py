import os

print("insert the path to the directory \nEx: local_drive directory1 directory 2 directory3")
src_directory = input("path:")

src_directory = src_directory.replace(" ", ":\\", 1).replace(" ", "\\")

directory_content = os.listdir(src_directory)

filename_extensions_folder = {"placeholder"}
filename_extension_index = 1

for file in directory_content:
    filename_extensions_folder.add(os.path.splitext(file)[filename_extension_index])

filename_extensions_folder.remove("")
filename_extensions_folder.remove("placeholder") 

for filename_extension in filename_extensions_folder:
    if not(os.path.exists(src_directory + "\\" + filename_extension)):
        os.mkdir(src_directory + "\\" + filename_extension)
    else:
        continue

files_moved = 0
files_iterated = 0

for file in directory_content:
    if os.path.splitext(file)[filename_extension_index] != "":
        files_iterated += 1

    for filename_extension in filename_extensions_folder:
        if os.path.splitext(file)[filename_extension_index] == filename_extension :
            os.replace(src_directory + "\\" + file, src_directory + "\\" + filename_extension + "\\" + file)
            files_moved += 1

print("{iterated} iterated files \n{moved} moved files".format(iterated=files_iterated, moved=files_moved)) 
