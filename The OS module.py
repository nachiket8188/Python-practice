import os
from datetime import datetime

# print(os.getcwd())
os.chdir("C:/Users/Nachiket/Desktop")
# print(os.getcwd())
print(os.listdir())
# os.rename("Temp files","Temp_files")
# os.mkdir("Temp files")
# os.mkdir("Temp files/Sub-directory")  # this won't work. Throws an error.
# os.makedirs("Temp files/Sub-directory") # This works as makedirs() allows us to create sub-directories directly.
# os.rmdir(".idea")
# print(os.listdir())
# print(os.stat("Topic Paper - 'Using Dynamic Testing Tools'.docx"))
# print("Size of file in bytes = ", os.stat("Topic Paper - 'Using Dynamic Testing Tools'.docx").st_size)
# print("Last modification time for file = ", datetime.fromtimestamp
# (os.stat("Topic Paper - 'Using Dynamic Testing Tools'.docx").st_mtime))
# print(os.walk("C:/Users/Nachiket/Desktop"))  # returns a generator object
# for directory, directories, files in os.walk("C:/Users/Nachiket/Desktop"):
#     print(directory)
#     print(directories)
#     print(files)
#     print()
# print(os.environ)
# print((os.environ.get('PATH')).split(';'))
print(os.path.basename("Blur.lnk"))
print(os.path.abspath("/Blur.lnk"))
print(os.path.splitext("/Blur.lnk"))  # to separate file name & it's extension.
print(dir(os.path))
