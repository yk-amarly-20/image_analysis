class LocationLengthException(Exception):
    def __str__(self):
        return "location length must be 2"
