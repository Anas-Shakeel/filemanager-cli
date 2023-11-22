# File Manager

## Note:

I am currently working on this `README.md` file...

## Description:

`File manager` is written specifically for Windows in python.<br>
It features high level file management tools such as copying, moving, pasting or deleting files and many more.<br>

## Installation:

1. Install latest [Python](https://www.python.org/download)
2. Download the code from github to your local machine (PC / Laptop).
3. Extract the `.zip` file
4. Run `main.py` from terminal or just double click it!

## How to use:

After running `main.py`, you'll see something like this:

> ```
> Welcome to
> ____ _ _    ____    _  _ ____ _  _ ____ ____ ____ ____
> |___ | |    |___    |\/| |__| |\ | |__| | __ |___ |__/
> |    | |___ |___    |  | |  | | \| |  | |__] |___ |  \
>
>
> #######################
> Written by Anas Shakeel
> #######################
>
> ## Main Menu
>
> [ 1]. Folder Bomb
> [ 2]. Create Folder
> [ 3]. Create Folders
> [ 4]. Copy File
> [ 5]. Copy Specific Files
> [ 6]. Copy All Files
> [ 7]. Copy Directory
> [ 8]. Move File
> [ 9]. Move Specific Files
> [10]. Move All Files
> [11]. Move Directory
> [12]. Delete File
> [13]. Delete Specific Files
> [14]. Delete All Files
> [15]. Delete Directory
> [16]. Delete Empty Folder
> [17]. Rename File
> [18]. Rename Directory
> [19]. Search Files
> [20]. Search Files (Advanced)
> [21]. Extract Directories
> [22]. Show File Properties
> [23]. Show Directory Properties
> [24]. Show File Size
> [25]. Show All Files
> [26]. Find Largest File
> [27]. Close the Program
>
> Choose an option:
> ```
>
> Type in the **number** for the tool you want to use and press `enter`.
>
> ```
> Choose an option: 24
> ```
>
> After pressing `enter` you would see a menu for that tool, just like below.
>
> ```
> ## File Size
> It shows file's size.
>
> Enter path to a file:
> ```
>
> Read the prompts and follow, you'll be just fine!
>
> ```
> ## File Size
> It shows file's size.
>
> Enter path to a file: E:\folder\file.txt
>
> File size of 'file.txt': 5.11 KB
>
> Press any key to continue...
>
> ```
>
> Press `enter` to go back to main menu
>
> #### You can use the rest of the program similarly.
>
> 1. Select the tool from menu.
> 2. Read and follow some prompts.
> 3. Press `enter` to go back to he menu.
> 4. **Repeat**.

## Features:

What this program offers?

- Create Infinite Empty Folders
- Create Directories
- Copy Files
- Copy Directories
- Move Files
- Move Directories
- Delete Files
- Delete Directories
- Delete Empty Folders
- Search Files
- Rename Files
- Rename Directories
- Show File Properties
- Show Directory Properties
- Find file size
- Show all files
- Find the largest or smallest file in a directory

## Libraries used in this project

`os` `shutil` `re` `sys` `platform` `time` `pyfiglet`

## Project's root directory

- `fm.py`
- `main.py`
- `README.md`
- `LICENSE`

## Overview of `main.py`

This is the entry-point of the program.<br>
Sort of a front-end that the users or you might see.

This file contains code related to the command-line user interface. So there's no point explaining this file.

### Libraries / Modules used

`os` `pyfiglet` `time` `re` `sys` `fm`

## Overview of `fm.py`

This file is a custom module i wrote in python for the High-level file operations. <br>
This file serves as a backend for the `main.py` file.

This module contains a **class** called `FileManager` which contains **36 methods**. all of them are briefly explained below.

### Libraries / Modules used

`os` `shutil` `platform` `time`

### Methods

> #### 1. `folder_bomb(directory, name)` <br>
>
> This method creates empty folders in `directory` infinitely until user
> stops the program `(ctrl+c)`.
>
> Be careful with this one as it will silently keep creating thousands of folders per second upon call.
>
> Be sure to somehow tell the users that they can press `ctrl+c` to break this loop.
>
> #### 2. `create_folder(directory, name)` <br>
>
> This method creates a **folder** in `directory`. If a folder of `name` already exists in the given directory, it throws a `FileExistsError()`.
>
> #### 3. `create_folders(directory, n, name)` <br>
>
> This method creates `n` folders in `directory`. If a folder of `name` already exists in the given directory, it just skips the name and moves to next.<br>
> This method also handles the filename increments.
>
> #### 4. `copy_file(src, dst)` <br>
>
> This method copies a file from `src` to `dst` <br>
> if `src` file already exists in `dst`, a new file will be created with the same name with increments.
>
> #### 5. `copy_files(src, dst, ext, whole_tree)` <br>
>
> This method copies all files of extension `ext` from `src` to `dst`. <br>
> if `src` file already exists in `dst`, a new file will be created with the same name with increments. <br>
> If `whole_tree` is set to `True`, it will also look into sub folders for `ext` files to copy. otherwise it only copies the said files from `directory`.
>
> #### 6. `copy_all_file(src, dst, whole_tree)` <br>
>
> This method copies all files from `src` to `dst`. <br>
> if `src` file already exists in `dst`, a new file will be created with the same name with increments.
> If `whole_tree` is set to `True`, it will also copy all files from sub folders. otherwise it only copies files from `directory`.
>
> #### 7. `copy_directory(src, dst)` <br>
>
> This method copies a whole directory `src` to `dst`. <br>
> if `src` already exists in `dst`, folder's name will be incremented.
>
> #### 8. `delete_file(filepath)` <br>
>
> This method permanently deletes `filepath` file. <br>
>
> #### 9. `delete_files(directory, ext, whole_tree)` <br>
>
> This method searches for all `ext` files in `directory` and permanently deletes them. <br>
> If `whole_tree` is set to `True`, it will search and delete the said files from sub folders too.
>
>
> #### 10. `delete_all_files(directory, whole_tree)` <br>
>
> This method deletes all files in `directory`. <br>
> If `whole_tree` is set to `True`, it will delete all files from sub folders too.
>
>
> #### 11. `delete_directory(directory)` <br>
>
> This method permanently deletes `directory` folder. <br>
>
>
> #### 12. `delete_empty_folders(directory, whole_tree)` <br>
>
> This method permanently deletes all empty folders in `directory`. <br>
> If `whole_tree` is set to `True`, it deletes empty folders from the sub folders too.
>
>
> #### 13. `filename_increment(filepath, dst_path)` <br>
>
> This method adds an incremented number in the `filepath` if file already exists in `dst_path` and returns the name. <br>
> if `dst_path` is omitted, method will use the `filepath`'s directory to look if filename exists not.
>
>
> #### 14. `foldername_increment(folderpath, dst_path)` <br>
>
> This method adds an incremented number in the `folderpath` if folder already exists in `dst_path` and returns the name. <br>
> if `dst_path` is omitted, method will use the `folderpath`'s directory to look if foldername exists not. <br>
> These methods are helper methods that this class uses.
>
>
> #### 15. `move_file(src, dst)` <br>
>
> This method moves a file from `src` to `dst` <br>
> if `src` file already exists in `dst`, this method will increment the file's name and move it there.
>
> #### 16. `move_files(src, dst, ext, whole_tree)` <br>
>
> This method moves all files of extension `ext` from `src` to `dst`. <br>
> if `src` file already exists in `dst`, this method will increment the file's name and move it there. <br>
> If `whole_tree` is set to `True`, it will also look into sub folders for `ext` files to move. otherwise it only moves the said files from `directory`.
>
> #### 17. `move_all_file(src, dst, whole_tree)` <br>
>
> This method moves all files from `src` to `dst`. <br>
> if `src` file already exists in `dst`, this method will increment the file's name and move it there.
> If `whole_tree` is set to `True`, it will also move all files from sub folders. otherwise it only moves files from `directory`.
>
> #### 18. `move_directory(src, dst)` <br>
>
> This method moves a whole directory `src` to `dst`. <br>
> if `src` already exists in `dst`, folder's name will be incremented.
>
>
> #### 19. `search_files(directory, ext, whole_tree)` <br>
>
> This method searches for `ext` files in `directory`. <br>
> if `whole_tree` is set to `True`, it also searches in the sub folders. <br>
> It returns a generator of all found filepaths.
>
> #### 20. `search_files_advanced(directory, ext, size_bounds, whole_tree)` <br>
>
> This method searches for `ext` files that are in `size_bounds` in `directory`. <br>
> `size_bounds` is a tuple used to set lower & upper boundaries for a certain size. this tuple expects two values `size_bounds=(min, max)`. min is used to set a minimum size limit and max for the upper limit.<br>
> if `whole_tree` is set to `True`, it also searches in the sub folders. <br>
> It returns a generator of dictionaries. each dictionary has two keys __'size'__ and __'path'__.
>

---

## Author : `Anas Shakeel`
