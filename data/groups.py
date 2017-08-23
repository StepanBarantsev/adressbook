from models.model_group import Group
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return  prefix + ''.join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Group(group_name='', group_header='', group_footer='')] +\
           [Group(group_name=random_string('name', 10), group_header=random_string('header', 20),
                  group_footer=random_string('footer', 20))
            for i in range(5)
            ]