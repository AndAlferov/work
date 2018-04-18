# -*- coding: utf-8 -*-

from model.contact import Contact


def test_add_contact(app):
    app.contact.create(Contact(firstname="sdfsdf", secondname="sdfsdf", number="234234"))


def test_add_empty_contact(app):
    app.contact.create(Contact(firstname="", secondname="", number=""))