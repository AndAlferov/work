from model.contact import Contact


def test_edit_first_contact(app):
    if app.contact.count() == 0:
      app.contact.create(Contact(firstname="test"))
    app.contact.test_edit_first_contact()