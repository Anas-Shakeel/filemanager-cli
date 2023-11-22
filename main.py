import sys
import re
from os import path
from os import system
from time import sleep
from pyfiglet import Figlet
from fm import FileManager


def main():
    # color commands (cmd)
    colors = {
        "default": "color 07",
        "green": "color 0a",
        "green_dark": "color 02",
        "gray": "color 08",
        "blue": "color 09",
        "aqua": "color 03",
        "red": "color 04",
        "yellow": "color 06",
    }

    # * Setting up the terminal
    system("cls")
    system("title File Manager written by Anas Shakeel")

    try:
        # * Welcome Screen
        system(colors['green'])
        figlet = Figlet()
        figlet.setFont(font="cybermedium")
        print("Welcome to\n", figlet.renderText("File Manager"), sep="")
        print("#######################", "\nWritten by Anas Shakeel\n",
              "#######################\n", sep="")
        sleep(3)

        # ? Starting the Program
        # Creating menu
        menu = [
            "Folder Bomb",
            "Create Folder",
            "Create Folders",
            "Copy File",
            "Copy Specific Files",
            "Copy All Files",
            "Copy Directory",
            "Move File",
            "Move Specific Files",
            "Move All Files",
            "Move Directory",
            "Delete File",
            "Delete Specific Files",
            "Delete All Files",
            "Delete Directory",
            "Delete Empty Folder",
            "Rename File",
            "Rename Directory",
            "Search Files",
            "Search Files (Advanced)",
            "Extract Directories",
            "Show File Properties",
            "Show Directory Properties",
            "Show File Size",
            "Show All Files",
            "Find Largest File",
            "Find Smallest File",
            "Close the Program",
        ]

        f = FileManager()

        while True:
            system(colors['green'])
            print("## Main Menu\n")
            # Showing Main Menu
            for index, item in enumerate(menu):
                print(f"[{index+1:>2}]. {item}")
                sleep(0.01)

            # get user choice
            option = get_int("\nChoose an option: ", 1, len(menu))

            match option:
                # * Folder Bomb
                case 1:
                    system("cls")
                    system(colors['red'])

                    # tool's description
                    print(
                        "## Folder Bomb\nIt keeps creating empty folders until stopped explicitly!")

                    directory = get_directory("\nEnter path to a directory: ")
                    folders_name = input("Enter base folder name: ")
                    if confirm(f"\n[Warning] this will bomb '{directory}' with empty folders."):
                        system("cls")
                        print(
                            f"[Info] Folders are being created in '{directory}'...\nctrl+c to stop")
                        try:
                            f.folder_bomb(directory, folders_name)
                        except KeyboardInterrupt:
                            print("[Info] Bombing Stopped...")
                            waitforkey()

                    else:
                        system("cls")

                # * Create Folder
                case 2:
                    system("cls")

                    # tool's description
                    print(
                        "## Create a Folder\nIt creates an empty folder in a directory.")

                    directory = get_directory("\nEnter path to a directory: ")
                    folder_name = input("Enter folder name: ")
                    if confirm(f"\n[Warning] this will create a folder named '{folder_name}' in '{directory}'"):
                        try:
                            f.create_folder(directory, folder_name)
                            print(
                                f"[Info] '{folder_name}' has been created successfully.")

                        except FileExistsError:
                            print(f"\n[Error] '{folder_name}' already exists in '{directory}'...")

                        waitforkey()

                    else:
                        system("cls")

                # * Create Folders
                case 3:
                    system("cls")

                    # tool's description
                    print(
                        "## Create multiple Folders\nIt creates 'n' empty folders in a directory.")

                    directory = get_directory("\nEnter path to a directory: ")
                    folder_name = input("Enter base folder name: ")
                    count = get_int(
                        "How many folders to create (LIMIT: 1000000): ", min=0, max=1000000)
                    if confirm(f"\n[Warning] this will create {count} folders in '{directory}'"):
                        try:
                            f.create_folders(directory, folder_name, count)
                            print(
                                f"[Info] '{count}' folders have been created successfully in '{directory}'")

                        except ValueError:
                            print(f"[Error] '{directory}' does not exists!")

                        waitforkey()
                    else:
                        system("cls")

                # * Copy File
                case 4:
                    system("cls")

                    # tool's description
                    print(
                        "## Copy a file\nIt copies a file from one place to another.")

                    src = get_file(
                        "\nEnter path to a file to be copied: ")
                    dst = get_directory("Enter path to a destination: ")
                    if confirm(f"\n[Warning] this will copy '{src}' to '{dst}'"):
                        # copy file
                        f.copy_file(src, dst)
                        print(
                            f"[Info] '{src}' has been copied successfully to '{dst}'")
                        waitforkey()
                    else:
                        system("cls")

                # * Copy Specific Files
                case 5:
                    system("cls")

                    # tool's description
                    print(
                        "## Copy specific files\nIt copies files with same extension from one place to another.")

                    src = get_directory(
                        "\nEnter path to a directory of files: ")
                    ext = get_extension("Enter extension of files to copy: ")
                    dst = get_directory("Enter path to a destination: ")
                    whole_tree = get_bool("Copy files from sub-dirs also?")

                    if confirm(f"\n[Warning] this will copy all '{ext}' files from '{src}' to '{dst}'"):
                        # copy file
                        f.copy_files(src, dst, ext, whole_tree)
                        print(
                            f"[Info] all '{ext}' files have been copied successfully to '{dst}'")
                        waitforkey()
                    else:
                        system("cls")

                # * Copy All Files
                case 6:
                    system("cls")

                    # tool's description
                    print(
                        "## Copy all files\nIt copies all files from one place to another.")

                    src = get_directory(
                        "\nEnter path to a directory of files: ")
                    dst = get_directory("Enter path to a destination: ")
                    whole_tree = get_bool("Copy files from sub-dirs also?")

                    if confirm(f"\n[Warning] this will copy all files from '{src}' to '{dst}'"):
                        # copy file
                        f.copy_all_files(src, dst, whole_tree)
                        print(
                            f"[Info] all files from '{src}' have been copied successfully to '{dst}'")
                        waitforkey()
                    else:
                        system("cls")

                # * Copy Directory
                case 7:
                    system("cls")

                    # tool's description
                    print(
                        "## Copy a folder\nIt copies a folder from one place to another.")

                    src = get_directory(
                        "\nEnter path to a folder: ")
                    dst = get_directory("Enter path to a destination: ")

                    if confirm(f"\n[Warning] this will copy '{src}' to '{dst}'"):
                        # copy folder
                        f.copy_directory(src, dst)
                        print(
                            f"[Info] '{src}' has been copied successfully to '{dst}'")
                        waitforkey
                    else:
                        system("cls")

                # * Move File
                case 8:
                    system("cls")

                    # tool's description
                    print(
                        "## Move a file\nIt moves a file from one place to another.")

                    src = get_file(
                        "\nEnter path to a file to be moved: ")
                    dst = get_directory("Enter path to a destination: ")
                    if confirm(f"\n[Warning] this will move '{src}' to '{dst}'"):
                        # move file
                        f.move_file(src, dst)
                        print(
                            f"[Info] '{src}' have been moved successfully to '{dst}'")
                        waitforkey()
                    else:
                        system("cls")

                # * Move Specific Files
                case 9:
                    system("cls")

                    # tool's description
                    print(
                        "## Move specific files\nIt moves files with same extension from one place to another.")

                    src = get_directory(
                        "\nEnter path to a directory of files: ")
                    ext = get_extension("Enter extension of files to move: ")
                    dst = get_directory("Enter path to a destination: ")
                    whole_tree = get_bool("Move files from sub-dirs also?")

                    if confirm(f"\n[Warning] this will move all '{ext}' files from '{src}' to '{dst}'"):
                        # move specific files
                        f.move_files(src, dst, ext, whole_tree)
                        print(
                            f"[Info] all '{ext}' files have beem moved successfully from '{src}' to '{dst}'")
                        waitforkey()
                    else:
                        system("cls")

                # *  Move All Files
                case 10:
                    system("cls")

                    # tool's description
                    print(
                        "## Move all files\nIt moves all files from one place to another.")

                    src = get_directory(
                        "\nEnter path to a directory of files: ")
                    dst = get_directory("Enter path to a destination: ")
                    whole_tree = get_bool("Move files from sub-dirs also?")

                    if confirm(f"\n[Warning] this will move all files from '{src}' to '{dst}'"):
                        # move all files
                        f.move_all_files(src, dst, whole_tree)
                        print(
                            f"[Info] all files from '{src}' have been moved successfully to '{dst}'")
                        waitforkey()
                    else:
                        system("cls")

                # *  Move Directory
                case 11:
                    system("cls")

                    # tool's description
                    print(
                        "## Move a folder\nIt moves a folder from one place to another.")

                    src = get_directory(
                        "\nEnter path to a folder: ")
                    dst = get_directory("Enter path to a destination: ")

                    if confirm(f"\n[Warning] this will move '{src}' to '{dst}'"):
                        # move folder
                        f.move_directory(src, dst)
                        print(
                            f"[Info] '{src}' has been moved successfully to '{dst}'")
                        waitforkey()
                    else:
                        system("cls")

                # *  Delete File
                case 12:
                    system("cls")

                    # tool's description
                    print(
                        "## Delete a file\nIt permanently deletes a file.")

                    src = get_file(
                        "\nEnter path to a file to be deleted: ")
                    if confirm(f"\n[Warning] this will delete '{src}'"):
                        # delete file
                        f.delete_file(src)
                        print(
                            f"[Info] '{src}' has been deleted successfully!")
                        waitforkey()
                    else:
                        system("cls")

                # *  Delete Specific Files
                case 13:
                    system("cls")

                    # tool's description
                    print(
                        "## Delete specific files\nIt permanently deletes files with same extension.")

                    src = get_directory(
                        "\nEnter path to a directory of files to be deleted: ")
                    ext = get_extension("Enter extension of files to delete: ")
                    whole_tree = get_bool("Delete files from sub-dirs also?")

                    if confirm(f"\n[Warning] this will delete all '{ext}' files from '{src}'"):
                        # delete specific files
                        f.delete_files(src, ext, whole_tree)
                        print(
                            f"[Info] all '{ext}' files from '{src}' have been deleted successfully!")
                        waitforkey()
                    else:
                        system("cls")

                # *  Delete All Files
                case 14:
                    system("cls")

                    # tool's description
                    print(
                        "## Delete all files\nIt permanently deletes all files from a directory.")

                    src = get_directory(
                        "\nEnter path to a directory of files to be deleted: ")
                    whole_tree = get_bool("Delete files from sub-dirs also?")

                    if confirm(f"\n[Warning] this will delete all files from '{src}'"):
                        # delete all files
                        f.delete_all_files(src, whole_tree)
                        print(
                            f"[Info] all files from '{src}' have been deleted successfully!")
                        waitforkey()
                    else:
                        system("cls")

                # *  Delete Directory
                case 15:
                    system("cls")

                    # tool's description
                    print(
                        "## Delete a folder\nIt permanently deletes a directory.")

                    src = get_directory(
                        "\nEnter path to a directory to be deleted: ")

                    if confirm(f"\n[Warning] this will delete '{src}'"):
                        # delete all files
                        f.delete_directory(src)
                        print(
                            f"[Info] '{src}' has been deleted successfully.")
                        waitforkey()
                    else:
                        system("cls")

                # *  Delete Empty Folder
                case 16:
                    system("cls")

                    # tool's description
                    print(
                        "## Delete empty folders\nIt permanently deletes all empty folders from a directory.")

                    src = get_directory(
                        "\nEnter path to a directory to clean: ")
                    whole_tree = get_bool(
                        "Delete empty folders from sub-dirs also?")

                    if confirm(f"\n[Warning] this will delete all empty folders from '{src}'"):
                        print(f"[Info] cleaning '{src}'...")
                        # delete empty folders
                        f.delete_empty_folders(src, whole_tree)
                        print(
                            f"[Info] '{src}' have been cleaned successfully.")
                        waitforkey()
                    else:
                        system("cls")

                # *  Rename File
                case 17:
                    system("cls")

                    # tool's description
                    print(
                        "## Rename a file\nIt renames a file, pretty much self-explanatory.")

                    src = get_file(
                        "\nEnter path to a file to rename: ")

                    name = input("Enter new name (with same extension): ")
                    
                    split_path = path.split(path.normpath(src))

                    if confirm(f"\n[Warning] this will rename '{split_path[-1]}' to '{name}'"):
                        try:
                            # Rename file
                            f.rename_file(src, name)
                            print(
                                f"[Info] '{split_path[-1]}' has been renamed to '{name}' successfully!")
                        except FileExistsError:
                            print(
                                f"[Error] '{name}' already exists in '{split_path[0]}'")
                        waitforkey()
                    else:
                        system("cls")

                # *  Rename Directory
                case 18:
                    system("cls")

                    # tool's description
                    print(
                        "## Rename a folder\nIt renames a folder, pretty much self-explanatory.")

                    src = get_directory(
                        "\nEnter path to a folder to rename: ")

                    name = input("Enter new name: ")

                    # split the path
                    split_path = path.split(path.normpath(src))

                    if confirm(f"\n[Warning] this will rename '{split_path[1]}' to '{name}'"):
                        try:
                            # Rename folder
                            f.rename_directory(src, name)
                            print(
                                f"[Info] '{split_path[1]}' has been renamed to '{name}' successfully!")
                        except FileExistsError:
                            print(
                                f"\n[Error] '{name}' already exists in '{split_path[0]}'")
                        waitforkey()
                    else:
                        system("cls")

                # *  Search Files
                case 19:
                    system("cls")

                    # tool's description
                    print(
                        "## Search files\nIt searches all files with the same extension in a directory and outputs them.")

                    src = get_directory(
                        "\nEnter path to a directory to search: ")
                    ext = get_extension("Enter extension of files to search: ")
                    whole_tree = get_bool("Search sub-dirs also?")

                    output = get_bool(
                        "Output to (text file [y]) OR (print here [n])")

                    # search file data
                    data = f.search_files(src, ext, whole_tree)

                    try:
                        if output:
                            # Export to text file
                            fname = input("Enter output filename: ") + ".txt"
                            if path.isfile(fname):
                                filename = f.filename_increment(fname, ".")
                            else:
                                filename = fname

                            print(
                                f"[Info] data is being written to '{filename}', please wait!")
                            with open(filename, "w") as outputfile:
                                # Search files
                                for line in data:
                                    try:
                                        outputfile.write(f"{line}\n")
                                    except UnicodeEncodeError:
                                        pass

                            print(
                                f"\n[Info] data have been exported successfully to '{filename}'")

                        else:
                            print("\n[Info] listing searched files...")
                            # print files
                            for line in data:
                                print(line)

                    except FileNotFoundError:
                        print("[Info] there are no files...")

                    waitforkey()

                # *  Search Files (Advanced)
                case 20:
                    system("cls")

                    # tool's description
                    print(
                        "## Search files (ADVANCED)\nIt searches all files with the same extension and within a size bound in a directory and outputs them.")

                    src = get_directory(
                        "\nEnter path to a directory to search: ")
                    ext = get_extension("Enter extension of files to search: ")
                    whole_tree = get_bool("Search sub-dirs also?")
                    min_limit = get_size_bounds(
                        "Enter minimum size of a file (e.g 2 mb): ")
                    max_limit = get_size_bounds(
                        "Enter maximum size of a file (e.g 2 mb): ")

                    output = get_bool(
                        "Output to (text file [y]) OR (print here [n])")

                    # search file data
                    data = f.search_files_advanced(
                        src, ext, (min_limit, max_limit), whole_tree)

                    try:
                        if output:
                            # Export to text file
                            fname = input("Enter output filename: ") + ".txt"
                            if path.isfile(fname):
                                filename = f.filename_increment(fname, ".")
                            else:
                                filename = fname

                            print(
                                f"[Info] data is being written to '{filename}', please wait!")
                            with open(filename, "w") as outputfile:
                                # Search files
                                for line in data:
                                    try:
                                        outputfile.write(
                                            f"({f._from_bytes(line['size'])[-1]}), {line['path']}\n")
                                    except UnicodeEncodeError:
                                        pass

                            print(
                                f"\n[Info] data have been exported successfully to '{filename}'")

                        else:
                            print("\n[Info] listing searched files...")
                            # print files
                            for line in data:
                                print(
                                    f"({f._from_bytes(line['size'])[-1]}), {line['path']}")
                    except FileNotFoundError:
                        print("[Info] there are no files...")

                    waitforkey()

                # *  Extract Directories
                case 21:
                    system("cls")

                    # tool's description
                    print(
                        "## Extract Directories\nIt searches all folders in a directory and outputs their path.")

                    src = get_directory(
                        "\nEnter path to a directory to search: ")
                    whole_tree = get_bool("Search sub-dirs also?")

                    output = get_bool(
                        "Output to (text file [y]) OR (print here [n])")

                    # extract folders data
                    data = f.extract_directories(src, whole_tree)

                    try:
                        if output:
                            # Export to text file
                            fname = input("Enter output filename: ") + ".txt"
                            if path.isfile(fname):
                                filename = f.filename_increment(fname, ".")
                            else:
                                filename = fname

                            print(
                                f"[Info] Data is being written to '{filename}', please wait!")
                            with open(filename, "w") as outputfile:
                                # Search files
                                for line in data:
                                    try:
                                        outputfile.write(f"{line}\n")
                                    except UnicodeEncodeError:
                                        pass

                            print(
                                f"\n[Info] Data have been exported successfully to '{filename}'")

                        else:
                            print(f"\n[Info] listing folders in '{src}'")
                            # print files
                            for line in data:
                                print(line)

                    except FileNotFoundError:
                        print("[Info] there are no folders...")

                    waitforkey()

                # *  Show File Properties
                case 22:
                    system("cls")

                    # tool's description
                    print(
                        "## File Properties\nIt extracts file properties and outputs.")

                    src = get_file("\nEnter path to a file: ")
                    output = get_bool(
                        "Output to (text file [y]) OR (print here [n])")

                    # extract folders data
                    data = f.show_file_properties(src)

                    if output:
                        # Export to text file
                        fname = input("Enter output filename: ") + ".txt"
                        if path.isfile(fname):
                            filename = f.filename_increment(fname, ".")
                        else:
                            filename = fname

                        print(
                            f"[Info] Data is being written to '{filename}', please wait!")
                        with open(filename, "w") as outputfile:
                            # writing data
                            for key in data.keys():
                                outputfile.write(
                                    f"{key.replace('_', ' ').capitalize()}: '{data[key]}'\n")

                        print(
                            f"\n[Info] Data have been exported successfully to '{filename}'")

                    else:
                        print(f"\n[Info] showing Properties for '{src}'...")
                        # printing data
                        for key in data.keys():
                            print(
                                f"{key.replace('_', ' ').capitalize()}: '{data[key]}'")
                            sleep(0.01)

                    waitforkey()

                # *  Show Directory Properties
                case 23:
                    system("cls")

                    # tool's description
                    print(
                        "## Folder Properties\nIt extracts folder properties and outputs.")

                    src = get_directory("\nEnter path to a folder: ")
                    output = get_bool(
                        "Output to (text file [y]) OR (print here [n])")

                    # extract folders data
                    data = f.show_directory_properties(src)

                    if output:
                        # Export to text file
                        fname = input("Enter output filename: ") + ".txt"
                        if path.isfile(fname):
                            filename = f.filename_increment(fname, ".")
                        else:
                            filename = fname

                        print(
                            f"[Info] Data is being written to '{filename}', please wait!")
                        with open(filename, "w") as outputfile:
                            # writing data
                            for key in data.keys():
                                outputfile.write(
                                    f"{key.replace('_', ' ').capitalize()}: '{data[key]}'\n")

                        print(
                            f"\n[Info] Data have been exported successfully to '{filename}'")

                    else:
                        print(f"\n[Info] showing Properties for '{src}'...")
                        # System properties
                        for key in data.keys():
                            print(
                                f"{key.replace('_', ' ').capitalize()}: '{data[key]}'")
                            sleep(0.01)

                    waitforkey()

                # *  Show File Size
                case 24:
                    system("cls")

                    # tool's description
                    print(
                        "## File Size\nIt shows file's size.")

                    src = get_file("\nEnter path to a file: ")

                    # extract folders data
                    filesize = f.get_file_size(src, formatted=True)

                    print(
                        f"\nFile size of '{path.basename(path.normpath(src))}': {filesize}")

                    waitforkey()

                # *  Show All Files
                case 25:
                    system("cls")

                    # tool's description
                    print(
                        "## Show All Files\nIt shows all files in a directory and outputs them.")

                    src = get_directory("\nEnter path to a folder: ")
                    whole_tree = get_bool("Search sub-dirs also?")
                    output = get_bool(
                        "Output to (text file [y]) OR (print here [n])")

                    # extract folders data
                    data = f.show_all_files(src, whole_tree)

                    try:
                        if output:
                            # Export to text file
                            fname = input("Enter output filename: ") + ".txt"
                            if path.isfile(fname):
                                filename = f.filename_increment(fname, ".")
                            else:
                                filename = fname

                            print(
                                f"[Info] Data is being written to '{filename}', please wait!")
                            with open(filename, "w") as outputfile:
                                # System properties
                                for item in data:
                                    outputfile.write(
                                        f"{item[1]} - {item[0]}\n")

                            print(
                                f"\n[Info] Data have been exported successfully to '{filename}'")

                        else:
                            print("\n[Info] listing searched files...")
                            # prinitng data
                            for item in data:
                                print(f"{item[1]} - {item[0]}")

                    except FileNotFoundError:
                        print("[Info] there are no files.....")

                    waitforkey()

                # *  Find Largest File
                case 26:
                    system("cls")

                    # tool's description
                    print(
                        "## Find Largest File\nIt finds the largest file in a directory and outputs it.")

                    src = get_directory("\nEnter path to a folder: ")
                    whole_tree = get_bool("Search sub-dirs also?")

                    print(f"\n[Info] scanning '{src}'...")
                    # finding largest file
                    data = f.find_largest_file(src, whole_tree)

                    # check if theres any data at all
                    if data[0]:
                        print(f"\nLargest file in '{src}' is:")
                        file_name = path.basename(data[0])
                        print(
                            f"File name: '{file_name}'\nFile size: '{data[1]}'\nFile path: '{data[0]}'")
                    else:
                        print(f"[Info] there are no files...")

                    waitforkey()

                # *  Find Smallest File
                case 27:
                    system("cls")

                    # tool's description
                    print(
                        "## Find Smallest File\nIt finds the smallest file in a directory and outputs it.")

                    src = get_directory("\nEnter path to a folder: ")
                    whole_tree = get_bool("Search sub-dirs also?")

                    print(f"\n[Info] scanning '{src}'...")
                    # finding smallest file
                    data = f.find_smallest_file(src, whole_tree)

                    # check if there's any data at all
                    if data[0]:
                        print(f"\nSmallest file in '{src}' is:")
                        file_name = path.basename(data[0])
                        print(
                            f"File name: '{file_name}'\nFile size: '{data[1]}'\nFile path: '{data[0]}'")
                    else:
                        print(f"[Info] there are no files...")

                    waitforkey()

                # *  Close the Program
                case 28:
                    system(colors['default'])
                    sys.exit()

                case _:
                    print("Default Case")

    except KeyboardInterrupt:
        system(colors['default'])
        sys.exit()


def confirm(message):
    """ Yes/No Confirmation end user """

    while True:
        answer = input(
            f"{message}\nAre you sure you want to continue? (y/n): ").lower().strip()
        if answer == "y":
            return True
        elif answer == "n":
            return False
        else:
            print("(y/n), choose one of these!\n")


def get_bool(prompt):
    """ Get bool from end-user """

    while True:
        answer = input(f"{prompt} (y/n): ").lower().strip()
        if answer == "y":
            return True
        elif answer == "n":
            return False
        else:
            print("(y/n), choose one of these!\n")


def get_int(prompt: str, min: int, max: int):
    """
    ### Get Int
    Get Int from end-user in range between `min` and `max` inclusive
    """
    while True:
        try:
            temp = int(input(prompt))
            if temp in range(min, max+1):
                return temp
            else:
                print(f"Invalid option, Try again!\n")
        except (ValueError, EOFError):
            print(f"Invalid option, Try again!\n")


def get_directory(prompt):
    """ Get Directory path from end user """
    while True:
        temp = input(prompt)
        if path.isdir(temp):
            return temp
        else:
            print(f"'{temp}' is not an existing directory, Try again!")


def get_file(prompt):
    """ Get file path from end user """
    while True:
        temp = input(prompt)
        if path.isfile(temp):
            return temp
        else:
            print(f"'{temp}' is not an existing file, Try again!")


def get_extension(prompt):
    """ Get file extension from end-user """

    while True:
        e = input(prompt)
        if e.startswith("."):
            return e
        else:
            print(f"'{e}' is not a valid extension")


def get_size_bounds(prompt):
    """ 
    #### Get Size Bounds from end-user
    Only below format is allowed
    ```
    format_sytax = "value unit"
    format_example = "2 kb"
    ```
    """
    # defining a pattern for size format
    pattern = re.compile("(^\d+ \w{1,2}$)", re.IGNORECASE)

    while True:
        if matches := re.match(pattern, input(prompt).strip()):
            # return match
            return matches.groups()[-1]

        else:
            print("Invalid format, try again\n")


def waitforkey(prompt="\nPress enter to continue...\n"):
    """ Wait for the user to press enter and then continue """

    input(prompt)


if __name__ == "__main__":
    main()
