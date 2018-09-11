""" This module is used to practice comments """
import argparse

c = """this module is used
to"""
print(c)
d = "this is module is used " \
    "to"
print(d)




# ====================== Block comment Example =====================
# The main function will parse arguments via the parser variable.  These
# arguments will be defined by the user on the console.  This will pass
# the word argument the user wants to parse along with the filename the
# user wants to use, and also provide help text if the user does not
# correctly pass the arguments.
#
# Add extra comment
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
      "-w","--word",dest="word",
      help="the word to be written to a text file."
    )
    parser.add_argument(
      "-f","--filename",dest="filename",
      help="the path to the text file to be searched through"
    )

    cmd_options = parser.parse_args()
    print(cmd_options)

    fp = open(cmd_options.filename, "w") # open a file in write mode
    fp.write(cmd_options.word)
    fp.close()


# ================== Documentation string Example=================== #
def get_db_conn(host_name, db, user, db_pass):
    """
    Get a db connection with given host.
    if no connection exist, thrown an exception
    :param host_name: hostname
    :param db: database name
    :param user: database user
    :param db_pass: database password
    :return:
    """
    pass

def get_conn(a, b):
    """

    :param a:
    :param b:
    :return:
    """

print(__name__)

