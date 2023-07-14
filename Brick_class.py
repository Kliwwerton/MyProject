

class Brick:
    """Class Brick. Creates a Brick class during initialization."""

    def __init__(self):
        self.name = None
        """Name of the Brick shape"""
        self.gost = None
        """Number of gost"""
        self.number = None
        """Number of the shape on gost"""
        self.size = []
        """Size of the Brick"""
        self.square = None
        """Square of the Brick (pressure square)"""
        self.volume = None
        """Volume of the Brick"""
        self.weight = None
        """Weight of the Brick"""
        self.volume_weight = None
        """volume_weight of the Brick"""

    def calculate_square(self):
        pass
