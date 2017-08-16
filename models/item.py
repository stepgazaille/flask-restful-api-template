"""
| Created: 2017-08-13
| Updated: 2017-08-13
"""
from db import db


class ItemModel(db.Model):
    """Item model."""

    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))

    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
    store = db.relationship('StoreModel')

    def __init__(self, name, price, store_id):
        self.name = name
        self.price = price
        self.store_id = store_id

    def json(self):
        """
        Converts this item to JSON.

        :return: this item.
        :rtype: JSON.
        """
        return {'name': self.name, 'price': self.price}

    @classmethod
    def find_by_name(cls, name):
        """
        Selects an item from the DB and returns it.

        :param name: the name of the item.
        :type name: str
        :return: an item.
        :rtype: ItemModel.
        """
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        """
        Inserts this item in the DB.
        """
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        """
        Deletes this item from the DB.
        """
        db.session.delete(self)
        db.session.commit()
