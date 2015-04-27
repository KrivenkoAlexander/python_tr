__author__ = 'Krivenko'
from sys import maxsize

class Contact:

    def __init__(self,firstname=None, middlename=None, lastname=None, nickname=None, title=None, company=None, address=None, homephone=None, mobilephone=None, workphone=None,secondaryphone=None,
                       fax=None,byear=None, ayear=None, address2=None, phone2=None, notes=None,droplist=None,droplist2=None,
                       droplist3=None,droplist4=None,id=None,allemail=None,allphones=None,alladress=None,email=None,email2=None,email3=None,):
        self.firstname=firstname
        self.middlename=middlename
        self.lastname=lastname
        self.nickname=nickname
        self.title=title
        self.company=company
        self.address=address
        self.homephone=homephone
        self.mobilephone=mobilephone
        self.workphone=workphone
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
        self.alladress=alladress
        self.allemail=allemail
        self.allphones=allphones
        self.secondaryphone=secondaryphone
        self.email=email
        self.email2=email2
        self.email3=email3


    def __repr__(self):
        return "%s:%s:%s" %(self.id,self.lastname,self.firstname,)

    def __eq__(self, other):
        return  (self.id is None or other.id is None or self.id==other.id) and\
                (self.firstname== other.firstname or self.firstname is None or other.firstname is None) and \
                ( self.lastname==other.lastname or self.lastname is None or other.lastname is None)and\
                (self.address==other.address or self.address is None or other.address is None) and \
                (self.homephone==other.homephone or self.homephone is None or other.homephone is None) and\
                (self.workphone==other.workphone or self.workphone is None or other.workphone is None) and\
                (self.mobilephone==other.mobilephone or self.mobilephone is None or other.mobilephone is None)


    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
