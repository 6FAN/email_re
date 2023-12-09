# Regular expression pattern for matching email addresses [1:31:57]
import re
email_pattern = r"\b[a-zA-Z0-9._+-1]+@[a-zA-Z0-9]+\.[a-z|A-Z]{2,7}\b"


def extract_mail(text):
    emails = re.findall(email_pattern,text)
    return emails
    

input_t =r"""
Please contact john.doe@example.com for harfan@fan.in more information.SG+mm@ex33.Com can also reach out to support@mywebsite.co.uk
     harfan@gmail.com
     pavanGowda91717+.@gmail.com"""
     
     
extracted_emails = extract_mail(input_t)
for ema in extracted_emails:
    print("Found Email : ",ema)
