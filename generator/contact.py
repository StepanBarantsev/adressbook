from models.model_contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return  prefix + ''.join([random.choice(symbols) for i in range(random.randrange(maxlen))])

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number_of_groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)
n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == '-n':
        n = int(a)
    elif o == '-f':
        f = a


testdata = [Contact(firstname='Stepan', middlename='Barantsev', lastname='Lol',
                                    nickname='Bloodes', email1='stepan.barantsev@gmail.com')] +\
           [Contact(firstname=random_string('', 10),
                    middlename=random_string('', 20),
                    lastname=random_string('', 20),
                    nickname=random_string('', 20),
                    homephone=random_string('', 20),
                    mobilephone=random_string('', 20),
                    workphone=random_string('', 20),
                    secondaryphone=random_string('', 20),
                    email1=random_string('', 20),
                    email2=random_string('', 20),
                    email3=random_string('', 20),
                    title=random_string('', 20),
                    notes=random_string('', 20),
                    company=random_string('', 20),
                    homepage=random_string('', 20),
                    fax=random_string('', 20))
            for i in range(5)
            ]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, 'w') as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
