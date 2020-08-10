
class FileExtensionException(Exception):
    """Raised when a given file extension does not match expected"""
    pass


class RouteIdException(Exception):
    """Raised when a route id/train number does not exist or is not supported by app"""
    pass