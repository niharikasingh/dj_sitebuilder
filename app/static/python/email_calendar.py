import datetime
from icalendar import Calendar, Event, vCalAddress, vText
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from flask import render_template
import smtplib

def email_calendar(card_dictionary):

    student_name        = card_dictionary['STUDENT_NAME']
    recipients          = [card_dictionary['STUDENT_EMAIL'], card_dictionary['INSTRUCTOR_NAME']['EMAIL']]
    client_name         = card_dictionary['CLIENT_NAME']
    client_lastname     = card_dictionary["CLIENT_NAME"].split(" ")[-1]

    calendar_content = create_calendar(card_dictionary)

    # Gmail login credentials for sender account
    gmail_username  = 'cji.intake.assistant@gmail.com'
    gmail_password  = '8zm{KyW&pgN%'

    # Format email
    message = MIMEMultipart()
    message['Subject']          = "{} Calendar Invite".format(client_lastname)
    message['From']             = "CJI Intake Assistant <" + gmail_username + ">"
    message['To']               = (", ").join(recipients)
    message.preamble            = """preamble"""
    message.student_firstname   = student_name
    message.client_lastname     = client_name

    # Render email_cal.html as html variable
    html = render_template('email_card_instructor.html', student_name=student_name, client_name=client_name)

    # Format and attach html as email body
    html_body = MIMEText(html, 'html')
    message.attach(html_body)

    # Format and attach email attachment
    calendar_attachment = MIMEText(calendar_content,'calendar;method=REQUEST')
    message.attach(calendar_attachment)

    # Try to send the email
    try:
        server_ssl = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server_ssl.ehlo()
        server_ssl.login(gmail_username, gmail_password)
        server_ssl.sendmail(gmail_username, recipients, message.as_string())
        server_ssl.close()

    # Except, print an error message
    except:
        print 'Something went wrong in sending email_calendar'



def create_calendar(card_dictionary):

    calendar_date = card_dictionary['NEXT_DATE']
    calendar_purpose = card_dictionary['NEXT_PURPOSE']
    calendar_date_object = datetime.datetime.strptime(calendar_date, '%B %d, %Y')
    client_lastname = card_dictionary["CLIENT_NAME"].split(" ")[-1]
    student_email = card_dictionary['STUDENT_EMAIL']
    instructor_email = card_dictionary['INSTRUCTOR_NAME']['EMAIL']

    calendar = Calendar()
    event = Event()

    event.add('dtstart', datetime.datetime(calendar_date_object.year, calendar_date_object.month, calendar_date_object.day, int('9')))
    event.add('dtend', datetime.datetime(calendar_date_object.year, calendar_date_object.month, calendar_date_object.day, int('10')))
    #event.add('dtend', datetime.date())
    event.add('summary', client_lastname + ", " + calendar_purpose)
    event.add('location', "Roxbury Division, BMC")
    event.add('attendee', [student_email + ', ' + instructor_email])
    event.add('organizer', student_email)

    calendar.add_component(event)

    calendar_content = calendar.to_ical()
    return(calendar_content)


# # OLD CODE FOR SENDING GMAIL INVITE
#
# from __future__ import print_function
# import httplib2
# import os
# from apiclient import discovery
# from oauth2client import client
# from oauth2client import tools
# from oauth2client.file import Storage
#
# import datetime
#
# try:
#     import argparse
#     flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
# except ImportError:
#     flags = None
#
# # If modifying these scopes, delete your previously saved credentials
# # at ~/.credentials/calendar-python-quickstart.json
# SCOPES = 'https://www.googleapis.com/auth/calendar'
# CLIENT_SECRET_FILE = '/Users/jeffreyroderick/PycharmProjects/cji_intake/static/documents/client_secret.json'
# APPLICATION_NAME = 'Google Calendar API Python Quickstart'
#
#
# def get_credentials():
#     """Gets valid user credentials from storage.
#
#     If nothing has been stored, or if the stored credentials are invalid,
#     the OAuth2 flow is completed to obtain the new credentials.
#
#     Returns:
#         Credentials, the obtained credential.
#     """
#     home_dir = os.path.expanduser('~')
#     credential_dir = os.path.join(home_dir, '.credentials')
#     if not os.path.exists(credential_dir):
#         os.makedirs(credential_dir)
#     credential_path = os.path.join(credential_dir,
#                                    'calendar-python-quickstart.json')
#
#     store = Storage(credential_path)
#     credentials = store.get()
#     if not credentials or credentials.invalid:
#         flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
#         flow.user_agent = APPLICATION_NAME
#         if flags:
#             credentials = tools.run_flow(flow, store, flags)
#         else: # Needed only for compatibility with Python 2.6
#             credentials = tools.run(flow, store)
#         print('Storing credentials to ' + credential_path)
#     return credentials
#
# def post2calendar(card_dictionary):
#
#     student_name        = card_dictionary['STUDENT_NAME']
#     client_lastname     = card_dictionary["CLIENT_NAME"].split(" ")[-1]
#     next_date           = card_dictionary['NEXT_DATE']
#     cal_object          = datetime.datetime.strptime(next_date, '%B %d, %Y')
#     next_purpose        = card_dictionary['NEXT_PURPOSE']
#     court_name          = card_dictionary['COURT']
#     student_email       = card_dictionary['STUDENT_EMAIL']
#     instructor_email   = card_dictionary['INSTRUCTOR_NAME']['EMAIL']
#
#     credentials = get_credentials()
#     http = credentials.authorize(httplib2.Http())
#     service = discovery.build('calendar', 'v3', http=http)
#
#     event = {
#         'summary': '{}, {}'.format(client_lastname, next_purpose),
#         'location': '{}'.format(court_name['NAME']),
#         'start': {
#             'dateTime': '{}-{}-{}T09:00:00'.format(cal_object.year, cal_object.month, cal_object.day),
#             'timeZone': 'America/New_York',
#         },
#         'end': {
#             'dateTime': '{}-{}-{}T10:00:00'.format(cal_object.year, cal_object.month, cal_object.day),
#             'timeZone': 'America/New_York',
#         },
#         'attendees': [
#             {'email': '{}'.format(student_email)},
#             {'email': '{}'.format(instructor_email)},
#         ],
#     }
#
#     event = service.events().insert(calendarId='primary', body=event, sendNotifications=True).execute()
#
#
#     print(event)
#     print(event['id'])
#
#     rule = {
#         "role": "reader",
#         "scope": {
#             "type": "user",
#             "value": "{}".format(student_email)
#         }
#     }
#
#     created_rule = service.acl().insert(calendarId='primary', body=rule).execute()
#
#     updated_event = service.events().move(calendarId='calendar', eventId=event['id'], destination='{}'.format(student_email))
#
#     print (updated_event['updated'])