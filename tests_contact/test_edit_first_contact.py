from model.contact import Contact


def test_edit_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test", secondname="text"))
    old_contacts = app.contact.get_contact_list()
    app.contact.test_edit_first_contact()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
