import pytest
import logging
import json
import psycopg2

from helpers.utils import *
from lib.config import settings


@pytest.fixture
def sender():
    sender = ApiRequest()

    return sender

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    response = getattr(item.obj.__self__, "response", None)

    if rep.when == "call" and response is not None:
        setattr(item, "response", response)

@pytest.fixture(autouse=True)
def failure_tracking(request):
    yield
    try:
        if request.node.rep_call.failed:
            print(request.node.response.headers)
    except:
        pass

@pytest.fixture
def connect_to_db(scope='module'):
    conn = psycopg2.connect(
            dbname=settings.DB['NAME'],
            user=settings.DB['USER'],
            password=settings.DB['PASSWORD'],
            host=settings.DB['HOST'],
            port=settings.DB['PORT']
    )

    yield conn
    conn.close()
