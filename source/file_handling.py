from util.logger import get_logger
from logging import DEBUG


logger = get_logger(DEBUG)

logger.info("=============== File Handling ==============")

fp = open("comments.py",mode="rb")


logger.info(fp.read())

logger.info(fp.read())
logger.info(fp.tell())
fp.seek(0)
logger.info(fp.read())
fp.seek(0)

# Useful to read big size file
logger.info(fp.read(1024))
logger.info(fp.tell())
# seek function
# offset -- How many steps the file pointer to get moved
# whence -- 0, 1,2 ->
# 0 -> from the beginning of the file
# 1 -> from the current file pointer position
# 2 -> from the end of the file
# 1,2 option are only supported for the files opened in birnary format
fp.read(20)
fp.seek(10,1)
logger.info(fp.read(20))
fp.seek(0)
fp.seek(-500, 2)
logger.info(fp.read())
#help(fp.seek)
fp.seek(0)
fp.close()


try:
    fp = open("operators.py","r")
    for line in fp:
        logger.info(line)
        logger.info(line[200])

except FileNotFoundError as e:
    logger.error("File not found :%s",e)
    raise e

except IndexError as e:
    logger.error("IndexError: %s", e.args)


else:
    logger.info("Reading of file is done")

fp.close()



# 'with' keyword is context manager to close opened connection/files incase of errors.
with open("operators.py") as fp:
    for line in fp:
        logger.info(line)
        try:
            logger.info(line[200])
        except IndexError as e:
            logger.error("Reading data from out of Index ")


# Read bigsize file
# Recommended approach for reading big size file
with open("operators.py") as fp:
    while True:
        # To read 500 bytes at a time
        data = fp.read(500)
        # True when reached EOF (End of File)
        if not data:
            break
        logger.info(data)

with open("operators.py") as fp:
    while True:
        # To read one line data
        data = fp.readline()
        # True when reached EOF (End of File)
        if not data:
            break
        logger.info(data)

with open("operators.py") as fp:
    # To read each line data into list.
    # It reads complete data from file.
    # Not recommended approach for big size file
    list_of_lines_data = fp.readlines()
    logger.info(list_of_lines_data)
    # fp.write("Hello to test write for the file opened with 'r' mode")



# ==================== write, writelines =============== #
# If mode is "w" or "w+", then file content is clear after file open .
# If file doesn't exist , new file will be created.

# "w" mode allows only write but read
# NewFile.txt will be created
with open("NewFile.txt", "w") as fp:
    fp.write("Hello this is new file with 'w' mode\n")
    # writelines(iterable_object)
    fp.writelines({"\nhello", "\tthis is in set"})
    fp.writelines(["\nnew data with list"])

    # "w" mode does allow to read file
    try:
        fp.read()
    except IOError as e:
        logger.error("w mode will not permit reading")


# w+ -> read and write allowed.
with open("NewFile1.txt", "w+") as fp:
    fp.write("This is new file with 'w+' mode")
    # To move file pointer to the beginning of the file
    fp.seek(0)
    logger.info(fp.read())


# r+ -> read and write allowed but new file will not be created
#     better approach read the file till end then add data to it.
with open("NewFile1.txt", "r+") as fp:
    logger.info(fp.read())
    fp.write("\nThis is new data with 'r+' mode")
    fp.seek(0)
    logger.info(fp.read())


# a -> append mode. File will be created if not exist but content is not clear.
# It allows only write.
# Pointer moved to end of the file so written content will be appended.

# Open Existing file
# Check content is clear or appended after below block executed
with open("NewFile1.txt", "a") as fp:
    fp.write("\n Hello new data from 'a' mode")
    try:
        fp.seek(0)
        fp.read()
    except IOError as e:
        logger.error("Read will not be permitted with 'a' mode")


# New File
# Check new file created.
with open("NewFile2.txt","a") as fp:
    fp.write("Hello this is new file with 'a' mode\n")

# Existing file
# 'a+' supports read and write file permissions
with open("NewFile2.txt","a+") as fp:
    fp.write("\n Hello this is existing file with 'a+'")
    fp.seek(0)
    logger.info(fp.read())

# Note: If any file is not open with "r",'w","a","r+","w+","a+". Use binary modes
# Modes to use: "rb", "wb", "ab", "rb+", "wb+", "ab+"
