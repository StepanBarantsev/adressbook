from sys import maxsize
class Contact:

    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, id=None,
                 homephone=None, mobilephone=None, workphone=None, secondaryphone=None,
                 all_phones_from_homepage=None, address=None, allemails=None, email1=None, email2=None,
                 email3=None, all_information=None, title=None, company=None, homepage=None, notes=None,
                 fax=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.id = id
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.secondaryphone = secondaryphone
        self.all_phones_from_homepage = all_phones_from_homepage
        self.address = address
        self.allemails = allemails
        self.email1 = email1
        self.email2 = email2
        self.email3 = email3
        self.all_information = all_information
        self.title = title
        self.notes = notes
        self.company = company
        self.homepage = homepage
        self.fax = fax

    def __repr__(self):
        return 'id:%s, firstname:%s, lastname:%s, middlename:%s, nickname:%s, homephone:%s, mobilephone:%s' \
               ', workphone:%s, secondaryphone:%s, address:%s, email1:%s' \
               ', email2:%s, email3:%s, title:%s, notes:%s, company:%s' \
               ', homepage:%s, fax:%s' % (self.id, self.firstname, self.lastname, self.middlename, self.nickname, self.homephone
                ,self.mobilephone, self.workphone, self.secondaryphone, self.address, self.email1, self.email2, self.email3, self.title
                ,self.notes, self.company, self.homepage, self.fax)

    def __eq__(self, other):
        return self.firstname == other.firstname and \
               (self.id == other.id or self.id == None or other.id == None) and \
               self.lastname == other.lastname

    def id_or_max(self):
        if self.id is not None:
            return int(self.id)
        else:
            return maxsize