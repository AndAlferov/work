from model.contact import Contact


def test_modify_contact_name(app):
    app.contact.modify_first_contact(Contact(firstname="New"))


# def test_modify_contact_header(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(name="test"))
#    app.contact.modify_first_contact(Contact(header="New header"))
