import json
import os

from jsonschema import validate, RefResolver

def get_resolver(schema):
    schema = schema

    schema_path = 'file:////{0}/schemas/'.format(
            os.path.dirname(__file__))

    resolver = RefResolver(schema_path, schema)

    return resolver

def assert_valid_schema(data, schema_file):
    """ Checks whether the given data matches the schema """

    schema = _load_json_schema(schema_file)
    return validate(data, schema, resolver=get_resolver(schema_file))

def _load_json_schema(filename):
    """Loads the given schema file"""

    relative_path = os.path.join('schemas', filename)
    absolute_path = os.path.join(os.path.dirname(__file__), relative_path)

    with open(absolute_path) as schema_file:
        return json.loads(schema_file.read())

def assert_valid_response(response, status_code, content_type):
    msg = ""
    if response.status_code != status_code:
        msg += f"Expected status code - {status_code}\nActual status code - "\
                f"{response.status_code}\n"

    if response.headers['Content-Type'] != content_type:
        msg += f"Expected Content-Type - {content_type}\nActual status code - "\
                f"{response.headers['Content-Type']}"

    if len(msg) != 0:
        raise AssertionError(msg)

def get_from_db(conn):
    cursor = conn.cursor()
    cursor.execute('SELECT result as user_action, feedback, device \
            FROM t_feedback_models ORDER BY id DESC LIMIT 1;')
    record = cursor.fetchone()
    cursor.close()

    row = {}
    row["user_action"] = str(record[0])
    row["feedback"] = record[1]
    row["device"] = record[2]

    return row

def assert_from_db(conn, user_action, feedback, device_type=""):
    result = get_from_db(conn)
    msg = ""

    if result["user_action"] != user_action:
        msg += f"params from request - 'user_action': '{user_action}'\nparams "\
                f"from DB - 'user_action': '{result['user_action']}'\n"

    if result["feedback"] != feedback:
        if len(set([result["feedback"], feedback]) - set(['', None])) != 0:
            msg += f"params from request - 'feedback': '{feedback}'\nparams "\
                    f"from DB - 'feedback': '{result['feedback']}'\n"

    if device_type:
        if result["device"] != device_type:
            msg += f"User-Agent - '{device_type}'\n device from DB - "\
                    f"'device': '{result['device']}'\n"

    if len(msg) != 0:
        raise AssertionError(msg)
