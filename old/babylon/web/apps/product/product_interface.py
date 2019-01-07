from web.utils.custom_exceptions import ValidationError, NonExistingResource
from web.apps.product.product_model import ProductModel, product_serializer


class ProductInterface:
    """
    Interface to the model
    """

    def __init__(self, session):
        self.session = session

    def get(self, product_id):
        product_query_set = self.session.query(ProductModel).get(product_id)
        if not product_query_set:
            raise NonExistingResource("Product id {} not found".format(product_id))
        data, errors = product_serializer.dump(product_query_set)
        return data

    def get_all(self):
        data, errors = product_serializer.dump(
            self.session.query(ProductModel).all(), many=True
        )
        return data

    def delete(self, product_id):
        product = self.session.query(ProductModel).get(product_id)
        if not product:
            raise NonExistingResource("Product {} not found".format(product_id))
        else:
            self.session.delete(product)
            return product_serializer.dump(product).data

    def add(self, new_data):
        new_data, errors = product_serializer.load(new_data)
        if errors:
            raise ValidationError(errors)

        new_product = ProductModel(**new_data)
        self.session.add(new_product)
        return new_data

    def update(self, product_id, new_data):
        """
        :param product_id:
        :param new_data: type dict
        :return:
        """
        existing_object = self.session.query(ProductModel).get(product_id)
        if not existing_object:
            raise NonExistingResource("Product {} not found".format(product_id))

        for key, value in new_data.items():
            setattr(existing_object, key, value)

        new_data, errors = product_serializer.dump(existing_object)
        if errors:
            raise ValidationError(errors)

        return new_data

    def initial_state(self):
        products = [
            {"name": "Lavender heart", "price": "9.25"},
            {"name": "Personalised cufflinks", "price": "45.00"},
            {"name": "Kids T-shirt", "price": "19.95"},
        ]
        for product in products:
            self.add(new_data=product)
