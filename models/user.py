"""
| Created: 2017-08-13
| Updated: 2017-08-13
"""
from db import db


class UserModel(db.Model):
    """User model."""

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))

    def __init__(self, username, password):
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username):
        """
        Selects a user from the DB and returns it.

        :param username: the username of the user.
        :type username: str
        :return: a user.
        :rtype: UserModel.
        """
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, _id):
        """
        Selects a user from the DB and returns it.

        :param _id: the id of the user.
        :type _id: int
        :return: a user.
        :rtype: UserModel.
        """
        return cls.query.filter_by(id=_id).first()

    def save_to_db(self):
        """
        Inserts this user in the DB.
        """
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        """
        Deletes this user from the DB.
        """
        db.session.delete(self)
        db.session.commit()
