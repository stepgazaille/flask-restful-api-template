"""
| Created: 2017-08-13
| Updated: 2017-08-13
"""
from db import db


class StoreModel(db.Model):
    """Store model."""

    __tablename__ = 'stores'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    items = db.relationship('ItemModel', lazy='dynamic')

    def __init__(self, name):
        self.name = name

    def json(self):
        """
        Converts this store and all its items to JSON.

        :return: this store and all its items.
        :rtype: JSON.
        """
        return {'name': self.name,
                'items': [item.json() for item in self.items.all()]}

    @classmethod
    def find_by_name(cls, name):
        """
        Selects a store from the DB and returns it.

        :param name: the name of the store.
        :type name: str
        :return: a store.
        :rtype: StoreModel.
        """
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        """
        Inserts this store in the DB.
        """
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        """
        Deletes this store from the DB.
        """
        db.session.delete(self)
        db.session.commit()
