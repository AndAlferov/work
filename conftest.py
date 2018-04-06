import pytest
from fixture.application1 import Application1


@pytest.fixture(scope = "session")
def app(request):
    fixture = Application1()
    request.addfinalizer(fixture.destroy)
    return fixture