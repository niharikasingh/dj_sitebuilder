import shutil

def delete_folder(card_dictionary, path2documents):

    client_lastname = card_dictionary["CLIENT_NAME"].split(" ")[-1].lower()

    # Define path to doc_drafts
    path2drafts = path2documents + client_lastname + '/'

    # Remove doc_drafts directory and contents
    shutil.rmtree(path2drafts)

    print "Successfully Deleted Folder"
