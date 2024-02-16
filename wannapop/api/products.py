from . import api_bp
from .errors import not_found
from ..models import Product, Category, BannedProduct, Status
from .helper_json import json_response
from flask import current_app, request

# Llistar productes i filtrar pel títolo
@api_bp.route('/products', methods=['GET'])
def get_prod_list():
    search = request.args.get('title')
    if search:
        # Watch SQL at terminal
        Product.db_enable_debug()
        # Filter using query param
        my_filter = Product.title.like('%' + search + '%')
        # items_with_store = Product.db_query_with(Category).filter()
        #producto = Product.get_with(search, [Category, Status], BannedProduct)
        products = Product.db_query_with(Category).filter(my_filter)

    else:
        # No filter
        products = Product.get_all_with(Category, BannedProduct)
    data = Product.to_dict_collection(products)
    return json_response(data)
#Veure els detalls d’un producte
@api_bp.route('/products/<int:id>', methods=['GET'])
def get_prod_id(id):
    result = Product.get_with(id)
    if result:
        data = Product.get_with(id, [Category, Status], BannedProduct)

        # data = Product.db_query_with(Category).filter(id)
        # (product, category, status, banned) = result
        # # Serialize data
        # data = Product.to_dict(result)
        # Add relationships
        # data["Category"] = Product.to_dict()
        # # (item, store, discount) = result
        # # Serialize data
        # data = Product.to_dict()
        # # Add relationships
        # data["Category"] = Product.to_dict()
        # # del data["prodd"]
        # # if (discount):
        # #     data["discount"] = discount.discount
        return json_response(data)
    else:
        current_app.logger.debug("Product {} not found".format(id))
        return not_found("Product not found")

    # search = request.args.get('title')
    # if search:
    #     # Watch SQL at terminal
    #     Product.db_enable_debug()
    #     # Filter using query param
    #     my_filter = Product.title.like('%' + search + '%')
    #     # items_with_store = Product.db_query_with(Category).filter()
    #     #producto = Product.get_with(search, [Category, Status], BannedProduct)
    #     products = Product.db_query_with(Category).filter(my_filter)

    # else:
    #     # No filter
    #     products = Product.get_all_with(Category, BannedProduct)
    # data = Product.to_dict_collection(products)
    # return json_response(data)

