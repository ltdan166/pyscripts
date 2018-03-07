#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import binascii
import sys
import base64
import csv
import codecs

from argparse import ArgumentParser

def read_file(): 
	parser = ArgumentParser(description="""Parse the file name""")
	parser.add_argument('-f', '--file', required=True,
                        help="""Parse the file name.""")	
	args = parser.parse_args()
	file = args.file
	
	with open (file, "rt") as f:
		with codecs.open ("decoded_"+file, "w", encoding='utf8') as newf:
			reader = csv.reader(f, delimiter="|")			
					
			for i, line in enumerate(reader):								
				for j, col in enumerate(line):						
					l = len(str(col)) % 4				
					if l != 0:
						print ('ERROR : line[{},{}] = {} with length {}'.format(i, j, str((col)), l))
					else:
						dec = base64.b64decode (str(col)).decode ('utf8')						
						print ('line[{},{}] = {}'.format(i+1, j, dec))						
						if j < len(line)-1:
							newf.write (dec+"|");					
						else:
							newf.write (dec+"\n");


if __name__ == '__main__':
    read_file()
	
	
		
