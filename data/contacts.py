from model.contact import Contact
import string
import random


def random_str(prefix,maxlen):
    symbols= string.ascii_letters + string.digits+' '*100
    return prefix+"".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

test_data=[Contact(firstname=random_str('firstname',15), middlename='middle', lastname="lastname", nickname='nickname', title='title',
                                        company="sdd", address="we", homephone="500", mobilephone="433", workphone="443", fax="3",
                                        byear="1988", ayear="1988",address2="retert", phone2="rr", notes="e",
                                        droplist="//div[@id='content']/form/select[1]//option[4]",
                                        droplist2="//div[@id='content']/form/select[2]//option[8]",
                                        droplist3="//div[@id='content']/form/select[3]//option[3]",droplist4="//div[@id='content']/form/select[4]//option[8]") for i in range(1)]
