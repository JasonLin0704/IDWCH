# ----------------------------------------------------------------------
# Instruction: 	A tool helps you correct homework. 
# Authors:		Jason, ${your_name}
# ----------------------------------------------------------------------

import os
import shutil

### You need to change:
# ----------------------------------------------------------
hw_num = '4'                # Which homework
hw_path = '/home/demo/HW4'  # Where those files at
target_path = '/home/demo'  # Where you want to move them to
# ---------------------------------------------------------- 
    
# Eliminate spaces of the file name
def rename():
    folder_list = os.listdir(hw_path)
    for folder_name in folder_list:
        old_name = folder_name
        new_name = folder_name.replace(' ', '_')
        os.rename(os.path.join(hw_path, old_name), os.path.join(hw_path, new_name))

# Create 3 folders to contain different types of submissions
def createFolder():
    for ext in ['c', 'cpp', 'pdf']:
        if os.path.exists(target_path + '/' + hw_num + '_' + ext) == False:
            os.mkdir(target_path + '/' + hw_num + '_' + ext)

# Collect those submissions into proper folders
def classify():
    target_path_c = target_path + '/' + hw_num + '_c' 
    target_path_cpp = target_path + '/' + hw_num + '_cpp' 
    target_path_pdf = target_path + '/' + hw_num + '_pdf' 

    folder_list = os.listdir(hw_path)
    for folder_name in folder_list:
        file_list = os.listdir(hw_path + '/' + folder_name)
        for file_name in file_list:

            root, extension = os.path.splitext(file_name)
            
            file_path = hw_path + '/' + folder_name + '/' + file_name

            # c file
            if extension == '.c':
                shutil.move(file_path, target_path_c)     
                if os.path.exists(file_path[:-2] + '.h') == True:
                    shutil.move(file_path[:-2] + '.h', target_path_c)

            # cpp file
            elif extension == '.cpp':
                shutil.move(file_path, target_path_cpp)   
                if os.path.exists(file_path[:-4] + '.h') == True:
                    shutil.move(file_path[:-4] + '.h', target_path_cpp)

            # pdf file
            elif extension == '.pdf':
                shutil.move(file_path, target_path_pdf)  

if __name__ == '__main__':
    rename()
    createFolder()
    classify()
