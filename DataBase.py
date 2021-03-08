import os
import psycopg2

import config

class PostgreSQLDataBase:
    # DONE
    def __init__(self):
        """Connecting to database"""
        self.connection = psycopg2.connect(database = config.DB_NAME, user = config.DB_USER,
                            password = config.DB_PASS, host = config.DB_HOST, port = config.DB_PORT)
        self.cursor = self.connection.cursor()
        # self.cursor.execute('CREATE TABLE users (ID BIGSERIAL PRIMARY KEY, user_ID INTEGER );')
        # self.connection.commit()

    # DONE
    def user_exists(self, user_id):
        """Check if there is already a user in the database"""
        with self.connection:
            self.cursor.execute('SELECT * FROM users WHERE user_ID = %s', (user_id,))
            result = self.cursor.fetchall()
            return bool(len(result))

    # DONE
    def add_user(self, user_id):
        """Adding new user"""
        with self.connection:
            self.cursor.execute('CREATE TABLE locations_of_' + str (user_id) + ' (idx INTEGER, name TEXT, last_aqi INTEGER, step INTEGER, notification BOOLEAN);')
            self.connection.commit()
            return self.cursor.execute("INSERT INTO users (user_id) VALUES (%s)", (user_id,))

    def get_all_users(self):
        """Returns all users"""
        with self.connection:
            self.cursor.execute("SELECT * FROM users")
            result = self.cursor.fetchall()
            return result

    # DONE
    def add_location(self, user_id, _idx, _name, _last_aqi, _notification):
        """Adding new location"""
        with self.connection:
            return self.cursor.execute("INSERT INTO locations_of_" + str (user_id) + " VALUES (%s, %s, %s, %s, %s)", (_idx, _name, _last_aqi, 20, _notification))

    # Done
    def name_exists(self, user_id, _name):
        """Check if there is already a location with such name in database"""
        with self.connection:
            self.cursor.execute("SELECT * FROM locations_of_" + str (user_id) + " WHERE name = %s", (_name,))
            result = self.cursor.fetchall()
            return bool(len(result))

    # Done
    def location_exists(self, user_id, _idx):
        """Check if location is already exists"""
        with self.connection:
            self.cursor.execute("SELECT * FROM locations_of_" + str(user_id) + " WHERE idx = %s", (_idx,))
            result = self.cursor.fetchall()
            return bool(len(result))

    # Done
    def get_location_info_idx(self, user_id, _idx):
        """Gets location info by idx"""
        with self.connection:
            self.cursor.execute("SELECT * FROM locations_of_" + str(user_id) + " WHERE idx = %s", (_idx,))
            result = self.cursor.fetchall()
            return result

    # Done
    def get_location_info_name(self, user_id, _name):
        """Gets location by name"""
        with self.connection:
            self.cursor.execute("SELECT * FROM locations_of_" + str (user_id) + " WHERE name = %s", (_name,))
            result = self.cursor.fetchall()
            return result

    # Done
    def get_all_locations(self, user_id):
        """Returns all user locations"""
        with self.connection:
            self.cursor.execute("SELECT * FROM locations_of_" + str (user_id))
            result = self.cursor.fetchall()
            return result

    # Done
    def update_name(self, user_id, _idx, new_name):
        """Update name of location"""
        with self.connection:
            return self.cursor.execute("UPDATE locations_of_" + str (user_id) + " SET name = %s WHERE idx = %s", (new_name, _idx))

    # Done
    def update_last_aqi(self, user_id, _idx, new_aqi):
        """Update last aqi of location"""
        with self.connection:
            return self.cursor.execute("UPDATE locations_of_" + str (user_id) + " SET last_aqi = %s WHERE idx = %s", (new_aqi, _idx))

    # Done
    def update_step(self, user_id, _idx, new_step):
        """Update step of location"""
        with self.connection:
            return self.cursor.execute("UPDATE locations_of_" + str (user_id) + " SET step = %s WHERE idx = %s", (new_step, _idx))

    # Done
    def update_notifications(self, user_id, _idx, status):
        """Update notifications of location"""
        with self.connection:
            return self.cursor.execute("UPDATE locations_of_" + str (user_id) + " SET notification = %s WHERE idx = %s", (status, _idx))

    # Done
    def delete_location(self, user_id, _idx):
        """Deletes location"""
        with self.connection:
            return self.cursor.execute("DELETE FROM locations_of_" + str (user_id) + " WHERE idx = %s", (_idx,))

    # Done
    def close(self):
        """Closing the database connection"""
        self.connection.close()