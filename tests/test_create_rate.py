import pytest
import logging
import json

from support.const import *
from support.assertions import *
from helpers.utils import *


logger = logging.getLogger('public_api')

REQUEST_PATH = '/nps'
REQUEST_TYPE = 'POST'

class TestPostRate:
    """Test create rate"""

    def setup_class(cls):
        logger.info('=================================================================')

    def teardown_class(cls):
        logger.info('-----------------------------------------------------------------')

    def setup_method(self, method):
        logger.info('==================TEST STARTED==================')
        logger.info(f"{self.__doc__} {method.__doc__}")

    def teardown_method(self, method):
        logger.info('------------------TEST FINISHED------------------')

    @pytest.mark.parametrize(
        "user_action, feedback",
        [
            ("1", "test"),
            ("2", "test\ntest"),
            ("3", None),
            ("2", ""),
            ("8", None),
            ("10", ""),
            # ("9", "test1"), #TODO сохраняется ли коммент?
            ("0", "test2"),
            ("4", "   test   ")
        ]
    )
    def test_full_body(self, connect_to_db, sender, body, user_action, feedback):
        """with valid json"""

        sender.set_data(body)
        sender.add_headers({'Content-Type': 'application/json'})

        res = sender.build(REQUEST_TYPE, REQUEST_PATH)
        payload = json.loads(res.text)

        assert_valid_response(res, STATUS_CODE_OK, CONTENT_TYPE_JSON)
        assert_valid_schema(payload, 'ok.json')

        assert payload["status"] == "ok"

        feedback = feedback.strip() if feedback is not None else None
        assert_from_db(connect_to_db, user_action, feedback)

    @pytest.mark.parametrize(
        "user_action, feedback",
        [
            # ("8", ""), #TODO
            # ("10", None), #TODO
            # ("10", "test"), #TODO
            # (None, None), #TODO
            (2, ""),
            (["8"], None),
            ("-2", ""),
            ("1.7", "test1"),
            ("11", "test2"),
            ("4", 4),
            ("3", [4]),
            (None, "test")
        ]
    )
    def test_validation_error(self, connect_to_db, sender, body, user_action, feedback):
        """with not valid values inside json"""

        sender.set_data(body)
        sender.add_headers({'Content-Type': 'application/json'})

        res = sender.build(REQUEST_TYPE, REQUEST_PATH)
        payload = json.loads(res.text)

        assert_valid_response(res, STATUS_CODE_BAD_REQUEST, CONTENT_TYPE_JSON)
        assert_valid_schema(payload, 'error.json')

        assert payload["status"] == "error"

        feedback = feedback.strip() if feedback is not None else None

        with pytest.raises(AssertionError):
            assert_from_db(connect_to_db, user_action, feedback)

    def test_not_allowed(self, sender):
        """not allowed method"""

        res = sender.build('GET', REQUEST_PATH)

        assert_valid_response(res, STATUS_CODE_NO_METHOD, CONTENT_TYPE_JSON)

    def test_invalid_json(self, sender):
        """request with invalid json"""

        sender.set_data('""')
        sender.add_headers({'Content-Type': 'application/json'})

        res = sender.build(REQUEST_TYPE, REQUEST_PATH)
        self.response = res

        payload = json.loads(res.text)

        assert_valid_response(res, STATUS_CODE_BAD_REQUEST, CONTENT_TYPE_JSON)
        assert_valid_schema(payload, 'error.json')

    def test_empty_json(self, sender):
        """request with empty json"""

        sender.set_data('{}')
        sender.add_headers({'Content-Type': 'application/json'})

        res = sender.build(REQUEST_TYPE, REQUEST_PATH)
        self.response = res

        payload = json.loads(res.text)

        assert_valid_response(res, STATUS_CODE_BAD_REQUEST, CONTENT_TYPE_JSON)
        assert_valid_schema(payload, 'error.json')

    def test_random_json(self, sender):
        """request with empty json"""

        sender.set_data('{"user": "admin", "comment": "test"}')
        sender.add_headers({'Content-Type': 'application/json'})

        res = sender.build(REQUEST_TYPE, REQUEST_PATH)
        self.response = res

        payload = json.loads(res.text)

        assert_valid_response(res, STATUS_CODE_BAD_REQUEST, CONTENT_TYPE_JSON)
        assert_valid_schema(payload, 'error.json')
