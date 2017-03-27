import docxtpl
import os

def print2docs(card_dictionary, path2documents):

    # Store client's last name in variable client_lastname
    client_lastname = card_dictionary["CLIENT_NAME"].split(" ")[-1].lower()

    # Define path to doc_templates and path to doc_drafts
    path2templates  = path2documents + 'doc_templates/'
    path2drafts     = path2documents + client_lastname + '/'

    # Make temporary folder to store drafts
    os.mkdir(path2drafts)

    for root, dirs, files in os.walk(path2templates):
        for dir in dirs:
            os.mkdir(os.path.join(path2drafts, dir))

        for file in files:
            if file != ".DS_Store":
                #print (os.path.join(root, file))
                #print (os.path.join(root.replace('doc_templates', client_lastname), file.replace('template', client_lastname)))
                template_document = docxtpl.DocxTemplate(os.path.join(root, file))
                template_document.render(card_dictionary)
                template_document.save(os.path.join(root.replace('doc_templates', client_lastname), file.replace('template', client_lastname)))
                print "Successfully Printed: " + file.replace('template', client_lastname)