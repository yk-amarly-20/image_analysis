class ColorLengthException(Exception):
    def __str__(self):
        return "color list length must be 3"
