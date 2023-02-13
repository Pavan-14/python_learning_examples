import os

print(os.path.isdir(r"D:\autocad"))

"""
# to check the path existed or not
print(os.path.exists(r'E:\Pavan Learnings\Braineest\week_02'))

#to check it is a directory or not
print(os.path.isdir(r'E:\Pavan Learnings\Braineest\week_01'))

#to check symbolic link (the answer False because if python won't support symbolic links on runtime)
print(os.path.islink(r'E:\Pavan Learnings\Braineest\week_01'))

#list of directories and file in a path
print(os.listdir(r'E:\Pavan Learnings'))

#create a directory. if directory existed raise exception
try:
    os.mkdir(r'E:\Pavan Learnings\Braineest\week_01')
except OSError as error:
    print(error)


# use the method os.path.join(path, *paths)
newdirectory = 'hhello'

parent_path = r"E:\Pavan Learnings\Braineest\week_01"

print(os.path.join(parent_path,newdirectory))




'''use the method os.makedirs(name, mode=0o777, exist_ok=False)'''
# Leaf directory 
directory = "c"
    
# Parent Directories (but a, b directories are not presented)
parent_dir = r"E:\Pavan Learnings\Braineest\week_01\a\b"
    
# mode 
mode = 0o666
    
path = os.path.join(parent_dir, directory) 
    
# Create the directory 'c' 
     
os.makedirs(path, mode) 
print("Directory '% s' created" % directory) 




'''exception suppressed by using the exist_ok = True'''
# os.makedirs() method will raise
# an OSError if the directory
# to be created already exists
# But It can be suppressed by
# setting the value of a parameter
# exist_ok as True
  
# Directory
directory = "c"
  
# Parent Directory path
parent_dir = r"E:\Pavan Learnings\Braineest\week_01\a\b"
  
# Path
path = os.path.join(parent_dir, directory)
  
# Create the directory
# 'c'
try:
    os.makedirs(path, exist_ok = True)
    print("Directory '%s' created successfully" % directory)
except OSError as error:
    print("Directory '%s' can not be created" % directory)
  
# By setting exist_ok as True
# error caused due already (the "FileExistsError" error suppressed)
# existing directory can be suppressed
# but other OSError may be raised
# due to other error like
# invalid path name
# exist_ok as False you will get print("Directory '%s' can not be created" % directory) statement as output

"""
