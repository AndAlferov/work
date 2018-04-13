# -*- coding: utf-8 -*-

from model.contact import Contact

def test_(app):
    app.contact.init_contact_creation()
    app.contact.fill_contact_firm(Contact(firstname="sdfsdf", secondname="sdfsdf", number="234234"))
    app.contact.submit_contact()
