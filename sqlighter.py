import sqlite3

class SQLighter:

    def __init__(self, database):
        """Connecting to database"""
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()

    def user_exists(self, user_ID):
        """Check if there is already a user in the database"""
        with self.connection:
            result = self.cursor.execute('SELECT * FROM `users` WHERE `user_ID` = ?', (user_ID,)).fetchall()
            return bool(len(result))

    def add_user(self, user_ID):
        """Adding new user"""
        with self.connection:
            self.cursor.execute('CREATE TABLE locations_of_' + str (user_ID) + ' (idx INTEGER, name STRING, last_aqi INTEGER, step INTEGER, notification BOOLEAN);')
            return self.cursor.execute('INSERT INTO `users` (`user_ID`) VALUES(?)', (user_ID,))

    def add_location(self, user_ID, _idx, _name, _last_aqi, _notification):
        """Adding new location"""
        with self.connection:
            return self.cursor.execute('INSERT INTO `locations_of_' + str (user_ID) + '` (`idx`, `name`, `last_aqi`, `step`, `notification`) VALUES(?, ?, ?, ?, ?)', (_idx, _name, _last_aqi, 20, _notification))

    def name_exists(self, user_ID, _name):
        """Check if there is already a user in the database"""
        with self.connection:
            result = self.cursor.execute('SELECT * FROM `locations_of_' + str (user_ID) + '` WHERE `name` = ?', (_name,)).fetchall()
            return bool(len(result))

    def location_exists(self, user_ID, _idx):
        """Check if location is already exists"""
        with self.connection:
            result = self.cursor.execute('SELECT * FROM `locations_of_' + str (user_ID) + '` WHERE `idx` = ?', (_idx,)).fetchall()
            return bool(len(result))

    def get_location_info_idx(self, user_ID, _idx):
        """Gets location by idx"""
        with self.connection:
            result = self.cursor.execute('SELECT * FROM `locations_of_' + str(user_ID) + '` WHERE `idx` = ?', (_idx,)).fetchall()
            return result

    def get_location_info_name(self, user_ID, _name):
        """Gets location by name"""
        with self.connection:
            result = self.cursor.execute('SELECT * FROM `locations_of_' + str(user_ID) + '` WHERE `name` = ?', (_name,)).fetchall()
            return result

    def get_all_locations(self, user_ID):
        """Returns all user locations"""
        with self.connection:
            result = self.cursor.execute('SELECT * FROM `locations_of_' + str(user_ID) + '`').fetchall()
            return result

    def update_name(self, user_ID, _idx, new_name):
        """Update name of location"""
        with self.connection:
            return self.cursor.execute("UPDATE `locations_of_" + str(user_ID) + "` SET `name` = ? WHERE `idx` = ?", (new_name, _idx))

    def update_last_aqi(self, user_ID, _idx, new_aqi):
        """Update last aqi of location"""
        with self.connection:
            return self.cursor.execute("UPDATE `locations_of_" + str(user_ID) + "` SET `last_aqi` = ? WHERE `idx` = ?", (new_aqi, _idx))

    def update_step(self, user_ID, _idx, new_step):
        """Update step of location"""
        with self.connection:
            return self.cursor.execute("UPDATE `locations_of_" + str(user_ID) + "` SET `step` = ? WHERE `idx` = ?", (new_step, _idx))

    def update_notifications(self, user_ID, _idx, status):
        """Update notifications of location"""
        with self.connection:
            return self.cursor.execute("UPDATE `locations_of_" + str(user_ID) + "` SET `notification` = ? WHERE `idx` = ?", (status, _idx))

    def delete_location(self, user_ID, _idx):
        """Deletes location"""
        with self.connection:
            return self.cursor.execute("DELETE FROM `locations_of_" + str(user_ID) + "` WHERE `idx` = ?", (_idx,))

    def close(self):
        """Closing the database connection"""
        self.connection.close()