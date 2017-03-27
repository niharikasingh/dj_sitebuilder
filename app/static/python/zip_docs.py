import os
import zipfile

def zip2folder(card_dictionary, path2documents):

    path2drafts = path2documents + card_dictionary["CLIENT_NAME"].split(" ")[-1].lower()

    path_file_zip = ''
    if not path_file_zip:
        path_file_zip = os.path.join(
            os.path.dirname(path2drafts), os.path.basename(path2drafts) + '.zip')

    with zipfile.ZipFile(path_file_zip, 'w', zipfile.ZIP_DEFLATED) as zip_file:
        for root, dirs, files in os.walk(path2drafts):
            for file_or_dir in files + dirs:
                zip_file.write(
                    os.path.join(root, file_or_dir),
                    os.path.relpath(os.path.join(root, file_or_dir),
                    os.path.join(path2drafts, os.path.pardir)))

    os.rename(path_file_zip, path2drafts + '/' + os.path.basename(path_file_zip))


