

class JWT:
    def __init__(self, secret_key):     # we will then init the JWT with .env variable
        self.secret_key = secret_key


    def _packHeader(self, algorithm="HS256", type="JWT"):

        header = {}
        
        return header


    def sign(self, header, payload):
        
        # encode header + payload + secret_key

        return signedToken


    def _validate(self, token):
        header, payload, signature = token.split(".")

        expected_signature = ...

        return expected_signature == signature


    def extract_data(self, token):

        if not token._validate:
            raise ...

        # decode the header and payload

        return header, payload  # do I need to return the header???