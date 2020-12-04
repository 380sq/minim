from flask import Blueprint, request

from lib import public_endpoint

hooks = Blueprint('hooks', __name__)


@public_endpoint
@hooks.route('/hook', methods=["POST", "GET"])
def hook():
    print("HOOKS")
    print("HOOKS")
    print("HOOKS")
    print(request.json)
    print("################# HOOKS")
