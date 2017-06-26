from shared import global_variables

def all_images_in_location():
    # Returns a list of all the names of the photos in the RECEIPT_LOCATION

    global_variables.RECEIPT_LOCATION = prompt_user_for_location()

    file_names = []
    for photos in global_variables.RECEIPT_LOCATION:
        file_names.append(photos)

    if global_variables.DEBUG:
        string_file_names = print_list_to_string(file_names)
        print "All the files located in the receipt location %s are %s" % (
         global_variables.RECEIPT_LOCATION, string_file_names
        )

    return file_names


def print_list_to_string(item_list):
    # TODO: is this correct?

    string = ""
    for item in item_list:
        string.append(item + "/n")
    return string

def prompt_user_for_location():
    # TODO: Maybe a popup to ask user to find the location of the photos.

    persist('receipt_location', receipt_location)
    return receipt_location
