import pandas
from bunch import bunchify

def court_list(input_court, path2documents):

    worksheet = pandas.read_excel(path2documents + 'court_list.xlsx', 'Sheet1')

    worksheet = worksheet.to_dict('index')
    for i in worksheet:
        if worksheet[i]['NAME'] == input_court:
            print "Successfully Read Excel For Input Court"
            return(bunchify(worksheet[i]))

def crime_list(input_crime, path2documents):

    worksheet = pandas.read_excel(path2documents + 'crime_list.xlsx', 'Sheet1')

    worksheet = worksheet.to_dict('index')
    for i in worksheet:
        if worksheet[i]['STAT_DESCR'] == input_crime:
            print "Successfully Read Excel For Input Crime"
            return(bunchify(worksheet[i]))