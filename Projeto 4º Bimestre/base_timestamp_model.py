class BaseTimestampModel():
    def __init__(self):
        self.__update_at = None
    def update_updated_at(self):
        from datetime import datetime
        self.__update_at = datetime.now()
    def get_updated_at(self):
        return self.__update_at