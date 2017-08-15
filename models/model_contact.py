from sys import maxsize
class Contact:

    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, email=None, id=None,
                 homephone=None, mobilephone=None, workphone=None, secondaryphone=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.email = email
        self.id = id
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.secondaryphone = secondaryphone

    def __repr__(self):
        return '%s:%s %s' % (self.id, self.firstname, self.lastname)

    def __eq__(self, other):
        return self.firstname == other.firstname and \
               (self.id == other.id or self.id == None or other.id == None) and \
               self.lastname == other.lastname

    def id_or_max(self):
        if self.id is not None:
            return int(self.id)
        else:
            return maxsize