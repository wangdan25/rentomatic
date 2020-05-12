from rentomatic.shared.domain_model import DomainModel
from typing import Dict


class StorageRoom(object):

    def __init__(self, code: str, size: int, price: int, latitude: float, longitude: float):
        self.code = code
        self.size = size
        self.price = price
        self.latitude = latitude
        self.longitude = longitude

    @classmethod
    def from_dict(cls, adict) -> StorageRoom:
        room = StorageRoom(
            code=adict['code'],
            size=adict['size'],
            price=adict['price'],
            latitude=adict['latitude'],
            longitude=adict['longitude'],
        )

        return room

    def to_dict(self) -> dict:
        return {
            'code': self.code,
            'size': self.size,
            'price': self.price,
            'latitude': self.latitude,
            'longitude': self.longitude,
        }

    def __eq__(self, other) -> bool:
        return self.to_dict() == other.to_dict()


DomainModel.register(StorageRoom)
