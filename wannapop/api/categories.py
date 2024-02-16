from . import api_bp
from .errors import not_found
from ..models import Category
from .helper_json import json_response
from flask import current_app

# Lista Category
@api_bp.route('/categories', methods=['GET'])
def get_category_list():
    Ordern = Category.get_all()
    data = Category .to_dict_collection(Ordern)
    return json_response(data)
