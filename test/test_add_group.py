# -*- coding: utf-8 -*-
import pytest
from model.group import Group
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_test_add_group(app):
    app.Login(username="admin", password="secret")
    app.create_group(Group(name="dfhdf", header="fdfdfs", footer="dfd"))
    app.Logout()


def test_test_add_empty_group(app):
    app.Login(username="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.Logout()
