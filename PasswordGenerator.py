import string
import random

Passwordlength = 8
specialCharacters = "!@#$%^&*"

print ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits + string.ascii_lowercase + specialCharacters) for i in range(Passwordlength))