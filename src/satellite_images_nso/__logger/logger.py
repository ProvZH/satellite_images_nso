import datetime

"""
    Simple logger class

    Author: Michael de Winter
"""
def append_log(message):
    with open("log.txt", "a") as myfile:
                myfile.write(str(datetime.datetime.now())+": "+message)