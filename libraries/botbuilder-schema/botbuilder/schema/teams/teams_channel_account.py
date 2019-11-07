# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.

from botbuilder.schema import ChannelAccount

class TeamsChannelAccount(ChannelAccount):
    def __init__(self, id = "", name = "", aad_object_id = "", role ="", given_name = "", surname = "", email = "", userPrincipalName = ""):
        super().__init__(**{"id":id, "name":name, "aad_object_id": aad_object_id, "role":role})
        self._given_name = given_name
        self._surname = surname
        self._email = email
        self._user_principal_name = userPrincipalName

    def get_id(self):
        return self._id
    
    def set_id(self, id):
        self._id = id

    def get_name(self):
        return self._name
    
    def set_name(self, name):
        self._name = name

    def get_given_name(self):
        return self._given_name
    
    def set_given_name(self, given_name):
        self._given_name = given_name

    def get_surname(self):
        return self._surname
    
    def set_surname(self, surname):
        self._surname = surname

    def get_email(self):
        return self._email
    
    def set_email(self, email):
        self._email = email
    
    def get_user_principal_name(self):
        return self._user_principal_name
    
    def set_user_principal_name(self, user_principal_name):
        self._user_principal_name = user_principal_name

    id = property(get_id, set_id)
    name = property(get_name, set_name)
    given_name = property(get_given_name, set_given_name)
    surname = property(get_surname, set_surname)
    email = property(get_email, set_email)
    user_principal_name = property(get_user_principal_name, set_user_principal_name)