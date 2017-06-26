from shared import global_variables

def persist(key, value):
    if global_variables.DEBUG:
        print "new key: %s, value: %s" % (key, value)

    # TODO: use a file included in the .gitignore to store basic data.
    # TODO: determine what file type, and access methods

def find_value(key):
    # TODO: this
