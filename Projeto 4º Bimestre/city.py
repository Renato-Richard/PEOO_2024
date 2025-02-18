class City:
    def __init__(self, city_id: id, city_name: str, total_shows_by_city: int, updated_at):
        self.__city_id = city_id
        self.__city_name = city_name
        self.__total_shows_by_city = total_shows_by_city
        self.__updated_at = updated_at
    def to_json(self):
        dic = {}
    def __str__(self):
        return f"{self.__city_id} - {self.__city_name} - {self.__total_shows_by_city} - {self.__updated_at}"