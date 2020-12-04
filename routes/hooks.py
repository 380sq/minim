from flask import Blueprint, request

from lib import public_endpoint

hooks = Blueprint('hooks', __name__)


@public_endpoint
@hooks.route('/hook', methods=["POST", "GET"])
def hook():
    print(">>>>>>>>>>>>>>>>>>>>")
    print(request.json())
    print(request.json())
