from xml.etree import ElementTree as ET
from gomatic.mixins import CommonEqualityMixin
from gomatic.xml_operations import ignore_patterns_in, PossiblyMissingElement


def Profiles(element):
    if element.tag == "admins":       
        return AdminUserProfile(PossiblyMissingElement(element).possibly_missing_child('user').iterator, PossiblyMissingElement(element).possibly_missing_child('role').iterator)

    if element.tag == "view":       
        return ViewUserProfile(PossiblyMissingElement(element).possibly_missing_child('user').iterator, PossiblyMissingElement(element).possibly_missing_child('role').iterator)

    if element.tag == "operate":       
        return OperateUserProfile(PossiblyMissingElement(element).possibly_missing_child('user').iterator, PossiblyMissingElement(element).possibly_missing_child('role').iterator)
    
    raise RuntimeError("don't know of profile matching " + ET.tostring(element, 'utf-8'))

class AdminUserProfile(CommonEqualityMixin):
    def __init__(self, users=[], roles=[]):
        self.__users = users
        self.__roles = roles

    def __repr__(self):
        return 'AdminUserProfile([%s],[%s])' % (','.join('"' + user + '"' for user in self.__users), ','.join('"' + role + '"' for role in self.__roles))

    def append_to(self, element):
        element.append(ET.fromstring('<admins>%s%s</admins>' % (''.join('<user>' + user + '</user>' for user in self.__users),''.join('<role>' + role + '</role>' for role in self.__roles))))

class ViewUserProfile(CommonEqualityMixin):
    def __init__(self, users=[], roles=[]):
        self.__users = users
        self.__roles = roles

    def __repr__(self):
        return 'ViewUserProfile([%s],[%s])' % (','.join('"' + user + '"' for user in self.__users), ','.join('"' + role + '"' for role in self.__roles))

    def append_to(self, element):
        element.append(ET.fromstring('<view>%s%s</view>' % (''.join('<user>' + user + '</user>' for user in self.__users),''.join('<role>' + role + '</role>' for role in self.__roles))))

class OperateUserProfile(CommonEqualityMixin):
    def __init__(self, users=[], roles=[]):
        self.__users = users
        self.__roles = roles

    def __repr__(self):
        return 'OperateUserProfile([%s],[%s])' % (','.join('"' + user + '"' for user in self.__users), ','.join('"' + role + '"' for role in self.__roles))

    def append_to(self, element):
        element.append(ET.fromstring('<operate>%s%s</operate>' % (''.join('<user>' + user + '</user>' for user in self.__users),''.join('<role>' + role + '</role>' for role in self.__roles))))