#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import os
import sys
import smtplib

from argparse import ArgumentParser

from email import encoders
from email.message import Message
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#https://docs.python.org/3/library/email-examples.html
#python MailSender.py -r cn_anstel@samfm.net -m c/a -f <filename>
#planon.tms.france@gmail.com
#Planon2017

COMMASPACE = ', '

def sendMail(): 
	parser = ArgumentParser(description="""\
Send the contents of a directory as a MIME message.
Unless the -o option is given, the email is sent by forwarding to your local
SMTP server, which then does the normal delivery process.  Your local machine
must be running an SMTP server.
""")
	parser.add_argument('-d', '--directory',
                        help="""Mail the contents of the specified directory,
                        otherwise use the current directory.  Only the regular
                        files in the directory are sent, and we don't recurse to
                        subdirectories.""")
	parser.add_argument('-m', '--mode', required=True,
                        help="""Tell the program how to send files : (c)ontent in the mail body or as (a)ttachments.""")
	parser.add_argument('-f', '--filename', 
                        help="""Rename the attached filename if specified. Otherwise use the original filename""")
	parser.add_argument('-r', '--recipient', required=True,
                        action='append', metavar='RECIPIENT',
                        default=[], dest='recipients',
                        help='A To: header value (at least one required)')
	args = parser.parse_args()
	directory = args.directory
	mode = args.mode
	extlist = ['.txt', '.csv']
	
	if not directory:
		directory = '.'
	
	#for every file in the directory, use the filename as Subject
	for filename in os.listdir(directory):
		path = os.path.join(directory, filename)				
		
		#if not txt file, skip
		if all ([ext not in filename for ext in extlist]) or not os.path.isfile(path):
		    continue
			
		print ('File to send : '+path)

		msg = MIMEMultipart()
		msg['From'] = 'planon.tms.france@gmail.com'
		msg['To'] = COMMASPACE.join (args.recipients)
		msg['Subject'] = filename 		
				
		#read file content if necessary, otherwise simply attach the file to the email
		content = '';
		with open(path) as fp :
			content = MIMEText(fp.read())
		if mode == 'a':
			with open(path) as fp :
				if args.filename:
					attachfn = args.filename
				else:
					attachfn = filename
				content.add_header('Content-Disposition', 'attachment', filename=attachfn)				
		
		msg.attach(content)
		mailserver = smtplib.SMTP_SSL('smtp.gmail.com', 465)
		mailserver.ehlo()		
		####TO COMPLETE WITH AN ACTUAL GMAIL ACCOUNT#####
		mailserver.login('', '')
		mailserver.sendmail('planon.tms.france@gmail.com', args.recipients, msg.as_string())
		mailserver.quit()

if __name__ == '__main__':
    sendMail()
