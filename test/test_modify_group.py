__author__ = 'Krivenko'
from model.group import Group
import random
from random import randrange

def test_modify_group_name(app,db,check_ui):
        if app.group.count()==0:
            app.group.create(Group(name="test"))
        # edit group and update
        old_groups=db.get_group_list()
        index = randrange(len(old_groups))
        group_data= Group(name="New name")
        id=old_groups[index].id
        app.group.modify_group_by_id(id,group_data)
        new_groups=db.get_group_list()
        for i in old_groups:
            if i.id==id:
                i.name=group_data.name
        assert sorted(old_groups,key=Group.id_or_max) == sorted(new_groups,key=Group.id_or_max)