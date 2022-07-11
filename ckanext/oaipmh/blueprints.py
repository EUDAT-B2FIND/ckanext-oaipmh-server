from flask import Blueprint

oai = Blueprint('oai', __name__)

@oai.route('/oai', endpoint='b2find_oai', methods=['POST', 'GET'])

def b2find_oai():
	return {}
