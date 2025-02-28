from models.band import Band, Bands
from models.city import City, Cities
from models.show import Show, Shows
from models.user import User, Users
from models.ticket import Ticket, Tickets

class View:
    def create_band(band_name, music_genre, description, formed_date, members_count, total_shows_by_band, band_status):
        b = Band(0, band_name, music_genre, description, formed_date, members_count, total_shows_by_band, band_status, "")
        Bands.create(b)
    def read_band():
        return Bands.read() 
    def read_ID_band(band_id):
        return Bands.read_ID(band_id)
    def update_band(band_id, band_name, music_genre, description, formed_date, members_count, total_shows_by_band, band_status):
        b = Band(band_id, band_name, music_genre, description, formed_date, members_count, total_shows_by_band, band_status, "")
        Bands.update(b)
    def delete_band(band_id):
        b = Band(band_id, "", "", "", "", "", "", "", "")
        Bands.delete(b)

    def create_city(city_name, total_shows_by_city):
        c = City(0, city_name, total_shows_by_city, "")
        Cities.create(c)
    def read_city():
        return Cities.read() 
    def read_ID_city(city_id):
        return Cities.read_ID(city_id)
    def update_city(city_id, city_name, total_shows_by_city):
        c = City(city_id, city_name, total_shows_by_city, "")
        Cities.update(c)
    def delete_city(city_id):
        c = City(city_id, "", "", "")
        Cities.delete(c)

    def create_show(description_of_show, show_date, show_time, is_virtual, available_tickets, ticket_price, sold_tickets, show_status):
        s = Show(0, 0, 0, description_of_show, show_date, show_time, is_virtual, available_tickets, ticket_price, sold_tickets, show_status, "")
        Shows.create(s)
    def read_show():
        return Shows.read()
    def read_ID_show(show_id):
        return Shows.read_ID(show_id)
    def update_show(show_id, band_id, city_id, description_of_show, show_date, show_time, is_virtual, available_tickets, ticket_price, sold_tickets, show_status):
        s = Show(show_id, band_id, city_id, description_of_show, show_date, show_time, is_virtual, available_tickets, ticket_price, sold_tickets, show_status, "")
        Shows.update(s)
    def delete_show(show_id):
        s = Show(show_id, "", "", "", "", "", "", "", "", "", "", "")
        Shows.delete(s)

    def create_user(user_name, email, password, birth_date):
        u = User(0, user_name, email, password, birth_date)
        Users.create(u)
    def read_user():
        return Users.read()
    def read_ID_user(user_id):
        return Users.read_ID(user_id)
    def update_user(user_id):
        u = User(user_id)
        Users.update(u)
    def delete_user(user_id):
        u = User(user_id)
        Users.delete(u)

    def create_ticket():
        t = Ticket(0)
        Tickets.create(t)
    def read_ticket():
        return Tickets.read()
    def read_ID_ticket(ticket_id):
        return Tickets.read_ID(ticket_id)
    def update_ticket(ticket_id):
        t = Ticket(ticket_id)
        Tickets.update(t)
    def delete_ticket(ticket_id):
        t = Ticket(ticket_id)
        Tickets.delete(t)

    def authenticate_user(email, password):
        for c in View.read_user():
            if c._User__email == email and c._User__password == password:
                return {"id" : c.id, "nome" : c._User__user_name }
        return None
    def authenticate_admin(email, password):
        for c in View.read_user():
            if c._User__email == email and c._User__password == password:
                return {"id" : c.id, "nome" : c._User__user_name }
        return None