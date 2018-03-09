import re
from robobrowser import RoboBrowser

br = RoboBrowser(user_agent="Chrome")
br.open("https://www.familytreedna.com/sign-in")
print(br)
form = br.get_forms()
print(form)
#passwordField
#print(fields)
"""
form['kitnum-input'] - '151401'
form['password-input'] - '3949293a'
br.submit_form(form)

src = str(br.get_forms())

print(src)
"""