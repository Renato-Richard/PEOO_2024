from models.crud import CRUD
import json
from datetime import datetime, date
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
        if isinstance(self.__formed_date, date):
            dic["formed_date"] = self.__formed_date.strftime("%d/%m/%Y")
        else:
            dic["formed_date"] = self.__formed_date
        dic["members_count"] = self.__members_count
        dic["total_shows_by_band"] = self.__total_shows_by_band
        dic["band_status"] = self.__band_status
        if isinstance(self.__updated_at, datetime):
            dic["updated_at"] = self.__updated_at.strftime("%d/%m/%Y %H:%M")
        else:
            dic["updated_at"] = self.__updated_at
        return dic
    def years_in_the_industry(self):
        return datetime.now().year - self.__formed_date.year
    def update_total_shows_by_band(self):
        return self.__total_shows_by_band
    def search_shows_by_band(band_name):
        shows = Bands.open()
        filtered_shows = [show for show in shows if band_name.lower() in show['band_name'].lower()]
        return filtered_shows
    def __str__(self):
        return f"{self.id} - {self.__band_name} - {self.__music_genre} - {self.__description} - {self.__formed_date} - {self.__members_count} - {self.__total_shows_by_band} - {self.__band_status} - {self.__updated_at}"
class Bands(CRUD):
    @classmethod
    def save(cls):
        with open("json/bands.json", mode="w") as file:
            json.dump([obj.to_json() for obj in cls.objetos], file, default=str, indent=4)
    @classmethod
    def open(cls):
        cls.objetos = []
        try:
            with open("json/bands.json", mode="r") as file:
                text = json.load(file)
            for obj in text:   
                b = Band(obj["id"], obj["band_name"], obj["music_genre"], obj["description"], obj["formed_date"], obj["members_count"], obj["total_shows_by_band"], obj["band_status"], obj["updated_at"])
                cls.objetos.append(b)
        except FileNotFoundError:
            pass