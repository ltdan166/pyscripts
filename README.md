# pyscripts 

MailSender.py -d <directory> -m <mode> -r <filename> -r <recipient>
-d, --directory : Mail the contents of the specified directory, otherwise use the current directory.  Only the regular files in the directory are sent, and we don't recurse to
 subdirectories.
-m, --mode : Tell the program how to send files : (c)ontent in the mail body or as (a)ttachments.
-f, --filename : Rename the attached filename if specified. Otherwise use the original filename.
-r, --recipient : 

Base64Check.py -f <filename> : decode the content of the file from base64