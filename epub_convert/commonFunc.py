import os

def findTargetFileList(ls_DataType=[".epub"], str_InputPath="./"):

    tmp_list = []
    allFileList = os.listdir(str_InputPath)

    for i in range(0, len(allFileList)):  # all file under the folder
        for j in range(0, len(ls_DataType)):  # target file type
            if (allFileList[i].endswith(ls_DataType[j])):
                tmp_list.append(str_InputPath + "\\" + allFileList[i])

    return tmp_list

def mkdir(path):
    folder = os.path.exists(path)

    if not folder:
        os.makedirs(path)
        print('\n-----Generate Directory Successfully----\n' +
              '[' + path + ']\n')
    else:
        # If folder is exist, print msg to note the user
        print('\n[' + path + ']'+'\nFolder Exists')

def chkdir(path):
    return os.path.isdir(path)

# # ==================== Base Classes ====================
# class __Common:
#     """
#     A base class for other models in the application.
#     It provides common functionality like a basic representation.
#     """
#     def __init__(self, name):
#         self.name = name

#     def __repr__(self):
#         return f"<{self.__class__.__name__}(name='{self.name}')>"

