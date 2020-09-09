# -*- coding: utf-8 -*- #используется в том случае если есть текст на русском языке

import time, re
from group import Group
from application import Application
import pytest


@pytest.fixture() #эта метка превращает фикстуру в инициализатор фикстуры
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture
#теперь можено избавиться от тестового класса и фикстуры завершения

def test_add_group(app):
    app.login(username="admin", password="secret")
    app.creat_group(Group(name="dgdfgdfg", header="dgdfgdfgdfg", footer="dgdfgdfgdfgdfgdfg"))
    app.logout()

def test_add_empty_group(app):
    app.login(username="admin", password="secret")
    app.creat_group(Group(name="", header="", footer=""))
    app.logout()




