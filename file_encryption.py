import os.path
import pyAesCrypt


# ENCRYPTION function
def encryption(file, password):

    # Buffer size
    size_of_buffer = 512 * 1024

    # Calling encryption method
    pyAesCrypt.encryptFile(
        str(file),
        str(file) + ".crp",
        password,
        size_of_buffer

    )

    print("File: " + str(os.path.splitext(file)[0] + " is encrypted!"))

    # Delete source file
    os.remove(file)

# Function for scanning directories
def search_dirs(directory, password):

    # Scanning each subdirectories in mentioned directory
    for name in os.listdir(directory):
        path = os.path.join(directory, name)

        # When file is found, encrypting it
        if os.path.isfile(path):
            try:
                encryption(path, password)
            except Exception as exc:
                print(exc)

        # If another directory found, continue with loop for searching files
        else:
            search_dirs(path, password)


password = input("Please enter a password for encrypting: ")
path_to_dir = input(str("Please enter a path to FOLDER: "))
search_dirs(path_to_dir, password)