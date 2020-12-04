import os


def create_file_if_not_exists(file):
    if not os.path.exists(file):
        open(file, 'w+')


def get_temp_folder():
    # define the name of the directory to be created
    return os.path.join(os.getcwd(), 'tmp')


def check_temp_folder():
    path = get_temp_folder()
    try:
        os.mkdir(path)
    except OSError:
        print("Creation of the directory %s failed" % path)
    else:
        print("Successfully created the directory %s " % path)


# check for tmp folder
check_temp_folder()
