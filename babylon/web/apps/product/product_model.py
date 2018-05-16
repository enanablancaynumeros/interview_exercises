from sqlalchemy import Column, Integer, String
from marshmallow import Schema, fields

from web.app import db


class ProductModel(db.Model):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100))
    price = Column(String(10))


class ProductSchema(Schema):
    id = fields.Int(required=False)
    name = fields.Str(required=True)
    price = fields.Str(required=True)


product_serializer = ProductSchema()
