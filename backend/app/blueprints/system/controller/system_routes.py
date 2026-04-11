from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from app.blueprints.system.services.service import SessionService, NotificationService
from app.blueprints.system.schemas import session_schema, sessions_schema, notification_schema, notifications_schema

session_bp = Blueprint('sessions', __name__)



# Get all sessions
@session_bp.get('/')
def get_all_sessions():
    try:
        sessions = SessionService.get_all_sessions()
        return jsonify(sessions_schema.dump(sessions)), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Get a specific session
@session_bp.get('/<session_id>')
def get_session(session_id):
    try:
        session = SessionService.get_session(session_id)
        
        if not session:
            return jsonify({'error': 'Session not found'}), 404
        
        return jsonify(session_schema.dump(session)), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Create a new session
@session_bp.post('/')
def create_session():
    try:
        data = request.get_json()
        
        validated_data = session_schema.load(data)
        
        session = SessionService.create_session(validated_data)
        
        return jsonify(session_schema.dump(session)), 201
    
    except ValidationError as err:
        return jsonify({'error': err.messages}), 400
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Update an existing session
@session_bp.put('/<session_id>')
def update_session(session_id):
    try:
        data = request.get_json()
            
        if not data:
            return jsonify({'error': 'No input data provided'}), 400
        
        validated_data = session_schema.load(data)
        
        session = SessionService.update_session(session_id, validated_data)
        
        if not session:
            return jsonify({'error': 'Session not found'}), 404
        
        
        return jsonify(session_schema.dump(session)), 200
    
    except ValidationError as err:
        return jsonify({'error': err.messages}), 400
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Delete a session
@session_bp.delete('/<session_id>')
def delete_session(session_id):
    try:
        session = SessionService.get_session(session_id)
        
        if not session:
            return jsonify({'error': 'Session not found'}), 404
        
        SessionService.delete_session(session_id)
        return jsonify({'message': 'Session deleted successfully'}), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
    

notification_bp = Blueprint('notification', __name__)



# Get all notifications
@notification_bp.get('/')
def get_all_notifications():
    try:
        notifications = NotificationService.get_all_notifications()
        return jsonify(notifications_schema.dump(notifications)), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Get a specific notification
@notification_bp.get('/<notification_id>')
def get_notification(notification_id):
    try:
        notification = NotificationService.get_notification(notification_id)
        
        if not notification:
            return jsonify({'error': 'Notification not found'}), 404
        
        return jsonify(notification_schema.dump(notification)), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Create a new notification
@notification_bp.post('/')
def create_notification():
    try:
        data = request.get_json()
        
        validated_data = notification_schema.load(data)
        
        notification = NotificationService.create_notification(validated_data)
        
        return jsonify(notification_schema.dump(notification)), 201
    
    except ValidationError as err:
        return jsonify({'error': err.messages}), 400
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Update an existing notification
@notification_bp.put('/<notification_id>')
def update_notification(notification_id):
    try:
        data = request.get_json()
            
        if not data:
            return jsonify({'error': 'No input data provided'}), 400
        
        validated_data = notification_schema.load(data)
        
        notification = NotificationService.update_notification(notification_id, validated_data)
        
        if not notification:
            return jsonify({'error': 'Notification not found'}), 404
        
        
        return jsonify(notification_schema.dump(notification)), 200
    
    except ValidationError as err:
        return jsonify({'error': err.messages}), 400
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Delete a notification
@notification_bp.delete('/<notification_id>')
def delete_notification(notification_id):
    try:
        notification = NotificationService.get_notification(notification_id)
        
        if not notification:
            return jsonify({'error': 'Notification not found'}), 404
        
        NotificationService.delete_notification(notification_id)
        return jsonify({'message': 'Notification deleted successfully'}), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500