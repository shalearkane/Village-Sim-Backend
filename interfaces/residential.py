from interfaces import Base

class Residential:
    def __init__(self, key: str, type: str, floors: int, boundaryPoints: list, centralPoint: list, metadata: Base):
        self.key = key
        self.type = type
        self.floors = floors
        self.boundaryPoints = boundaryPoints
        self.centralPoint = centralPoint
        self.metadata = metadata
    
    def to_dict(self):
        return {
            "key": self.key,
            "type": self.type,
            "floors": self.floors,
            "boundaryPoints": self.boundaryPoints,
            "centralPoint": self.centralPoint,
            "metadata": self.metadata.to_dict()
        }