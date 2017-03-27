import dateutil.parser
from ..python import read_excel

def format_data(card_dictionary, path2documents):

    # For instructor, add appropriate instructor's email
    if 'INSTRUCTOR_NAME' in card_dictionary:
        card_dictionary['INSTRUCTOR_NAME'] = {'NAME': 'Jeffrey Roderickss',
                                              'EMAIL': 'jroderick@jd17.law.harvard.edu',
                                              'SALUTATION': 'Mr. Proctor'}
        # if card_dictionary['INSTRUCTOR_NAME'] == 'Jennifer McKinnon':
        #     card_dictionary['INSTRUCTOR_NAME'] = {'NAME': 'Jennifer McKinnon', 'EMAIL': 'Jennifer McKinnon <jmckinnon@law.harvard.edu>'}
        # if card_dictionary['INSTRUCTOR_NAME'] == 'Lia Monahon':
        #     card_dictionary['INSTRUCTOR_NAME'] = {'NAME': 'Lia Monahon', 'EMAIL': 'Lia Monahon <lmonahon@law.harvard.edu>'}
        # if card_dictionary['INSTRUCTOR_NAME'] == 'Kristin Muniz':
        #     card_dictionary['INSTRUCTOR_NAME'] = {'NAME': 'Kristin Muniz', 'EMAIL': 'Kristin Muniz <kmuniz@law.harvard.edu>'}
        # if card_dictionary['INSTRUCTOR_NAME'] == 'Robert Proctor':
        #     card_dictionary['INSTRUCTOR_NAME'] = {'NAME': 'Robert Proctor', 'EMAIL': 'Robert Proctor <rproctor@law.harvard.edu>'}
        # if card_dictionary['INSTRUCTOR_NAME'] == 'Dehlia Umunna':
        #     card_dictionary['INSTRUCTOR_NAME'] = {'NAME': 'Dehlia Umunna', 'EMAIL': 'Dehlia Umunna <dumunna@law.harvard.edu>'}

    # For gender, add appropriate vocabulary
    if 'CLIENT_GENDER' in card_dictionary:
        if card_dictionary['CLIENT_GENDER'].lower() == 'male':
            card_dictionary['CLIENT_GENDER'] = {'GENDER': 'Male',
                                                'POSS': 'his',
                                                'SUBJ': 'he',
                                                'OBJ': 'him',
                                                'SAL': 'Mr. ' + card_dictionary['CLIENT_NAME'].split(" ")[-1]}
        elif card_dictionary['CLIENT_GENDER'].lower() == 'female':
            card_dictionary['CLIENT_GENDER'] = {'GENDER': 'Female',
                                                'POSS': 'her',
                                                'SUBJ': 'she',
                                                'OBJ': 'her',
                                                'SAL': 'Ms. ' + card_dictionary['CLIENT_NAME'].split(" ")[-1]}
        else:
            card_dictionary['CLIENT_GENDER'] = {'GENDER': 'UNDEFINED',
                                                'POSS': 'UNDEFINED',
                                                'SUBJ': 'UNDEFINED',
                                                'OBJ': 'UNDEFINED',
                                                'SAL': 'UNDEFINED'}

    # For court, check for crime in crime_list and add data
    if 'COURT' in card_dictionary:
        court_data = read_excel.court_list(card_dictionary['COURT'], path2documents)
        card_dictionary['COURT'] = court_data

    # For charges, check for crime in crime_list and add data
    if 'CHARGE_1' in card_dictionary:
        card_dictionary['CHARGE_1'] = read_excel.crime_list(card_dictionary['CHARGE_1'], path2documents)
    if 'CHARGE_2' in card_dictionary:
        card_dictionary['CHARGE_2'] = read_excel.crime_list(card_dictionary['CHARGE_2'], path2documents)
    if 'CHARGE_3' in card_dictionary:
        card_dictionary['CHARGE_3'] = read_excel.crime_list(card_dictionary['CHARGE_3'], path2documents)
    if 'CHARGE_4' in card_dictionary:
        card_dictionary['CHARGE_4'] = read_excel.crime_list(card_dictionary['CHARGE_4'], path2documents)
    if 'CHARGE_5' in card_dictionary:
        card_dictionary['CHARGE_5'] = read_excel.crime_list(card_dictionary['CHARGE_5'], path2documents)

    # For dates, parse dates and then format appropriately
    if 'CLIENT_DOB' in card_dictionary:
        card_dictionary['CLIENT_DOB'] = dateutil.parser.parse(card_dictionary['CLIENT_DOB']).strftime('%B %-d, %Y')
    if 'ARRAIGNMENT' in card_dictionary:
        card_dictionary['ARRAIGNMENT'] = dateutil.parser.parse(card_dictionary['ARRAIGNMENT']).strftime('%B %-d, %Y')
    if 'COMPLAINT_DATE' in card_dictionary:
        card_dictionary['COMPLAINT_DATE'] = dateutil.parser.parse(card_dictionary['COMPLAINT_DATE']).strftime('%B %-d, %Y')
    if 'OFFENSE_DATE' in card_dictionary:
        card_dictionary['OFFENSE_DATE'] = dateutil.parser.parse(card_dictionary['OFFENSE_DATE']).strftime('%B %-d, %Y')
    if 'NEXT_DATE' in card_dictionary:
        card_dictionary['NEXT_DATE'] = dateutil.parser.parse(card_dictionary['NEXT_DATE']).strftime('%B %-d, %Y')

    # For addresses, format appropriately
    if 'CLIENT_ADDRESS' in card_dictionary:
        print card_dictionary['CLIENT_ADDRESS']
    if 'INCIDENT_ADDRESS' in card_dictionary:
        print card_dictionary['INCIDENT_ADDRESS']

    return(card_dictionary)