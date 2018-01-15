from flask import Blueprint, request, jsonify, current_app

from ....models.user import User, UserSchema, UserNotificationSchema
from ....utils.get_model_or_404 import get_model_or_404

from descriptions import GET_USER_DESCRIPTIONS, GET_USER_NOTIFICATIONS_DESCRIPTIONS

app = Blueprint('user', __name__)


@app.route('/api/users/<int:id>')
def get_user(id):
  query = User.query.filter_by(id=id).one_or_none()
  if (query is not None):
    schema = UserSchema()
    user_serialized = schema.dump(query)
    
    return jsonify({
      'status': 200,
      'description': GET_USER_DESCRIPTIONS['SUCCESS'],
      'payload': user_serialized.data
    }), 200

  else:
    return jsonify({
    'status' : 404,
    'description': GET_USER_DESCRIPTIONS['NOT_FOUND']   
  }), 404


@app.route('/api/users/<int:id>/notifications')
def get_user_notifications(id):
  query = get_model_or_404(User, id)

  schema = UserNotificationSchema()
  notifications_serialized = schema.dump(query)

  if (len(notifications_serialized.data['notification']) > 0):
    return jsonify({
      'status': 200,
      'description': GET_USER_NOTIFICATIONS_DESCRIPTIONS['SUCCESS'],
      'payload': notifications_serialized.data
    }), 200

  else:
    return jsonify({
    'status': 404,
    'description': GET_USER_NOTIFICATIONS_DESCRIPTIONS['NOT_FOUND']
  }), 404