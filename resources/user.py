"""
| Created: 2017-08-13
| Updated: 2017-08-13
"""
from flask_restful import Resource, reqparse

from models.user import UserModel


class UserRegister(Resource):
    """Users' endpoint."""

    parser = reqparse.RequestParser()
    parser.add_argument(
        'username',
        type=str,
        required=True,
        help="This field cannot be left blank!")
    parser.add_argument(
        'password',
        type=str,
        required=True,
        help="This field cannot be left blank!")

    def post(self):
        """
        Creates a new user using the provided username and password.

        :return: success or failure.
        :rtype: application/json response.
        """
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {
                'message':
                "A user with name '{}' already exists."
                .format(data['username'])
            }, 400

        user = UserModel(**data)  # data['username'], data['password']
        user.save_to_db()

        return {"message": "User created successfully."}, 201

    def delete(self):
        """
        Finds a user by its username and deletes it.

        :param username: the username of the user.
        :type username: str
        :return: success or failure.
        :rtype: application/json response.
        """
        data = UserRegister.parser.parse_args()
        user = UserModel.find_by_username(data['username'])

        if user:
            user.delete_from_db()

        return {'message': 'User deleted'}
