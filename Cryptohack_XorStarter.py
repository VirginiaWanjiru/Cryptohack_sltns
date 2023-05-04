

import sys
from Crypto.Util.number import bytes_to_long
from Crypto.Util.number import long_to_bytes
import this
import base64



if sys.version_info.major == 2:
    print("You are running Python 2, which is no longer supported. Please update to Python 3.")

print("Here is your flag:")

data="label"
flag=''

for c in data:
   flag+= chr(ord(c)^ 13)

   print('crypto{{{}}}'.format(flag))




