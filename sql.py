import sqlite3

connection = sqlite3.connect('student.db')
cursor = connection.cursor()

# Create the table
table = '''
CREATE TABLE STUDENT (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(255),
    class VARCHAR(50),
    roll INTEGER,
    marks REAL,
    address VARCHAR(255)
);
'''
cursor.execute(table)

# Insert records
records = [
    ('John Doe', '12A', 1001, 85.5, '123 Main St'),
    ('Alice Smith', '11B', 1002, 92.3, '456 Elm St'),
    ('Bob Johnson', '10C', 1003, 78.9, '789 Oak St'),
    ('Emily Brown', '9A', 1004, 88.2, '321 Pine St'),
    ('Michael Lee', '8B', 1005, 95.7, '654 Maple St'),
    ('Emma Wilson', '7C', 1006, 79.4, '987 Cedar St'),
    ('William Taylor', '6A', 1007, 84.6, '159 Walnut St'),
    ('Sophia Garcia', '5B', 1008, 91.1, '357 Birch St'),
    ('James Martinez', '4C', 1009, 87.8, '753 Spruce St'),
    ('Olivia Rodriguez', '3A', 1010, 76.3, '852 Fir St'),
    ('Daniel Hernandez', '2B', 1011, 94.5, '426 Sycamore St'),
    ('Ava Lopez', '1C', 1012, 82.9, '963 Cedar St'),
    ('Benjamin Gonzalez', '12A', 1013, 89.4, '147 Oak St'),
    ('Mia Perez', '11B', 1014, 83.7, '258 Maple St'),
    ('Ethan Adams', '10C', 1015, 90.8, '369 Pine St'),
    ('Isabella Campbell', '9A', 1016, 77.6, '753 Walnut St'),
    ('Alexander Wright', '8B', 1017, 92.0, '159 Elm St'),
    ('Charlotte Hill', '7C', 1018, 88.5, '357 Cedar St'),
    ('David Mitchell', '6A', 1019, 81.2, '987 Birch St'),
    ('Sofia Roberts', '5B', 1020, 95.3, '426 Spruce St')
]

cursor.executemany('INSERT INTO STUDENT (name, class, roll, marks, address) VALUES (?, ?, ?, ?, ?)', records)

print("The inserted records are : ")

# Retrieve and print the inserted records
data = cursor.execute('''SELECT * FROM STUDENT''')
for row in data:
    print(row)

# Commit changes and close connection
connection.commit()
connection.close()
