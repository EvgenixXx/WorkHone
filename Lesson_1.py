import sqlite3


# Функция для создания базы данных
def create_database():
    # Используем контекстный менеджер для работы с базой данных
    with sqlite3.connect('conference.db') as conn:
        cursor = conn.cursor()

        # Создание таблицы для участников конференции
        cursor.execute('''  
        CREATE TABLE IF NOT EXISTS Participants (  
            id INTEGER PRIMARY KEY AUTOINCREMENT,  
            full_name TEXT NOT NULL,  
            academic_degree TEXT,  
            scientific_field TEXT,  
            workplace TEXT,  
            department TEXT,  
            position TEXT,  
            country TEXT,  
            city TEXT,  
            address TEXT,  
            work_phone TEXT,  
            email TEXT  
        );  
        ''')

        # Создание таблицы для конференций
        cursor.execute('''  
        CREATE TABLE IF NOT EXISTS Conferences (  
            id INTEGER PRIMARY KEY AUTOINCREMENT,  
            title TEXT NOT NULL,  
            date DATE NOT NULL,  
            location TEXT NOT NULL,  
            organizers TEXT,  
            sponsors TEXT,  
            duration_days INTEGER,  
            participant_count INTEGER,  
            speaker_count INTEGER  
        );  
        ''')

        # Создание таблицы для участия в конференциях
        cursor.execute('''  
        CREATE TABLE IF NOT EXISTS Participation (  
            id INTEGER PRIMARY KEY AUTOINCREMENT,  
            participant_id INTEGER,  
            conference_id INTEGER,  
            role TEXT CHECK(role IN ('Докладчик', 'Участник')),  
            invitation_sent_date DATE,  
            application_received_date DATE,  
            report_topic TEXT,  
            thesis_received BOOLEAN,  
            arrival_date DATE,  
            hotel_needed BOOLEAN,  
            departure_date DATE,  
            FOREIGN KEY (participant_id) REFERENCES Participants(id),  
            FOREIGN KEY (conference_id) REFERENCES Conferences(id)  
        );  
        ''')

        # Создание таблицы для гостиниц
        cursor.execute('''  
        CREATE TABLE IF NOT EXISTS Hotels (  
            id INTEGER PRIMARY KEY AUTOINCREMENT,  
            name TEXT NOT NULL,  
            address TEXT NOT NULL,  
            phone TEXT  
        );  
        ''')

        # Создание таблицы для участников гостиниц
        cursor.execute('''  
        CREATE TABLE IF NOT EXISTS HotelParticipants (  
            id INTEGER PRIMARY KEY AUTOINCREMENT,  
            participant_id INTEGER,  
            hotel_id INTEGER,  
            check_in_date DATE,  
            check_out_date DATE,  
            FOREIGN KEY (participant_id) REFERENCES Participants(id),  
            FOREIGN KEY (hotel_id) REFERENCES Hotels(id)  
        );  
        ''')


# Запуск функции создания базы данных
if __name__ == "__main__":
    create_database()