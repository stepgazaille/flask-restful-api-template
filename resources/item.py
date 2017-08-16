"""
| Created: 2017-08-13
| Updated: 2017-08-13
"""
from flask_jwt import jwt_required
from flask_restful import Resource, reqparse
from models.item import ItemModel


class Item(Resource):
    """Items' endpoint."""

    parser = reqparse.RequestParser()
    parser.add_argument(
        'price',
        type=float,
        required=True,
        help="This field cannot be left blank!"
    )
    parser.add_argument(
        'store_id',
        type=int,
        required=True,
        help="Every item needs a store id."
    )

    @jwt_required()
    def get(self, name):
        """
        Finds an item by its name and returns it.

        :param name: the name of the item.
        :type name: str
        :return: item data.
        :rtype: application/json.
        """
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {'message': 'Item not found'}, 404

    def post(self, name):
        """
        Creates a new item using the provided name, price and store_id.

        :param name: the name of the item.
        :type name: str
        :param price: the item's price.
        :type items: float
        :param store_id: the item's parent store.
        :type store_id: int
        :return: success or failure message.
        :rtype: application/json response.
        """
        if ItemModel.find_by_name(name):
            return {'message': "An item with name '{}' already exists."
                               .format(name)}, 400
        request_data = Item.parser.parse_args()

        item = ItemModel(name, **request_data)

        try:
            item.save_to_db()
        except:
            return {'message': 'An error occurred inserting the item.'}, 500

        return item.json(), 201

    def delete(self, name):
        """
        Finds an item by its name and deletes it.

        :param name: the name of the item.
        :type name: str
        :return: success or failure message.
        :rtype: application/json response.
        """
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
        return {'message': 'Item deleted'}

    def put(self, name):
        """
        Creates or updates an item using the provided name, price and store_id.

        :param name: the name of the item.
        :type name: str
        :param price: the item's price.
        :type items: float
        :param store_id: the item's parent store.
        :type store_id: int
        :return: success or failure message.
        :rtype: application/json response.
        """
        request_data = Item.parser.parse_args()
        item = ItemModel.find_by_name(name)

        if item is None:
            item = ItemModel(name, **request_data)
        else:
            item.price = request_data['price']
            item.store_id = request_data['store_id']
        item.save_to_db()
        return item.json()


class ItemList(Resource):
    """Stores' list endpoint."""

    @classmethod
    def get(cls):
        """
        Returns a list of all items.

        :return: all stores' data.
        :rtype: application/json.
        """
        return {'items': [item.json() for item in ItemModel.query.all()]}
