import smtplib
import datetime
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from icalendar import Calendar, Event, vCalAddress, vText
from flask import render_template

def send_emails(card_dictionary, path2documents):

    student_name            = card_dictionary['STUDENT_NAME']
    student_lastname        = card_dictionary['STUDENT_NAME'].split(" ")[-1]
    student_email           = card_dictionary['STUDENT_EMAIL']
    client_name             = card_dictionary['CLIENT_NAME']
    client_lastname         = card_dictionary['CLIENT_NAME'].split(" ")[-1]
    client_salutation       = card_dictionary['CLIENT_GENDER']['SAL'] + " " + client_lastname
    instructor_salutation   = card_dictionary['INSTRUCTOR_NAME']['SALUTATION']
    instructor_email        = card_dictionary['INSTRUCTOR_NAME']['EMAIL']
    court_name              = card_dictionary['COURT']['SUBNAME'].split(" ")[1]
    arraignment_date        = card_dictionary['ARRAIGNMENT']
    next_date               = card_dictionary['NEXT_DATE']
    next_purpose            = card_dictionary['NEXT_PURPOSE']


    path2zip = path2documents + client_lastname.lower() + '/' + client_lastname.lower() + '.zip'
    calendar_content = create_calendar(card_dictionary)

    print(path2zip)

    # Gmail login credentials for sender account
    gmail_username  = 'cji.intake.assistant@gmail.com'
    gmail_password  = '8zm{KyW&pgN%'

    # Format email to student
    message_student = MIMEMultipart()
    message_student['Subject']              = "{} Documents".format(client_lastname)
    message_student['From']                 = "CJI Intake Assistant <" + gmail_username + ">"
    message_student['To']                   = student_email
    message_student.preamble                = """preamble"""
    message_student.student_firstname       = student_name
    message_student.client_lastname         = client_name
    message_student.instructor_salutation   = instructor_salutation

    # Render email_card_student.html as html variable for student
    html_student = render_template('email_card_student.html',
                                   student_name=student_name,
                                   client_name=client_name,
                                   client_salutation=client_salutation)

    # Format and attach html as email body for student
    html_body_student = MIMEText(html_student, 'html')
    message_student.attach(html_body_student)

    # Format and attach zip folder as attachment for student
    zip_attachment = MIMEApplication(open(path2zip).read())
    zip_attachment.add_header('Content-Disposition', 'attachment', filename='{}_documents.zip'.format(client_name))
    message_student.attach(zip_attachment)

    # Format and attach calendar invite as attachment for student
    calendar_attachment = MIMEText(calendar_content, 'calendar;method=REQUEST')
    message_student.attach(calendar_attachment)

    # Try to send the email to student
    try:
        server_ssl = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server_ssl.ehlo()  # optional
        server_ssl.login(gmail_username, gmail_password)
        server_ssl.sendmail(gmail_username, student_email, message_student.as_string())
        server_ssl.close()
        print "Successfully Emailed Student"

    # Except, print an error message
    except:
        print 'Something went wrong in sending email to student'


    # Format email to instructor
    message_instructor                          = MIMEMultipart()
    message_instructor['Subject']               = "{} New Case".format(student_name)
    message_instructor['From']                  = "CJI Intake Assistant <" + gmail_username + ">"
    message_instructor['To']                    = instructor_email
    message_instructor.preamble                 = """preamble"""
    message_instructor.student_firstname        = student_name
    message_instructor.client_lastname          = client_name
    message_instructor.instructor_salutation    = instructor_salutation
    message_instructor.court_name               = court_name
    message_instructor.arraignment_date         = arraignment_date

    # Render email_card_instructor.html as html variable for instructor
    html_instructor = render_template('email_card_instructor.html',
                                      student_name=student_name,
                                      client_name=client_name,
                                      instructor_salutation=instructor_salutation,
                                      court_name=court_name,
                                      arraignment_date=arraignment_date,
                                      next_purpose=next_purpose,
                                      next_date=next_date)

    # Format and attach html as email body for student
    html_body_instructor = MIMEText(html_instructor, 'html')
    message_instructor.attach(html_body_instructor)

    # Try to send the email to instructor
    try:
        server_ssl = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server_ssl.ehlo()  # optional
        server_ssl.login(gmail_username, gmail_password)
        server_ssl.sendmail(gmail_username, student_email, message_instructor.as_string())
        server_ssl.close()
        print "Successfully Emailed Instructor"

    # Except, print an error message
    except:
        print 'Something went wrong in sending email to instructor'


def create_calendar(card_dictionary):

    calendar_date = card_dictionary['NEXT_DATE']
    calendar_purpose = card_dictionary['NEXT_PURPOSE']
    calendar_date_object = datetime.datetime.strptime(calendar_date, '%B %d, %Y')
    client_lastname = card_dictionary["CLIENT_NAME"].split(" ")[-1]
    student_email = card_dictionary['STUDENT_EMAIL']

    calendar = Calendar()
    event = Event()

    event.add('dtstart', datetime.datetime(calendar_date_object.year, calendar_date_object.month, calendar_date_object.day, int('9')))
    event.add('dtend', datetime.datetime(calendar_date_object.year, calendar_date_object.month, calendar_date_object.day, int('10')))
    #event.add('dtend', datetime.date())
    event.add('summary', client_lastname + ", " + calendar_purpose)
    event.add('location', "Roxbury Division, BMC")
    event.add('organizer', student_email)

    calendar.add_component(event)

    calendar_content = calendar.to_ical()
    return(calendar_content)

