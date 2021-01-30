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












# import sqlite3
# import os
# import psycopg2
#
# class SQLighter:
#
#     # def __init__(self, database):
#     #     """Connecting to database"""
#     #     self.connection = sqlite3.connect(database)
#     #     self.cursor = self.connection.cursor()
#
#     def __init__(self, DATABASE_URL):
#         """Connecting to database"""
#         self.connection = psycopg2.connect(DATABASE_URL, sslmode='require')
#         self.cursor = self.connection.cursor()
#         # self.cursor.execute('CREATE TABLE users (ID BIGSERIAL PRIMARY KEY, user_ID VARCHAR (255) );')
#
#         # self.cursor.execute('CREATE TABLE users (ID INTEGER SERIAL, user_ID VARCHAR (255) );')
#         # self.cursor.execute('CREATE TABLE users (ID INTEGER SERIAL KEY AUTOINCREMENT, user_ID VARCHAR (255) );')
#
#     def user_exists(self, user_ID):
#         """Check if there is already a user in the database"""
#         with self.connection:
#             # result = self.cursor.execute(f'SELECT user_ID FROM users')
#             # result = self.cursor.execute(f'SELECT * FROM users WHERE user_ID = "{user_ID}"')
#
#             # result = self.cursor.execute(f"SELECT * FROM users WHERE user_ID = '{user_ID}'")
#             # result = self.cursor.execute('SELECT * FROM users WHERE user_ID = "%s"', (user_ID,)).fetchall()
#             print(result.fetchall())
#             if result is None:
#                 print("HERE")
#                 return False
#             else:
#                 print("THERE")
#                 return True
#             # MySQL
#             # result = self.cursor.execute('SELECT * FROM `users` WHERE `user_ID` = ?', (user_ID,)).fetchall()
#             # return bool(len(result))
#
#     def add_user(self, user_ID):
#         """Adding new user"""
#         with self.connection:
#             self.cursor.execute('CREATE TABLE locations_of_' + str ("user_ID") + ' (idx INTEGER, name TEXT, last_aqi INTEGER, step INTEGER, notification BOOLEAN);')
#             return self.cursor.execute('INSERT INTO users (user_ID) VALUES(%s)', (user_ID,))
#
#     def add_location(self, user_ID, _idx, _name, _last_aqi, _notification):
#         """Adding new location"""
#         with self.connection:
#             return self.cursor.execute('INSERT INTO `locations_of_' + str (user_ID) + '` (`idx`, `name`, `last_aqi`, `step`, `notification`) VALUES(?, ?, ?, ?, ?)', (_idx, _name, _last_aqi, 20, _notification))
#
#     def name_exists(self, user_ID, _name):
#         """Check if there is already a user in the database"""
#         with self.connection:
#             result = self.cursor.execute('SELECT * FROM `locations_of_' + str (user_ID) + '` WHERE `name` = ?', (_name,)).fetchall()
#             return bool(len(result))
#
#     def location_exists(self, user_ID, _idx):
#         """Check if location is already exists"""
#         with self.connection:
#             result = self.cursor.execute('SELECT * FROM `locations_of_' + str (user_ID) + '` WHERE `idx` = ?', (_idx,)).fetchall()
#             return bool(len(result))
#
#     def get_location_info_idx(self, user_ID, _idx):
#         """Gets location by idx"""
#         with self.connection:
#             result = self.cursor.execute('SELECT * FROM `locations_of_' + str(user_ID) + '` WHERE `idx` = ?', (_idx,)).fetchall()
#             return result
#
#     def get_location_info_name(self, user_ID, _name):
#         """Gets location by name"""
#         with self.connection:
#             result = self.cursor.execute('SELECT * FROM `locations_of_' + str(user_ID) + '` WHERE `name` = ?', (_name,)).fetchall()
#             return result
#
#     def get_all_locations(self, user_ID):
#         """Returns all user locations"""
#         with self.connection:
#             result = self.cursor.execute('SELECT * FROM `locations_of_' + str(user_ID) + '`').fetchall()
#             return result
#
#     def update_name(self, user_ID, _idx, new_name):
#         """Update name of location"""
#         with self.connection:
#             return self.cursor.execute("UPDATE `locations_of_" + str(user_ID) + "` SET `name` = ? WHERE `idx` = ?", (new_name, _idx))
#
#     def update_last_aqi(self, user_ID, _idx, new_aqi):
#         """Update last aqi of location"""
#         with self.connection:
#             return self.cursor.execute("UPDATE `locations_of_" + str(user_ID) + "` SET `last_aqi` = ? WHERE `idx` = ?", (new_aqi, _idx))
#
#     def update_step(self, user_ID, _idx, new_step):
#         """Update step of location"""
#         with self.connection:
#             return self.cursor.execute("UPDATE `locations_of_" + str(user_ID) + "` SET `step` = ? WHERE `idx` = ?", (new_step, _idx))
#
#     def update_notifications(self, user_ID, _idx, status):
#         """Update notifications of location"""
#         with self.connection:
#             return self.cursor.execute("UPDATE `locations_of_" + str(user_ID) + "` SET `notification` = ? WHERE `idx` = ?", (status, _idx))
#
#     def delete_location(self, user_ID, _idx):
#         """Deletes location"""
#         with self.connection:
#             return self.cursor.execute("DELETE FROM `locations_of_" + str(user_ID) + "` WHERE `idx` = ?", (_idx,))
#
#     def close(self):
#         """Closing the database connection"""
#         self.connection.close()