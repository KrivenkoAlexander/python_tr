
import string
import random
from model.contact import Contact
import os.path
import jsonpickle
import sys
import getopt

try:
    opts, args=getopt.getopt(sys.argv[1:],"n:f",["numbers of contacts","file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n=5
f="data/contacts.json"

for o,a in opts:
    if o== "-n":
        n=int(a)
    elif o=="-f":
        f=a

def random_str(prefix,maxlen):
    symbols= string.ascii_letters + string.digits+' '*100
    return prefix+"".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

test_data=[Contact(firstname=random_str('firstname',15), middlename='middle', lastname="lastname", nickname='nickname', title='title',
                                        company="sdd", address="we", homephone="500", mobilephone="433", workphone="443", fax="3",
                                        byear="1988", ayear="1988",address2="retert", phone2="rr", notes="e",
                                        droplist="//div[@id='content']/form/select[1]//option[4]",
                                        droplist2="//div[@id='content']/form/select[2]//option[8]",
                                        droplist3="//div[@id='content']/form/select[3]//option[3]",droplist4="//div[@id='content']/form/select[4]//option[8]") for i in range(n)]

file=os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",f)

with open(file,"w") as out:
    jsonpickle.set_encoder_options('json',indent=2)
    out.write(jsonpickle.encode(test_data))
