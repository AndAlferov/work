from model.contact import Contact


def test_modify_contact_name(app):
    if app.contact.count() == 0:
      app.contact.create(Contact(firstname="test"))
    app.contact.modify_first_contact(Contact(firstname="New"))


def test_modify_contact_header(app):
    if app.contact.count() == 0:
      app.contact.create(Contact(firstname="test"))
    app.contact.modify_first_contact(Contact(secondname="New header"))