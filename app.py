from flask import Flask
from flask_restful import Resource, Api
import json
from uuid import uuid4

app = Flask(__name__)
api = Api(app)


class Quote(Resource):
    def get(self, key=None):
        if key is None:
            return json.dumps(dict(
                error="""You didn't include an API key as a GET request
                parameter \"key\". Get one by making a PUT request to
                https://www.quotablemises.com/auth?agentName=<user_agent_name>.
                You can make up whatever user agent name you like. This is
                just to track usage for my own curiosity and to avoid abuse
                of the service."""))
        if exists(key):
            return json.dumps(dict(
                body="test",
                citation="test",
                topic="test"))

    def put(self, body, citation, topic):
        return json.dumps(dict(
            success=True))


class Auth(Resource):
    def get(self, agentName):
        return json.dumps(dict(key=str(uuid4())))


def exists(key):
    return True


api.add_resource(Quote, '/')
api.add_resource(Auth, '/auth/<string:agentName>')

app.run()
