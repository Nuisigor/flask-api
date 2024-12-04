from flask import request, jsonify
from src.config.settings.environment import Environment

class ApiKeyMiddleware:
    def __init__(self):
        pass

    def __call__(self, f):
        def wrapper(*args, **kwargs):
            provided_api_key = request.headers.get("API-KEY")
            if not provided_api_key:
                return jsonify({"message": "API-KEY não fornecida"}), 401
            if provided_api_key != Environment.API_KEY:
                return jsonify({"message": "API-KEY inválida"}), 403
            return f(*args, **kwargs)
        return wrapper

