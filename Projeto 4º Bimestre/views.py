from datetime import datetime
from models.band import Band, Bands
from models.city import City, Cities
from models.show import Show, Shows
from models.user import User, Users
from models.ticket import Ticket, Tickets
import streamlit as st
class View:
    @staticmethod
    def create_band(band_name, music_genre, description, formed_date, members_count, total_shows_by_band, band_status, updated_at):
        b = Band(0, band_name, music_genre, description, formed_date, members_count, total_shows_by_band, band_status, updated_at)
        Bands.create(b)
    @staticmethod
    def read_band():
        return Bands.read()
    @staticmethod
    def read_ID_band(band_id):
        return Bands.read_ID(band_id)
    @staticmethod
    def update_band(band_id, band_name, music_genre, description, formed_date, members_count, total_shows_by_band, band_status):
        b = Band(band_id, band_name, music_genre, description, formed_date, members_count, total_shows_by_band, band_status, "")
        Bands.update(b)
    @staticmethod
    def delete_band(band_id):
        b = Band(band_id, "", "", "", "", "", "", "", "")
        Bands.delete(b)
    @staticmethod
    def create_city(city_name, total_shows_by_city, updated_at):
        c = City(0, city_name, total_shows_by_city, updated_at)
        Cities.create(c)
    @staticmethod
    def read_city():
        return Cities.read()
    @staticmethod
    def read_ID_city(city_id):
        return Cities.read_ID(city_id)
    @staticmethod
    def update_city(city_id, city_name, total_shows_by_city, updated_at):
        c = City(city_id, city_name, total_shows_by_city, updated_at)
        Cities.update(c)
    @staticmethod
    def delete_city(city_id):
        c = City(city_id, "", "", "")
        Cities.delete(c)
    @staticmethod
    def create_show(band_id, city_id, description_of_show, show_date, show_time, is_virtual, available_tickets, ticket_price, sold_tickets, show_status, update_at):
        s = Show(band_id, city_id, 0, description_of_show, show_date, show_time, is_virtual, available_tickets, ticket_price, sold_tickets, show_status, update_at)
        Shows.create(s)
    @staticmethod
    def read_show():
        return Shows.read()
    @staticmethod
    def read_ID_show(show_id):
        return Shows.read_ID(show_id)
    @staticmethod
    def update_show(show_id, band_id, city_id, description_of_show, show_date, show_time, is_virtual, available_tickets, ticket_price, sold_tickets, show_status, update_at):
        s = Show(show_id, band_id, city_id, description_of_show, show_date, show_time, is_virtual, available_tickets, ticket_price, sold_tickets, show_status, update_at)
        Shows.update(s)
    @staticmethod
    def delete_show(show_id):
        s = Show(show_id, "", "", "", "", "", "", "", "", "", "", "")
        Shows.delete(s)
    @staticmethod
    def create_user(user_name, email, password, birth_date, updated_at):
        u = User(0, user_name, email, password, birth_date, updated_at)
        Users.create(u)
    @staticmethod
    def read_user():
        return Users.read()
    @staticmethod
    def read_ID_user(user_id):
        return Users.read_ID(user_id)
    @staticmethod
    def update_user(user_id):
        u = User(user_id)
        Users.update(u)
    @staticmethod
    def delete_user(user_id):
        u = User(user_id)
        Users.delete(u)
    @staticmethod
    def create_ticket(show_id, ticket_price,updated_at):
        t = Ticket(0, show_id, ticket_price, updated_at)
        Tickets.create(t)
    @staticmethod
    def read_ticket():
        return Tickets.read()
    @staticmethod
    def read_ID_ticket(ticket_id):
        return Tickets.read_ID(ticket_id)
    @staticmethod
    def update_ticket(id, show_id, ticket_price,updated_at):
        t = Ticket(id, show_id, ticket_price, updated_at)
        Tickets.update(t)
    @staticmethod
    def delete_ticket(ticket_id):
        t = Ticket(ticket_id)
        Tickets.delete(t)
    @staticmethod
    def is_admin():
        for c in View.read_user():
            if c._User__email == "admin": return
        View.create_user("admin", "admin", "1234", datetime.now())
    @staticmethod
    def authenticate_user(email, password):
        for c in View.read_user():
            if c._User__email == email and c._User__password == password:
                return {"id" : c.id, "user_name" : c._User__user_name }
        return None
    @staticmethod
    def authenticate_admin(email, password):
        for c in View.read_user():
            if c._User__email == email and c._User__password == password:
                return {"id" : c.id, "user_name" : c._User__user_name }
        return None
    @staticmethod
    def search_shows_by_band(band_name):
        bands = View.read_band()
        filtered_shows = [show for show in bands if band_name.lower() in show._Band__band_name.lower()]
        return filtered_shows
    @staticmethod
    def search_shows_by_city(city_name):
        bands = View.read_city()
        filtered_shows = [show for show in bands if city_name.lower() in show._City__city_name.lower()]
        return filtered_shows