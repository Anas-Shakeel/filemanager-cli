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
> Type in the __number__ for the tool you want to user and press `enter`.
>```
> Choose an option: 24
>```
> After pressing `enter`, you would see a menu for that tool, just like below.
> ```
> ## File Size
> It shows file's size.
> 
> Enter path to a file:
> ```
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
> Press `enter` to go back to main menu
> 


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
- Search for Specific Files
- Rename Files
- Rename Directories
- Show File Properties
- Show Directory Properties
- Find file size
- List all files
- Find the largest file in a directory


## Libraries used in this project
`os` `shutil` `re` `sys` `platform` `time` `pyfiglet` ``


## Project's root directory
- `fm.py`
- `main.py`


## Overview of `fm.py`
This file is a custom module i wrote in python to fulfill my needs of creating a `Filemanager`

This module contains a __class__ called `FileManager` which contains __26 methods__. all of them are briefly explained below.

### Libraries / Modules used
> `os` <br>
> it was used heavily and mercilessly in this module. from simple operations of __splitting__ and __joining__ paths to some of more advanced ones.
>
> `shutil` <br>
> it was also used for some High-level file operations to copy/move files & directories, delete directories etc.
>
> `platform` <br>
> This module was used to get system related information.
>
> `time` <br>
> The only purpose of this module was to convert seconds into more human readable dates, That's it.
>
### Methods
>
> #### 1. `folder_bomb(directory, name)` <br>
> This method upon call, creates __hundreds or even thousands__ of empty folders _per second_ as long as the program is running. Although, `ctrl+c` can stop the process.
> > 
> > #### Parameters:
> > `directory : str`
> > Address of the folder/directory in which to create the folders.
> >
> > `name : str`
> > Base name of the folders to create, wil automatically be incremented.
> >
> #### 2. `create_folder(directory, name)` <br>
> This method creates a __folder__ in given __directory__. If a folder of given name already exists in the given directory, it currently throws a `FileExistsError()`.
> > #### Parameters:
> > `directory : str`
> > Address of the folder/directory in which to create the folder.
> >
> > `name : str`
> > Base name of the folders to create.
> >
> >
> #### 3. `create_folders(directory, n, name)` <br>
> This method creates `n` folders in given __directory__. If a folder of given name already exists in the given directory, it currently just skips the name and moves to next.
> > #### Parameters:
> > `directory : str`
> > Address of the folder/directory in which to create the folders.
> >
> > `n : int`
> > Address of the folder/directory in which to create the folder.
> >
> > `name : str`
> > Base name of the folders to create. names will automatically be incremented.
> >





---
## Author : Anas Shakeel