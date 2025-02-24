from models.crud import CRUD
import json
class Band:
    def __init__(self, band_id: int, band_name: str, music_genre: str, description: str, formed_date: str, members_count: int, total_shows_by_band: int, band_status: str, updated_at):
        self.__band_id = band_id
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
    def __str__(self):
        return f"{self.__band_id} - {self.__band_name} - {self.__music_genre} - {self.__description} - {self.__formed_date} - {self.__members_count} - {self.__total_shows_by_band} - {self.__band_status} - {self.__updated_at}"
class Bands(CRUD):
    @classmethod
    def save(cls):
        with open("bands.json", mode="w") as file:
            json.dump(cls.objetos, file, default = vars)
    @classmethod
    def open(cls):
        cls.objetos = []
        try:
            with open("bands.json", mode="r") as file:
                text = json.load(file)
            for obj in text:   
                b = Band(obj["band_id"], obj["band_name"], obj["music_genre"], obj["description"], obj["formed_date"], obj["members_count"], obj["total_shows_by_band"], obj["band_status"], obj["updated_at"])
            cls.objetos.append(b)
        except FileNotFoundError:
            pass