from models.crud import CRUD
import json
from datetime import datetime
class Band:
    def __init__(self, id: int, band_name: str, music_genre: str, description: str, formed_date: str, members_count: int, total_shows_by_band: int, band_status: str, updated_at):
        self.id = id
        self.__band_name = band_name
        self.__music_genre = music_genre
        self.__description = description
        self.__formed_date = formed_date
        self.__members_count = members_count
        self.__total_shows_by_band = total_shows_by_band
        self.__band_status = band_status
        self.__updated_at = updated_at
    def to_json(self):
        dic = {}
        dic["id"] = self.id
        dic["band_name"] =  self.__band_name
        dic["music_genre"] = self.__music_genre
        dic["description"] = self.__description
        dic["formed_date"] = self.__formed_date.data().strftime("%d/%m/%Y")
        dic["members_count"] = self.__members_count
        dic["total_shows_by_band"] = self.__total_shows_by_band
        dic["band_status"] = self.__band_status
        dic["updated_at"] = self.__updated_at.datetime().strftime("%d/%m/%Y %H:%M")
        return dic
    def years_in_the_industry(self):
        return datetime.now().year - self.__formed_date.year
    def update_total_shows_by_band(self):
        return self.__total_shows_by_band
    def search_shows_by_band():
        pass
    def update_updated_at():
        pass
    def __str__(self):
        return f"{self.id} - {self.__band_name} - {self.__music_genre} - {self.__description} - {self.__formed_date} - {self.__members_count} - {self.__total_shows_by_band} - {self.__band_status} - {self.__updated_at}"
class Bands(CRUD):
    @classmethod
    def save(cls):
        with open("json/bands.json", mode="w") as file:
            json.dump(cls.objetos, file, default = vars)
    @classmethod
    def open(cls):
        cls.objetos = []
        try:
            with open("json/bands.json", mode="r") as file:
                text = json.load(file)
            for obj in text:   
                b = Band(obj["id"], obj["_Band__band_name"], obj["_Band__music_genre"], obj["_Band__description"], obj["_Band__formed_date"], obj["_Band__members_count"], obj["_Band__total_shows_by_band"], obj["_Band__band_status"], obj["_Band__updated_at"])
            cls.objetos.append(b)
        except FileNotFoundError:
            pass