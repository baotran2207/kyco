

from chalice import Blueprint, Chalice

from chalicelib.dynamo_db.base import dynamodb_table
users_blueprints = Blueprint(__name__)


@users_blueprints.route('/users', methods=['POST'])
def create_user():
    request = users_blueprints.current_app.current_request.json_body
    item = {
        'PK': 'User#%s' % request['username'],
        'SK': 'Profile#%s' % request['username'],
    }
    item.update(request)
    dynamodb_table.put_item(Item=item)
    return item


@users_blueprints.route('/users/{username}', methods=['GET'])
def get_user(username):
    key = {
        'PK': 'User#%s' % username,
        'SK': 'Profile#%s' % username,
    }
    item = dynamodb_table.get_item(Key=key)['Item']
    del item['PK']
    del item['SK']
    return item



