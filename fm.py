"""
## File manager
```
author      : "Anas shakeel"
python--ver : 3.11
fm--version : 1.0
fm--descrip : "Features some cool (file management and other) tools"
```
This particular class and all of code in it is a backend that
serves to the 'main.py' file.
"""

import os
import shutil
import platform as pt
import time


class FileManager:
    """
    ## File Manager
    A custom file management class to handle basic file management.
    """

    def __init__(self) -> None:
        pass

    def folder_bomb(self, directory: str, name="folder"):
        """
        ### Folder bomb
        Creates empty folders in a directory infinitely until user
        stops the program (ctrl+c).

        Be careful with this one as it will silently keep 
        creating thousands of folders per second upon call.

        ### Be sure to somehow tell the users that they can press
        ### ctrl+c (KeyboardInterrupt) to stop or break this loop.
        """

        # directory validation
        if not os.path.exists(directory):
            raise ValueError("directory does not exists")

        # creating folder path
        folder_path = os.path.normpath(f"{directory}\\{name}")

        n = 0
        # infinite loop
        while True:
            try:
                # create folder name
                folder = f"{folder_path} {n}"

                # if folder already exists, skip to next iteration
                if os.path.exists(folder):
                    n += 1
                    continue

                # create folder
                os.mkdir(folder)
                n += 1

            except FileExistsError:
                # print("Folder already exists")
                pass

    def create_folder(self, directory: str, name: str):
        """
        ### Create a folder
        Creates a folder in `directory` with `name`

        ```
        >> fm.create_folder(directory="C:\\Old folder", name="New folder")
        # if folder 'name' does not already exist in 'directory'
        'C:\\Old folder\\New folder'

        # if it exists
        FileExistsError()
        ```
        """

        # directory validation
        if not os.path.isdir(directory):
            raise ValueError("'directory' does not exist")

        # create folder_name
        folder_name = os.path.join(os.path.normpath(directory), name)

        # folder_name validation
        if os.path.isdir(folder_name):
            raise FileExistsError(f"'{folder_name}' already exists")

        # CREATE FOLDER
        os.mkdir(folder_name)

    def create_folders(self, directory: str,  name: str, n: int):
        """
        ### Create Folders
        Creates `n` empty folders in `directory` with `name`

        """

        # directory validation
        if not os.path.exists(directory):
            raise ValueError("directory does not exists")

        # create folder path
        # folders_path = os.path.normpath(f"{directory}\\{name}")
        folders_path = os.path.join(os.path.normpath(directory), name)

        # CREATE FOLDERS
        for i in range(n):
            # make a folder with increment integers
            folder = f"{folders_path} {i}"

            # if folder already exists, skip to next iteration
            if os.path.exists(folder):
                # print(f"{folder} already exists")
                continue

            # create folder
            os.mkdir(folder)

    def copy_file(self, src: str, dst: str):
        """
        ### Copy File
        Copy a file from `src` to `dst`

        if `src` file already exists in `dst`, a new file is created with the same name
        with increments.

        ```
        # Parameters
        src = "C:\\file.txt"
        dst = "D:\\folder"
        ```
        """
        # src validation
        if not os.path.isfile(src):
            raise ValueError("'src' file does not exist")

        # dst validation
        if not os.path.isdir(dst):
            raise ValueError("'dst' directory does not exist")

        # create file name
        filename = self.filename_increment(src, dst)

        # copying file
        shutil.copyfile(src, filename)

    def copy_files(self, src: str, dst: str, ext=".txt", whole_tree=False):
        """
        ### Copy Files
        Copies all files with `ext` extensions from `src` to `dst`

        ```
        # parameters
        src = 'where to look for files'
        dst = 'where to copy the files'
        ext = 'what files to copy'
        whole_tree = 'scan only root-dir or sub-dirs also'
        ```
        """

        # src validation
        if not os.path.exists(src):
            raise ValueError("'src' directory does not exist")

        # dst validation
        if not os.path.exists(dst):
            raise ValueError("'dst' directory does not exist")

        # scan the src directory and look for the files
        if whole_tree:
            # scan all subdirs also
            for file in self.search_files(src, ext, whole_tree=True):
                self.copy_file(file, dst)

        else:
            # scan only root dir
            for file in self.search_files(src, ext, whole_tree=False):
                self.copy_file(file, dst)

    def copy_all_files(self, src: str, dst: str, whole_tree=False):
        """
        ### Copy All Files
        Copies all files from `src` to `dst`

        ```
        # parameters
        src = 'where to look for files'
        dst = 'where to copy the files'
        whole_tree = 'scan only root-dir or sub-dirs also'
        ```
        """

        # src validation
        if not os.path.exists(src):
            raise ValueError("'src' directory does not exist")

        # dst validation
        if not os.path.exists(dst):
            raise ValueError("'dst' directory does not exist")

        # scan the src directory and look for the files
        if whole_tree:
            # scan all subdirs also
            for root, dirs, files in os.walk(src):
                for file in files:
                    self.copy_file(os.path.join(root, file), dst)

        else:
            # scan only root dir
            with os.scandir(src) as scanner:
                for entry in scanner:
                    if entry.is_file():
                        self.copy_file(entry, dst)

    def copy_directory(self, src: str, dst: str):
        """
        ### Copy Directory
        Copies a whole directory `src` to `dst`

        if a folder already exists in `dst`, creates a new folder with the same 
        name (incremented)
        """
        # src validation
        if not os.path.isdir(src):
            raise ValueError("'src' directory does not exist")

        # dst validation
        if not os.path.isdir(dst):
            raise ValueError("'dst' directory does not exist")

        # create new foldername (with increments)
        folder_name = self.foldername_increment(src, dst)

        # copy the directory to 'dst'
        shutil.copytree(src, os.path.join(dst, folder_name))

    def delete_file(self, filepath: str):
        """
        ### Delete File
        Deletes the given `filepath` file
        """

        # if file doesn't exists, raise valueError
        if not os.path.isfile(filepath):
            raise ValueError("file does not exist")

        # delete file
        os.remove(filepath)

    def delete_files(self, directory: str, ext=".txt", whole_tree=False):
        """
        ### Delete Files
        Deletes files of `ext` extension from a `directory`

        ##### Parameters
            - `directory` folder path from which to delete files
            - `ext` which files to delete
            - `whole_tree` if True, walks the whole directory tree and deletes all `ext` files

        """

        # check if directory exists or not
        if not os.path.exists(directory):
            raise ValueError("directory does not exists")

        if whole_tree:
            # scan whole directory tree
            for root, dirs, files in os.walk(directory):
                for file in files:
                    # if file is of 'ext' extension, delete!
                    if os.path.splitext(file)[-1] == ext:
                        os.remove(os.path.join(root, file))

        else:
            # scan given directory
            with os.scandir(directory) as scanner:
                for entry in scanner:
                    if os.path.isfile(entry):
                        # if file is of extension 'ext'
                        if os.path.splitext(entry)[-1] == ext:
                            # delete the file
                            os.remove(entry.path)

    def delete_all_files(self, directory: str, whole_tree=False):
        """
        ### Delete All Files
        Deletes all files found in `directory` and also in sub directories if
        `whole_tree` is set to `True`.
        """
        # directory validation
        if not os.path.exists(directory):
            raise ValueError("directory does not exist")

        # ! DELETE FILES
        if whole_tree:
            # * delete every file found in every sub-dirs
            for root, dirs, files in os.walk(directory):
                # delete every file found in root-dir and sub-dirs
                for file in files:
                    os.remove(os.path.join(root, file))

        else:
            # * delete every file found only in the root-dir
            with os.scandir(directory) as scanner:
                for entry in scanner:
                    # delete every file found in root dir
                    if entry.is_file():
                        os.remove(entry)

    def delete_directory(self, directory: str):
        """
        ### Delete directory
        Deletes a whole directory permenantly

        #### Be careful with this one! one mistake and your data, GONE!!!
        """
        # directory validation
        if not os.path.isdir(directory):
            raise ValueError("directory does not exist")

        # remove dir-tree
        shutil.rmtree(directory)

    def delete_empty_folders(self, directory: str, whole_tree=False):
        """
        ### Delete Empty Folders
        Deletes all empty folders from a directory.

        ##### Parameters:
        ```
        directory:
            "Directory to delete folders from"
        whole_tree:
            "If True, deletes all empty folders from that directory tree otherwise, only from main directory"
        ```
        """

        # if dir doesn't exists, raise error
        if not os.path.exists(directory):
            raise ValueError("directory does not exist")

        # START CLEANING
        if whole_tree:
            # scan whole tree
            for root, dirs, files in os.walk(directory, topdown=False):
                for sub in dirs:
                    try:
                        # try to remove the folder
                        os.rmdir(os.path.join(root, sub))

                    except OSError:
                        # if folder not empty, skip to next iteration
                        continue

        else:
            # scan only provided dir
            with os.scandir(directory) as scanner:
                for entry in scanner:
                    if entry.is_dir():
                        try:
                            # remove the folder
                            os.rmdir(entry.path)

                        except OSError:
                            # if not empty, skip to next iteration
                            continue

    def filename_increment(self, filepath: str, dst_path=""):
        """
        ### Filename Increment
        Adds an incremented number in the `filepath` if file already exists in `dst_path`

        if `dst_path` is omitted, method will use the `filepath`'s root dir to look 
        if filename exists or not

        ```
        >> FileManager.filename_increment("C:\\file.txt")
        # if file already exists
        'C:\\file 0.txt'

        # otherwise
        'C:\\file.txt'
        ```
        """

        # extract filename and extension
        filename = os.path.splitext(os.path.basename(filepath))[0]
        ext = os.path.splitext(filepath)[-1]

        # set root path
        if dst_path == "":
            # if dst_path omitted, set file's path
            root = os.path.split(filepath)[0]
        else:
            # if path given, set dst_path's path
            root = dst_path

        # creating new_name
        new_name = os.path.join(root, filename + ext)

        # if file exists
        if os.path.exists(new_name):
            for i in range(1000000):
                # create a new name
                new_name = f"{os.path.join(root, filename)} {i}{ext}"

                # if new_name is non-existent, return
                if not os.path.exists(new_name):
                    return new_name
        else:
            return new_name

    def foldername_increment(self, folderpath: str, dst_path=""):
        """
        ### Foldername Increment
        Adds an incremented number in the `folderpath` if file already exists in `dst_path`

        if `dst_path` is omitted, method will use the `folderpath`'s root dir to look 
        if folder exists or not

        ```
        >> FileManager.foldername_increment("C:\\folder")
        # if file already exists
        'C:\\folder 0'

        # otherwise
        'C:\\folder'
        ```
        """

        # extract foldername
        folder_name = os.path.basename(os.path.normpath(folderpath))

        # set root path
        if dst_path == "":
            # if dst_path omitted, set folder's path
            root = os.path.split(folderpath)[0]
        else:
            # if dst_path given, set dst_path's path
            root = dst_path

        # creating new_name
        new_name = os.path.join(root, folder_name)

        # if folder exists
        if os.path.exists(new_name):
            for i in range(1000000):
                # create a new name
                new_name = f"{os.path.join(root, folder_name)} {i}"

                # if new_name is non-existent, return
                if not os.path.exists(new_name):
                    return new_name
        else:
            return new_name

    def move_file(self, src: str, dst: str):
        """
        ### Move File
        Move a file from `src` to `dst`

        if `src` file already exists in `dst`, a new file is created with the same name
        with increments.

        ```
        # Parameters
        # src = "C:\\file.txt"
        # dst = "D:\\folder"
        ```
        """
        # src validation
        if not os.path.isfile(src):
            raise ValueError("'src' file does not exist")

        # dst validation
        if not os.path.isdir(dst):
            raise ValueError("'dst' directory does not exist")

        # create file name
        filename = self.filename_increment(src, dst)

        # moving file
        shutil.move(src, filename)

    def move_files(self, src: str, dst: str, ext=".txt", whole_tree=False):
        """
        ### Move Files
        Move all files with `ext` extensions from `src` to `dst`

        ```
        # parameters
        src = 'where to look for files'
        dst = 'where to move the files'
        ext = 'what files to move'
        whole_tree = 'scan only root-dir or sub-dirs also'
        ```
        """

        # src validation
        if not os.path.exists(src):
            raise ValueError("'src' directory does not exist")

        # dst validation
        if not os.path.exists(dst):
            raise ValueError("'dst' directory does not exist")

        # scan the src directory and look for the files
        if whole_tree:
            # scan all subdirs also
            for file in self.search_files(src, ext, whole_tree=True):
                self.move_file(file, dst)

        else:
            # scan only root dir
            for file in self.search_files(src, ext, whole_tree=False):
                self.move_file(file, dst)

    def move_all_files(self, src: str, dst: str, whole_tree=False):
        """
        ### Move All Files
        Move all files from `src` to `dst`

        ```
        # parameters
        src = 'where to look for files'
        dst = 'where to move the files'
        whole_tree = 'scan only root-dir or sub-dirs also'
        ```
        """

        # src validation
        if not os.path.exists(src):
            raise ValueError("'src' directory does not exist")

        # dst validation
        if not os.path.exists(dst):
            raise ValueError("'dst' directory does not exist")

        # scan the src directory and look for the files
        if whole_tree:
            # scan all subdirs also
            for root, dirs, files in os.walk(src):
                for file in files:
                    self.move_file(os.path.join(root, file), dst)

        else:
            # scan only root dir
            with os.scandir(src) as scanner:
                for entry in scanner:
                    if entry.is_file():
                        self.move_file(entry, dst)

    def move_directory(self, src: str, dst: str):
        """
        ### Move Directory
        Moves a whole directory `src` to `dst`

        if a folder already exists in `dst`, creates a new folder with the same 
        name (incremented)
        """
        # src validation
        if not os.path.isdir(src):
            raise ValueError("'src' directory does not exist")

        # dst validation
        if not os.path.isdir(dst):
            raise ValueError("'dst' directory does not exist")

        # create new foldername (with increments)
        folder_name = self.foldername_increment(src, dst)

        # copy the directory to 'dst'
        shutil.move(src, os.path.join(dst, folder_name))

    def search_files(self, directory: str, ext: str, whole_tree=False):
        """
        ### Search Files
        Returns a generator of all filepaths with `ext` extension in `directory`

        ```
        # Parameters
        directory = "where to find the files, e.g 'C:\\Program Files'"
        ext = "what type of files to find, e.g '.txt'"
        whole_tree = "scan only root-dir or sub-dirs also"
        ```
        """
        # directory validation
        if not os.path.isdir(directory):
            raise ValueError("directory does not exist")

        # if directory doesn't have any files at all, error
        if not self.has_any_file(directory, whole_tree):
            raise FileNotFoundError(f"'{directory}' doesn't have any files.")

        if not "." in ext:
            raise ValueError("'ext' must be an extension [e.g '.txt']")

        # searching files
        if whole_tree:
            # scan the whole tree
            for root, dirs, files in os.walk(directory):
                for file in files:
                    # if file has 'ext' extension
                    if os.path.splitext(file)[-1] == ext:
                        # yield the file's path
                        yield os.path.join(root, file)

        else:
            # scan only root directory (no sub-dirs)
            with os.scandir(directory) as scanner:
                for entry in scanner:
                    if entry.is_file():
                        # if files has the 'ext' extension
                        if os.path.splitext(entry.name)[-1] == ext:
                            # yield file's path
                            yield entry.path

    def search_files_advanced(self, directory: str, ext: str, size_bounds: tuple, whole_tree=False):
        """
        ### Search Files (Advanced)
        Returns a Generator of the dictionaries of filepaths & sizes of all files found 
        with `ext` extension in `directory` within `size_bounds`

        ```
        # Parameters
        directory = "where to find the files, e.g 'C:\\Program Files'"
        ext = "what type of files to find, (e.g '.txt')"
        size_bounds = "Defines the size of files to find, (e.g ('2 kb', '10 mb'))"
        whole_tree = "scan only root-dir or sub-dirs also"
        ```
        """

        # directory validation
        if not os.path.isdir(directory):
            raise ValueError("'directory' does not exist")

        # if directory doesn't have any files at all, error
        if not self.has_any_file(directory, whole_tree):
            raise FileNotFoundError(f"'{directory}' doesn't have any files.")

        # extension validation
        if not "." in ext:
            raise ValueError("'ext' must be an extension [e.g '.txt']")

        # size_bounds validation
        if not len(size_bounds) == 2:
            raise ValueError("'_size_bound' must have 2 values")

        # Limits for min and max
        lower_limit = float(self._to_bytes(size_bounds[0]))
        upper_limit = float(self._to_bytes(size_bounds[1]))

        # * searching files
        if whole_tree:
            # scan the whole tree
            for root, dirs, files in os.walk(directory):
                for file in files:
                    # if file has 'ext' extension
                    if os.path.splitext(file)[-1] == ext:
                        file_path = os.path.join(root, file)
                        file_size = os.path.getsize(file_path)
                        # if filesize is under bounds, yield
                        if file_size >= lower_limit and file_size <= upper_limit:
                            # yield the file's path
                            yield {"path": file_path, "size": file_size}

        else:
            # scan only root directory (no sub-dirs)
            with os.scandir(directory) as scanner:
                for entry in scanner:
                    if entry.is_file():
                        # if files has the 'ext' extension
                        if os.path.splitext(entry.name)[-1] == ext:
                            file_size = os.path.getsize(entry.path)
                            if file_size >= lower_limit and file_size <= upper_limit:
                                # yield file's path
                                # yield (entry.path, file_size)
                                yield {"path": entry.path, "size": file_size}

    def extract_directories(self, directory: str, whole_tree=False):
        """
        ### Extract Directories
        Returns a generator of all the folder paths in `directory`
        """

        # directory validation
        if not os.path.isdir(directory):
            raise NotADirectoryError(f"'{directory}' is not a directory")

        # if directory doesn't have any files at all, error
        if not self.has_any_dir(directory, whole_tree):
            raise FileNotFoundError(
                f"'{directory}' doesn't have any directories.")

        if whole_tree:
            # scan sub-dirs also
            for root, dirs, files in os.walk(directory):
                yield root

        else:
            # scan root dir only
            with os.scandir(directory) as scanner:
                for entry in scanner:
                    if entry.is_dir():
                        yield entry.path

    def rename_file(self, filepath: str, name: str):
        """
        ### Rename a file
        Renames a `filepath` file to `name`.

        ```
        >> fm.rename_file(filepath="C:\\File.txt", name="Newfile.txt")
        # if 'Newfile.txt' does not already exists
        'C:\\Newfile.txt'

        # if it exists
        FileExistsError()
        ```
        """
        # filepath validation
        if not os.path.isfile(filepath):
            raise FileNotFoundError(f"'{filepath}' must lead to a file")

        # extract root and extension
        root = os.path.split(os.path.normpath(filepath))[0]

        # create new_name
        new_name = os.path.join(root, name)

        # if file already exists
        if os.path.isfile(new_name):
            raise FileExistsError(
                f"'{name}' already exists, cannot rename")

        # rename the file
        os.rename(filepath, new_name)

    def rename_directory(self, directory: str, name: str):
        """
        ### Rename a directory/folder
        Renames a `directory` to `name`

        ```
        >> fm.rename_directory(directory="C:\\folder", name="new folder")
        # if 'new folder' does not already exists
        'C:\\new folder'

        # if it exists
        FileExistsError()
        ```
        """
        # directory validation
        if not os.path.isdir(directory):
            raise NotADirectoryError("'directory' must be a directory path")

        # extract root
        root = os.path.split(os.path.normpath(directory))[0]
        # create new_name
        new_name = os.path.join(root, name)

        # directory validation
        if os.path.isdir(new_name):
            raise FileExistsError(f"'{name}' already exists")

        # rename directory
        os.rename(directory, new_name)

    def show_system_properties(self):
        """
        ### Show System Properties
        Returns a dictionary with as much system information as possible

        ```
        # returned dictionary keys
        dict_keys(
            [
                'time_of_report',
                'environment_variables',
                'architecture',
                'machine',
                'computer_name',
                'operating_sys',
                'os_name',
                'os_version',
                'processor',
                'num_of_processors',
                'username',
                'py_build',
                'py_compiler',
                'py_implementation',
                'py_version'
            ])
        ```
        """
        # holds extracted system info
        master = {}

        # get system info
        system_environments = os.environ
        master['time_of_report'] = time.ctime(time.time())
        master['environment_variables'] = system_environments
        master['architecture'] = pt.architecture()
        master['machine'] = pt.machine()
        master['computer_name'] = pt.node()
        master['operating_sys'] = pt.platform()
        master['os_name'] = pt.system()
        master['os_version'] = pt.version()
        master['processor'] = pt.processor()
        master['num_of_processors'] = system_environments["NUMBER_OF_PROCESSORS"]
        master['username'] = system_environments['USERNAME']
        master['py_build'] = pt.python_build()
        master['py_compiler'] = pt.python_compiler()
        master['py_implementation'] = pt.python_implementation()
        master['py_version'] = pt.python_version()

        # return the info dict
        return master

    def get_file_size(self, filepath: str, formatted=False):
        """
        ### Get File Size
        Returns the file size of `filepath`

        ```
        >> fm.get_file_size('C:\\File.txt', formatted=False)
        2248

        >> fm.get_file_size('C:\\File.txt', formatted=True)
        (2.2, 'KB', '2.2 KB')
        ```
        """

        # size of 'filepath' in bytes
        size = os.path.getsize(filepath)

        # returning decision ? formatted or not?
        if not formatted:
            return size

        # return formatted size otherwise
        return self._from_bytes(size)[-1]

    def show_file_properties(self, filepath: str):
        """
        ### Show Properties
        Returns a dictionary full of properties of `filepath` file

        ```
        # returned values
        dict_keys(
            [
                'path',
                'drive_letter',
                'name',
                'size',
                'extension',
                'creation',
                'modified',
                'accessed',
                # 'creation_in_seconds',
                # 'modified_in_seconds',
                # 'accessed_in_seconds'
        ])
        ```
        """

        # directory validation
        if not os.path.isfile(filepath):
            raise ValueError("'filepath' does not exist")

        # will hold every detail to be returned
        master = {}

        # *** START PROCESS
        # getting file info
        stats = os.stat(filepath)

        # extract info... from 'directory'
        f_root = os.path.split(os.path.normpath(filepath))[0]
        f_name = os.path.basename(os.path.normpath(filepath))
        f_extension = os.path.splitext(f_name)[-1]
        f_drive_letter = os.path.splitdrive(f_root)[0].replace(":", "")
        # extarcting info from 'stats'
        f_size = self._from_bytes(stats.st_size)[-1]
        f_creation_in_seconds = stats.st_ctime
        f_modified_in_seconds = stats.st_mtime
        f_accessed_in_seconds = stats.st_atime
        f_creation = time.ctime(stats.st_ctime)
        f_modified = time.ctime(stats.st_mtime)
        f_accessed = time.ctime(stats.st_atime)

        # Filling 'master' dictionary
        master['path'] = f_root
        master['drive_letter'] = f_drive_letter
        master['name'] = f_name
        master['size'] = f_size
        master['extension'] = f_extension
        master['creation'] = f_creation
        master['modified'] = f_modified
        master['accessed'] = f_accessed
        # master['creation_in_seconds'] = f_creation_in_seconds
        # master['modified_in_seconds'] = f_modified_in_seconds
        # master['accessed_in_seconds'] = f_accessed_in_seconds

        return master

    def show_directory_properties(self, directory: str):
        """
        ### Show Properties
        Returns a dictionary full of properties of `directory` such as size, date created, date modified etc.

        ```
        # returned values
        dict_keys(
            [
                'path',
                'drive_letter',
                'name',
                'size',
                'creation',
                'modified',
                'accessed'
                'files'
                'folders'
        ])
        ```
        """

        # directory validation
        if not os.path.exists(directory):
            raise ValueError("'directory' does not exist")

        # will hold every detail to be returned
        master = {}

        # *** START PROCESS
        # getting file info
        stats = os.stat(directory)

        # extract info... from 'directory'
        f_root = os.path.split(os.path.normpath(directory))[0]
        f_name = os.path.basename(os.path.normpath(directory))
        f_drive_letter = os.path.splitdrive(f_root)[0].replace(":", "")
        # extarcting info from 'stats'
        f_creation = time.ctime(stats.st_ctime)
        f_modified = time.ctime(stats.st_mtime)
        f_accessed = time.ctime(stats.st_atime)

        # finding folder size by finding each of its file's size
        size = 0
        file_count = 0

        for root, dirs, files in os.walk(directory):
            for file in files:
                size += os.path.getsize(os.path.join(root, file))
                file_count += 1

        f_size = self._from_bytes(size)

        # Filling 'master' dictionary
        master['path'] = f_root
        master['drive_letter'] = f_drive_letter
        master['name'] = f_name
        master['size'] = f_size[-1]
        master['creation'] = f_creation
        master['modified'] = f_modified
        master['accessed'] = f_accessed
        master['files'] = file_count
        master['folders'] = self.find_number_of_dirs(directory, whole_tree=True)

        return master

    def show_all_files(self, directory: str, whole_tree=False):
        """
        ### Show All Files
        Returns a generator containing tuples of path & size of each files found in `directory`
        """

        # directory validation
        if not os.path.isdir(directory):
            raise FileNotFoundError(
                f"'{directory}' is not an exisiting directory.")

        # if directory doesn't have any files at all, error
        if not self.has_any_file(directory, whole_tree):
            raise FileNotFoundError(f"'{directory}' doesn't have any files.")

        if whole_tree:
            # scan subdirs also
            for root, dirs, files in os.walk(directory):
                for file in files:
                    # find path & size
                    path = os.path.join(root, file)
                    size = self.get_file_size(path, formatted=True)
                    yield (path, size)

        else:
            # scan only root dir
            with os.scandir(directory) as scanner:
                for entry in scanner:
                    if entry.is_file():
                        size = self.get_file_size(entry.path, formatted=True)
                        yield (entry.path, size)

    def find_largest_file(self, directory: str, whole_tree=False):
        """
        ### Find Largest File
        Returns a tuple containing path & size of the largest file in `directory`
        """
        # directory validation
        if not os.path.isdir(directory):
            raise FileNotFoundError(
                f"'{directory}' is not an existing directory.")

        largest_file_size = 0
        largest_file_path = ''

        if whole_tree:
            # scan sub-dirs
            for root, dirs, files in os.walk(directory):
                for file in files:
                    path = os.path.join(root, file)
                    size = self.get_file_size(path)
                    if size > largest_file_size:
                        largest_file_size = size
                        largest_file_path = path

            # return the largest file
            return (largest_file_path, self._from_bytes(largest_file_size)[-1])

        else:
            # scan only root dir
            with os.scandir(directory) as scanner:
                for entry in scanner:
                    if entry.is_file():
                        size = self.get_file_size(entry.path)
                        if size > largest_file_size:
                            largest_file_size = size
                            largest_file_path = entry.path

                # return the largest file
                return (largest_file_path, self._from_bytes(largest_file_size)[-1])

    def find_smallest_file(self, directory: str, whole_tree=False):
        """
        ### Find Smallest File
        Returns a tuple containing path & size of the smallest file in `directory`
        """
        # directory validation
        if not os.path.isdir(directory):
            raise FileNotFoundError(
                f"'{directory}' is not an existing directory.")

        smallest_file_size = 9895604649984  # == 9 TB
        smallest_file_path = ''

        if whole_tree:
            # scan sub-dirs
            for root, dirs, files in os.walk(directory):
                for file in files:
                    path = os.path.join(root, file)
                    size = self.get_file_size(path)

                    # if found '0 bytes' file
                    if size == 0:
                        smallest_file_size = size
                        smallest_file_path = path
                        break

                    # if found file with size less than stored
                    if size < smallest_file_size:
                        smallest_file_size = size
                        smallest_file_path = path

            # return the smallest file
            return (smallest_file_path, self._from_bytes(smallest_file_size)[-1])

        else:
            # scan only root dir
            with os.scandir(directory) as scanner:
                for entry in scanner:
                    if entry.is_file():
                        size = self.get_file_size(entry.path)

                        # if found '0 bytes' file
                        if size == 0:
                            smallest_file_size = size
                            smallest_file_path = entry.path
                            break

                        # if found a file with size less than stored
                        if size < smallest_file_size:
                            smallest_file_size = size
                            smallest_file_path = entry.path

                # return the largest file
                return (smallest_file_path, self._from_bytes(smallest_file_size)[-1])

    def find_number_of_files(self, directory: str, whole_tree=False):
        """
        ### Find Number of files
        as name suggests, it finds the number of total files in a `directory`.
        """
        # directory validation
        if not os.path.isdir(directory):
            raise NotADirectoryError(
                f"'{directory}' is not an existing directory.")

        file_count = 0

        if whole_tree:
            # scan whole tree
            for root, dirs, files in os.walk(directory):
                for _ in files:
                    file_count += 1

        else:
            # scan root only
            with os.scandir(directory) as scanner:
                for entry in scanner:
                    if entry.is_file():
                        file_count += 1

        # return
        return file_count

    def find_number_of_dirs(self, directory: str, whole_tree=False):
        """
        ### Find Number of dirs
        as name suggests, it finds the number of total folders in a `directory`.
        """
        # directory validation
        if not os.path.isdir(directory):
            raise NotADirectoryError(
                f"'{directory}' is not an existing directory.")

        dir_count = 0

        if whole_tree:
            # scan whole tree
            for root, dirs, files in os.walk(directory):
                for _ in dirs:
                    dir_count += 1

        else:
            # scan root only
            with os.scandir(directory) as scanner:
                for entry in scanner:
                    if entry.is_dir():
                        dir_count += 1

        # return
        return dir_count

    def _from_bytes(self, _bytes: int):
        """
        ### Bytes Converter
        Converts `bytes` to other data storage units

        ```
        >> fm._from_bytes(1024)
        (1.0, 'KB', '1.0 KB')

        >> fm._from_bytes(104815200)
        (99.95, 'MB', '99.95 MB')
        ```
        """

        # ? if _bytes is zero, Return
        if _bytes == 0:
            # if size is zero
            return (0.0, 'B', '0.0 B')

        # will hold return values
        master = {}

        # Unit Factors
        factors = {
            "B": 1,
            "KB": 1024,
            "MB": 1024 ** 2,
            "GB": 1024 ** 3,
            "TB": 1024 ** 4,
            "PB": 1024 ** 5
        }

        # ? one by one calculates each fact in factors
        for fact in factors.keys():
            # calculate bytes into new unit (kb or mb or other)
            new_unit = round(_bytes / factors[fact], 2)

            # if bewteen 1-1024, return it
            if int(new_unit) in range(1, 1024):
                # returning values in (tuple)
                return (new_unit, fact, f"{new_unit} {fact}")

    def _to_bytes(self, _size: str):
        """
        ### To Bytes
        Converts other Data Storage units to bytes

        ```
        >> fm._to_bytes(_size="5 kb")
        5120

        >> fm._to_bytes(_size="5 mb")
        5242880
        ```
        """
        # extract values
        values = _size.strip().upper().split()
        size = int(values[0])
        unit = values[1]

        # size validation
        if size <= 0:
            return 0

        # unit validation
        if not (unit and unit.isalpha() and len(unit) in [1, 2]):
            raise ValueError(f"'{unit}' is not a valid unit")

        # ? Calculate bytes
        # Unit Factors
        factors = {
            "B": 1,
            "KB": 1024,
            "MB": 1024 ** 2,
            "GB": 1024 ** 3,
            "TB": 1024 ** 4,
            "PB": 1024 ** 5
        }

        # ? Calculate bytes
        return factors[unit] * size

    def has_any_file(self, directory: str, whole_tree=False) -> bool:
        """
        ### Has any file
        just like name suggests, it checks whether or not the `directory` has any files.
        """
        # directory validation
        if not os.path.isdir(directory):
            raise FileNotFoundError(
                f"'{directory}' is not an existing directory.")

        if whole_tree:
            #  scan whole tree
            for root, dirs, files in os.walk(directory):
                for file in files:
                    if os.path.isfile(os.path.join(root, file)):
                        return True
            return False

        else:
            # scan root only
            with os.scandir(directory) as scanner:
                for entry in scanner:
                    if entry.is_file():
                        return True
                return False

    def has_any_dir(self, directory: str, whole_tree=False) -> bool:
        """
        ### Has any dir
        just like name suggests, it checks whether or not the `directory` has any folders\dirs.
        """
        # directory validation
        if not os.path.isdir(directory):
            raise FileNotFoundError(
                f"'{directory}' is not an existing directory.")

        if whole_tree:
            #  scan whole tree
            for root, dirs, files in os.walk(directory):
                for d in dirs:
                    if os.path.isdir(os.path.join(root, d)):
                        return True
            return False

        else:
            # scan root only
            with os.scandir(directory) as scanner:
                for entry in scanner:
                    if entry.is_dir():
                        return True
                return False
