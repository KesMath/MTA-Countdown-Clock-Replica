from requests.auth import AuthBase

HEADER_KEY = 'x-api-key'

class TokenAuth(AuthBase):
    """Implements a custom authentication scheme.
        'HEADER_KEY: token' will be used to format header dictionary of request object"""

    def __init__(self, token):
        self.token = token

    def __call__(self, r):
        """Attach an API token to a custom auth header."""
        r.headers[HEADER_KEY] = f'{self.token}'
        return r