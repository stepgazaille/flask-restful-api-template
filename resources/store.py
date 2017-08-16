"""
| Created: 2017-08-13
| Updated: 2017-08-13
"""
from flask_restful import Resource
from models.store import StoreModel


class Store(Resource):
    """Stores' endpoint."""

    def get(self, name):
        """
        Finds a store by its name and returns it.

        :param name: the name of the store.
        :type name: str
        :return: store data.
        :rtype: application/json.
        """
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        return {'message': 'Store not found'}, 404

    def post(self, name):
        """
        Creates a new store using the provided name and list of items.

        :param name: the name of the store.
        :type name: str
        :param items: the store's initial list of items.
        :type items: str list
        :return: success or failure message.
        :rtype: application/json response.
        """
        if StoreModel.find_by_name(name):
            return {
                'message': "A store with name '{}' already exists."
                           .format(name)
            }, 400

        store = StoreModel(name)

        try:
            store.save_to_db()
        except:
            return {'message': 'An error occurred inserting the store.'}, 500

        return store.json(), 201

    def delete(self, name):
        """
        Finds a store by its name and deletes it.

        :param name: the name of the store.
        :type name: str
        :return: success or failure message.
        :rtype: application/json response.
        """
        store = StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()
        return {'message': 'Store deleted'}


class StoreList(Resource):
    """Stores' list endpoint."""

    @classmethod
    def get(cls):
        """
        Returns a list of all stores.

        :return: all stores' data.
        :rtype: application/json.
        """
        return {'stores': [store.json() for store in StoreModel.query.all()]}
