from flask import Blueprint, request, jsonify
from .service import RatingsService
from .schema import RatingSchema


ratings_bp = Blueprint('ratings', __name__)
schema = RatingSchema()
schema_many = RatingSchema(many=True)


# Get all ratings
@ratings_bp.route('/', methods=['GET'])
def get_ratings():
    try:
        ratings = RatingsService.get_all_ratings()
        return jsonify(schema_many.dump(ratings)), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Get a specific rating
@ratings_bp.route('/<rating_id>', methods=['GET'])
def get_rating(rating_id):
    try:
        rating = RatingsService.get_rating(rating_id)
        if not rating:
            return jsonify({'error': 'Rating not found'}), 404
        return jsonify(schema.dump(rating)), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Create a new rating
@ratings_bp.route('/', methods=['POST'])
def create_rating():
    try:
        data = request.get_json()
        rating = RatingsService.create_rating(data)
        return jsonify(schema.dump(rating)), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Update an existing rating
@ratings_bp.route('/<rating_id>', methods=['PUT'])
def update_rating(rating_id):
    try:
        data = request.get_json()
        rating = RatingsService.update_rating(rating_id, data)
        if not rating:
            return jsonify({'error': 'Rating not found'}), 404
        return jsonify(schema.dump(rating)), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Delete a rating
@ratings_bp.route('/<rating_id>', methods=['DELETE'])
def delete_rating(rating_id):
    try:
        rating = RatingsService.get_rating(rating_id)
        if not rating:
            return jsonify({'error': 'Rating not found'}), 404
        RatingsService.delete_rating(rating_id)
        return jsonify({'message': 'Rating deleted successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500