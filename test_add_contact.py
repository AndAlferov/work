# -*- coding: utf-8 -*-
import pytest
from contact import Contact
from application1 import Application1


@pytest.fixture
def app(request):
    fixture = Application1()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_(app):
    app.login(username="admin", password="secret")
    app.init_contact_creation()
    app.fill_contact_firm(Contact(firstname="sdfsdf", secondname="sdfsdf", number="234234"))
    app.submit_contact()
    app.logout()
