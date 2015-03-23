__author__ = 'Krivenko'
from sys import maxsize

class Contact:

    def __init__(self,firstname=None, middlename=None, lastname=None, nickname=None, title=None, company=None, address=None, home=None, mobile=None, work=None,
                       fax=None,byear=None, ayear=None, address2=None, phone2=None, notes=None,droplist=None,droplist2=None,droplist3=None,droplist4=None, id=None):
        self.firstname=firstname
        self.middlename=middlename
        self.lastname=lastname
        self.nickname=nickname
        self.title=title
        self.company=company
        self.address=address
        self.home=home
        self.mobile=mobile
        self.work=work
        self.fax=fax
        self.byear=byear
        self.ayear=ayear
        self.address2=address2
        self.phone2=phone2
        self.notes=notes
        self.droplist=droplist
        self.droplist2=droplist2
        self.droplist3=droplist3
        self.droplist4=droplist4
        self.id=id

    def __repr__(self):
        return "%s:%s:%s" %(self.id,self.lastname,self.firstname,)

    def __eq__(self, other):
        return  (self.id is None or other.id is None or self.id==other.id) and (self.firstname== other.firstname or self.firstname is None or other.firstname is None) and ( self.lastname==other.lastname or self.lastname is None or other.lastname is None)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
