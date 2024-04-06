# Mini project: Erfan Shafagh and Matthew Lee (group 43)
import sqlite3


# Connecting to the database
connection = sqlite3.connect('council.db')
cursor = connection.cursor()
print("Database has been connected successfully!")


# All tables names
tables = ["Researchers", "Competitions", "Applications",
          "Collaborators", "Reviewers", "Conflicts",
          "Assignments", "Committees", "Discussions"]


# Deleting tables if needed
for table in tables:
    cursor.execute("DROP TABLE IF EXISTS " + table + " ;")
print("Tables have been deleted!")


# Creating all needed tables
cursor.execute('''CREATE TABLE IF NOT EXISTS Researchers ( 
               researcher_id INTEGER PRIMARY KEY, 
               first_name VARCHAR(15), 
               last_name VARCHAR(15), 
               email VARCHAR(30), 
               organization VARCHAR(30) 
               ); ''')
cursor.execute('''CREATE TABLE IF NOT EXISTS Competitions ( 
               competition_id INTEGER PRIMARY KEY, 
               title VARCHAR(15), 
               deadline DATE, 
               description VARCHAR(100), 
               area VARCHAR(50), 
               status VARCHAR(10), 
               CHECK ( status IN ('Open','Closed') )
               ); ''')
cursor.execute('''CREATE TABLE IF NOT EXISTS Applications ( 
               application_id INTEGER PRIMARY KEY, 
               competition_id INTEGER REFERENCES Competitions(competition_id), 
               principal_investigator INTEGER REFERENCES Researchers(researcher_id), 
               requested_amount INTEGER, 
               status VARCHAR(10), 
               awarded_amount INTEGER, 
               awarded_date DATE, 
               CHECK ( status IN ('submitted','awarded', 'not awarded') )
               ); ''')
cursor.execute('''CREATE TABLE IF NOT EXISTS Collaborators ( 
               application_id INTEGER REFERENCES Applications(application_id), 
               researcher_id INTEGER REFERENCES Researchers(researcher_id), 
               PRIMARY KEY(application_id, researcher_id) 
               ); ''')
cursor.execute('''CREATE TABLE IF NOT EXISTS Reviewers ( 
               reviewer_id INTEGER PRIMARY KEY, 
               researcher_id INTEGER REFERENCES Researchers(researcher_id) 
               ); ''')
cursor.execute('''CREATE TABLE IF NOT EXISTS Conflicts ( 
               reviewer_id INTEGER REFERENCES Reviewers(reviewer_id), 
               researcher_id INTEGER REFERENCES Researchers(researcher_id), 
               PRIMARY KEY(reviewer_id, researcher_id) 
               ); ''')
cursor.execute('''CREATE TABLE IF NOT EXISTS Assignments ( 
               reviewer_id INTEGER REFERENCES Reviewers(reviewer_id), 
               competition_id INTEGER REFERENCES Competitions(competition_id), 
               deadline DATE, 
               status VARCHAR(10), 
               PRIMARY KEY(reviewer_id, competition_id), 
               CHECK ( status IN ('submitted', 'not submitted') )
               ); ''')
cursor.execute('''CREATE TABLE IF NOT EXISTS Committees ( 
               committee_id INTEGER PRIMARY KEY, 
               meeting_date DATE
               ); ''')
cursor.execute('''CREATE TABLE IF NOT EXISTS Discussions ( 
               committee_id INTEGER REFERENCES Committees(committee_id), 
               competition_id INTEGER REFERENCES Competitions(competition_id), 
               PRIMARY KEY(committee_id, competition_id) 
               ); ''')
print("Tables have been created!")


# Initial data tuples
Researchers = [
    (1, 'John', 'Doe', 'johndoe@example.com', 'University A'),
    (2, 'Jane', 'Smith', 'janesmith@example.com', 'University B'),
    (3, 'Michael', 'Johnson', 'michaeljohnson@example.com', 'University C'),
    (4, 'Emily', 'Brown', 'emilybrown@example.com', 'University D'),
    (5, 'David', 'Lee', 'davidlee@example.com', 'University E'),
    (6, 'Sarah', 'Wilson', 'sarahwilson@example.com', 'University F'),
    (7, 'Daniel', 'Martinez', 'danielmartinez@example.com', 'University G'),
    (8, 'Jennifer', 'Garcia', 'jennifergarcia@example.com', 'University H'),
    (9, 'Christopher', 'Lopez', 'christopherlopez@example.com', 'University I'),
    (10, 'Mary', 'Young', 'maryyoung@example.com', 'University J'),
    (11, 'Matthew', 'Harris', 'matthewharris@example.com', 'University K'),
    (12, 'Laura', 'Clark', 'lauraclark@example.com', 'University L'),
    (13, 'Kevin', 'Lewis', 'kevinlewis@example.com', 'University M'),
    (14, 'Amanda', 'Walker', 'amandawalker@example.com', 'University N'),
    (15, 'Jason', 'Wright', 'jasonwright@example.com', 'University O'),
    (16, 'Michelle', 'Roberts', 'michelleroberts@example.com', 'University P'),
    (17, 'Brian', 'Taylor', 'briantaylor@example.com', 'University Q'),
    (18, 'Stephanie', 'Allen', 'stephanieallen@example.com', 'University R'),
    (19, 'Eric', 'Young', 'ericyoung@example.com', 'University S'),
    (20, 'Rachel', 'Scott', 'rachelscott@example.com', 'University T')
]

Competitions = [
    (1, 'Research Grant 1', '2024-05-15', 'Funding for research projects', 'Science', 'Open'),
    (2, 'Scholarship Program', '2024-06-30', 'Scholarships for students', 'Education', 'Closed'),
    (3, 'Innovation Challenge', '2024-04-20', 'Encouraging innovative ideas', 'Technology', 'Open'),
    (4, 'Arts Festival Funding', '2024-07-10', 'Supporting art events', 'Arts', 'Open'),
    (5, 'Community Development Grant', '2024-08-15', 'Support for community projects', 'Social Sciences', 'Open'),
    (6, 'Medical Research Fund', '2024-06-01', 'Funding medical research studies', 'Medicine', 'Closed'),
    (7, 'Environmental Sustainability', '2024-09-30', 'Recognizing environmental initiatives', 'Environment', 'Open'),
    (8, 'Startup Competition', '2024-05-30', 'Competition for startup ideas', 'Business', 'Open'),
    (9, 'Humanitarian Aid Grant', '2024-07-20', 'Providing aid to humanitarian projects', 'Social Sciences', 'Open'),
    (10, 'Data Science Challenge', '2024-08-10', 'Challenges in data science', 'Technology', 'Open'),
    (11, 'Literary Awards', '2024-09-15', 'Awards for literary works', 'Arts', 'Open'),
    (12, 'Public Health Initiative', '2024-06-15', 'Initiatives to improve public health', 'Medicine', 'Closed'),
    (13, 'Education Innovation Grant', '2024-07-25', 'Funding innovative education projects', 'Education', 'Open'),
    (14, 'Space Exploration Fund', '2024-08-20', 'Supporting space exploration endeavors', 'Science', 'Open'),
    (15, 'Cultural Exchange Program', '2024-09-01', 'Promoting cultural exchange', 'Arts', 'Open'),
    (16, 'Renewable Energy Research Grant', '2024-05-20', 'Funding renewable energy research', 'Environment', 'Open'),
    (17, 'Entrepreneurship Summit', '2024-07-05', 'Summit for entrepreneurs', 'Business', 'Closed'),
    (18, 'Artificial Intelligence Challenge', '2024-08-30', 'Challenges in AI development', 'Technology', 'Open'),
    (19, 'Gender Equality Initiative', '2024-09-10', 'Promoting gender equality', 'Social Sciences', 'Open'),
    (20, 'Public Policy Research Grant', '2024-06-20', 'Funding research in public policy', 'Politics', 'Open')
]

Applications = [
    (1, 1, 3, 5000, 'submitted', 'NULL', 'NULL'), (2, 2, 5, 10000, 'awarded', 8000, '2024-04-05'),
    (3, 3, 8, 7500, 'submitted', 'NULL', 'NULL'), (4, 4, 11, 3000, 'not awarded', 'NULL', 'NULL'),
    (5, 5, 15, 6000, 'submitted', 'NULL', 'NULL'), (6, 6, 18, 9000, 'awarded', 8500, '2024-03-28'),
    (7, 7, 2, 24000, 'submitted', 'NULL', 'NULL'), (8, 8, 7, 7000, 'awarded', 6000, '2024-04-10'),
    (9, 9, 12, 5500, 'submitted', 'NULL', 'NULL'), (10, 10, 20, 28000, 'awarded', 7500, '2024-03-30'),
    (11, 11, 4, 2000, 'not awarded', 'NULL', 'NULL'), (12, 12, 10, 9500, 'awarded', 9000, '2024-04-02'),
    (13, 13, 14, 24500, 'submitted', 'NULL', 'NULL'), (14, 14, 19, 37000, 'awarded', 6500, '2024-03-29'),
    (15, 15, 1, 3500, 'submitted', 'NULL', 'NULL'), (16, 16, 6, 28000, 'awarded', 7500, '2024-04-01'),
    (17, 17, 9, 3000, 'not awarded', 'NULL', 'NULL'), (18, 18, 13, 6000, 'submitted', 'NULL', 'NULL'),
    (19, 19, 16, 27500, 'awarded', 17000, '2024-04-03'), (20, 20, 17, 4000, 'submitted', 'NULL', 'NULL')
]

Collaborators = [
    (2, 1), (2, 3), (6, 7), (6, 8), (8, 5), (10, 3), (10, 6), (12, 14), (13, 2), (13, 19), (13, 10), (14, 7),
    (16, 10), (16, 11), (16, 12), (19, 1), (19, 3), (19, 4), (19, 5), (19, 6), (19, 9), (19, 10), (19, 11), (19, 12)
]

Reviewers = [
    (1, 2), (2, 4), (3, 6), (4, 8), (5, 10), (6, 12), (7, 14), (8, 16), (9, 18), (10, 20), (11, 1), (12, 3),
    (13, 5), (14, 7), (15, 9), (16, 11), (17, 13), (18, 15), (19, 17), (20, 19)
]

Conflicts = [
    (1, 3), (2, 5), (3, 7), (4, 9), (5, 11), (6, 13), (7, 15), (8, 17), (9, 19), (10, 1), (11, 2), (12, 4),
    (13, 6), (14, 8), (15, 10), (16, 12), (17, 14), (18, 16), (19, 18), (20, 20)
]

Assignments = [
    (1, 1, '2024-05-10', 'submitted'), (2, 1, '2024-05-10', 'not submitted'),
    (3, 1, '2024-05-10', 'not submitted'), (4, 2, '2024-06-25', 'not submitted'),
    (5, 2, '2024-06-25', 'submitted'), (6, 2, '2024-06-25', 'not submitted'),
    (7, 3, '2024-04-15', 'submitted'), (8, 3, '2024-04-15', 'not submitted'),
    (9, 3, '2024-04-15', 'not submitted'), (10, 4, '2024-07-05', 'submitted'),
    (11, 4, '2024-07-05', 'not submitted'), (12, 4, '2024-07-05', 'not submitted'),
    (13, 5, '2024-08-10', 'not submitted'), (14, 5, '2024-08-10', 'submitted'),
    (15, 5, '2024-08-10', 'not submitted'), (16, 6, '2024-05-28', 'submitted'),
    (17, 6, '2024-05-28', 'not submitted'), (18, 6, '2024-05-28', 'not submitted'),
    (19, 7, '2024-09-25', 'submitted'), (20, 7, '2024-09-25', 'not submitted'),
    (1, 8, '2024-05-25', 'not submitted'), (2, 8, '2024-05-25', 'submitted'),
    (3, 8, '2024-05-25', 'not submitted'), (4, 9, '2024-07-15', 'not submitted'),
    (5, 9, '2024-07-15', 'submitted'), (6, 9, '2024-07-15', 'not submitted'),
    (7, 10, '2024-08-05', 'submitted'), (8, 10, '2024-08-05', 'not submitted'),
    (9, 10, '2024-08-05', 'not submitted'), (10, 11, '2024-09-10', 'not submitted'),
    (11, 11, '2024-09-10', 'submitted'), (12, 11, '2024-09-10', 'not submitted'),
    (13, 12, '2024-06-10', 'submitted'), (14, 12, '2024-06-10', 'not submitted'),
    (15, 12, '2024-06-10', 'not submitted'), (16, 13, '2024-07-20', 'not submitted'),
    (17, 13, '2024-07-20', 'submitted'), (18, 13, '2024-07-20', 'not submitted'),
    (19, 14, '2024-08-15', 'submitted'), (20, 14, '2024-08-15', 'not submitted'),
    (1, 15, '2024-08-28', 'submitted'), (2, 15, '2024-08-28', 'not submitted'),
    (3, 15, '2024-08-28', 'not submitted'), (4, 16, '2024-05-15', 'submitted'),
    (5, 16, '2024-05-15', 'not submitted'), (6, 16, '2024-05-15', 'not submitted'),
    (7, 17, '2024-07-01', 'submitted'), (8, 17, '2024-07-01', 'not submitted'),
    (9, 17, '2024-07-01', 'not submitted'), (10, 18, '2024-08-25', 'submitted'),
    (11, 18, '2024-08-25', 'not submitted'), (12, 18, '2024-08-25', 'not submitted'),
    (13, 19, '2024-09-05', 'not submitted'), (14, 19, '2024-09-05', 'submitted')
]

Committees = [
    (1, '2024-05-01'), (2, '2024-06-10'), (3, '2024-07-20'), (4, '2024-08-05'), (5, '2024-09-15')
]

Discussions = [
    (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)
]


# Inserting into tables
try:
    cursor.executemany('''INSERT INTO Researchers (researcher_id, first_name, last_name, email, organization)  
                       VALUES (?, ?, ?, ?, ?)''', Researchers)
    cursor.executemany('''INSERT INTO Competitions (competition_id, title, deadline, description, area, status) 
                       VALUES (?, ?, ?, ?, ?, ?)''', Competitions)
    cursor.executemany('''INSERT INTO Applications (application_id, competition_id, principal_investigator, 
                       requested_amount, status, awarded_amount, awarded_date) 
                       VALUES (?, ?, ?, ?, ?, ?, ?)''', Applications)
    cursor.executemany('''INSERT INTO Collaborators (application_id, researcher_id) 
                       VALUES (?, ?)''', Collaborators)
    cursor.executemany('''INSERT INTO Reviewers (reviewer_id, researcher_id) 
                       VALUES (?, ?)''', Reviewers)
    cursor.executemany('''INSERT INTO Conflicts (reviewer_id, researcher_id) 
                       VALUES (?, ?)''', Conflicts)
    cursor.executemany('''INSERT INTO Assignments (reviewer_id, competition_id, deadline, status) 
                       VALUES (?, ?, ?, ?)''', Assignments)
    cursor.executemany('''INSERT INTO Committees (committee_id, meeting_date) 
                       VALUES (?, ?)''', Committees)
    cursor.executemany('''INSERT INTO Discussions (committee_id, competition_id) 
                       VALUES (?, ?)''', Discussions)
except sqlite3.IntegrityError:
    print("ERROR: There was a problem in inserting into the database!\n")
print("Initial data have been inserted into tables!\n")


# Printing all data in all tables
for table in tables:
    cursor.execute("SELECT * FROM " + table + " ;")
    print(f'-------------{table}-------------')
    rows = cursor.fetchall()
    if rows:
        for row in rows:
            print(row)
        print("\n")
    else:
        print("Table is empty!\n")


# task 1
print("Task 1: Find all competitions (calls for grant proposals) open at a user-specified month, which already have\n"
      "at least one submitted large proposal. For a proposal to be large, it has to request more than $20,000 or to\n"
      "have more than 10 participants, including the principal investigator. Return both IDs and the titles.")
while True:
    month = input("Enter a month for task 1 (e.g. 09 or 07): ")
    cursor.execute('''SELECT DISTINCT Competitions.competition_id, Competitions.title 
                   FROM Competitions 
                        JOIN Applications ON Competitions.competition_id = Applications.competition_id 
                   WHERE Competitions.status = 'Open' 
                         AND strftime('%m', Competitions.deadline) = ? 
                         AND (Applications.requested_amount > 20000 
                              OR (SELECT COUNT(*) 
                                  FROM Collaborators 
                                  WHERE Applications.application_id = Collaborators.application_id) > 10) 
                         AND Applications.status = 'submitted'; ''', (month,))
    rows = cursor.fetchall()
    if rows:
        for row in rows:
            print(row)
    else:
        print("Unfortunately, we do not have any matched items in the table!")
    again = input("Do you want to try this task again! (y or n): ")
    if not again == "y":
        print("\n")
        break


# task 2
print("Task 2: For a user-specified area,  find the proposal(s) that request(s) the largest amount of money.")
while True:
    area = input("Enter an area for task 2 (e.g. Science or Arts): ")
    cursor.execute('''SELECT Competitions.competition_id, Competitions.title, Applications.requested_amount 
                   FROM Competitions 
                        JOIN Applications ON Competitions.competition_id = Applications.competition_id 
                   WHERE Competitions.area = ? 
                         AND Applications.requested_amount = (SELECT MAX(Applications.requested_amount) 
                                                              FROM Competitions 
                                                                   JOIN Applications ON Competitions.competition_id = 
                                                                                          Applications.competition_id 
                                                              WHERE Competitions.area = ? ); ''', (area, area))
    rows = cursor.fetchall()
    if rows:
        for row in rows:
            print(row)
    else:
        print("Unfortunately, we do not have any matched items in the table!")
    again = input("Do you want to try this task again! (y or n): ")
    if not again == "y":
        print("\n")
        break


# task 3
print("Task 3: For a user-specified date, find the proposals submitted before that date that are awarded the\n"
      "largest amount of money.")
while True:
    date = input("Enter a date for task 3 (e.g. 2024-03-30): ")
    cursor.execute('''SELECT Competitions.competition_id, Competitions.title, Applications.requested_amount 
                   FROM Competitions 
                        JOIN Applications ON Competitions.competition_id = Applications.competition_id 
                   WHERE Applications.status = 'awarded' 
                         AND Applications.awarded_date < ? 
                   ORDER BY Applications.awarded_amount DESC 
                   LIMIT 1 ;''', (date,))
    rows = cursor.fetchall()
    if rows:
        for row in rows:
            print(row)
    else:
        print("Unfortunately, we do not have any matched items in the table!")
    again = input("Do you want to try this task again! (y or n): ")
    if not again == "y":
        print("\n")
        break


# task 4
print("Task 4: For an area specified by the user, output its average requested/awarded discrepancy, that is, the \n"
      "absolute value of the difference between the amounts.")
while True:
    area = input("Enter an area for task 4 (e.g. Science or Education): ")
    cursor.execute('''SELECT AVG(ABS(Applications.requested_amount - Applications.awarded_amount)) 
                   AS average_discrepancy 
                   FROM Applications 
                        JOIN Competitions ON Applications.competition_id = Competitions.competition_id 
                   WHERE Competitions.area = ? 
                         AND Applications.status = 'awarded'; ''', (area,))
    rows = cursor.fetchall()
    if rows:
        for row in rows:
            if row[0] is None:
                print("Unfortunately, we do not have records to compute this!")
            else:
                print(row[0])
    else:
        print("Unfortunately, we do not have any matched items in the table!")
    again = input("Do you want to try this task again! (y or n): ")
    if not again == "y":
        print("\n")
        break


# task 5
print("Task 5: Reviewer assignment: Provide the user with the option of assigning a set of reviewers to review a \n"
      "specific grant application (research proposal), one proposal at a time. The proposal ID should be specified by\n"
      "the user. Before doing the reviewers assignment, the user should be able to request and receive a list of \n"
      "reviewers who are not in conflict with the proposal being reviewed, and who still have not reached the maximum\n"
      "of three proposals to review.")
while True:
    proposalID = input("Enter a proposal ID for task 5 (e.g. 19 or 20): ")
    cursor.execute('''SELECT Reviewers.reviewer_id, Researchers.first_name, Researchers.last_name 
                   FROM Reviewers 
                        JOIN Researchers ON Reviewers.researcher_id = Researchers.researcher_id 
                   WHERE Reviewers.reviewer_id NOT IN (SELECT Conflicts.reviewer_id 
                                                       FROM Conflicts 
                                                            JOIN Collaborators ON Collaborators.researcher_id = 
                                                                                  Conflicts.researcher_id 
                                                            JOIN Applications ON Collaborators.application_id = 
                                                                                 Applications.application_id 
                                                       WHERE Applications.competition_id = ? ) 
                         AND Reviewers.reviewer_id NOT IN (SELECT reviewer_id 
                                                           FROM Assignments 
                                                           GROUP BY reviewer_id 
                                                           HAVING COUNT(*) >= 3 ) ;''', (proposalID,))
    rows = cursor.fetchall()
    if rows:
        for row in rows:
            print(row)
    else:
        print("Unfortunately, there is not free or none conflict reviewer right now!")
    reviewerID = input("Enter a reviewer ID for task 5 (e.g. 19 or 20): ")
    deadline = input("Enter a deadline for task 5 (e.g. 2024-04-01): ")
    print("Status will be 'not submitted' by default")
    status = "not submitted"
    try:
        cursor.execute('''INSERT INTO Assignments (reviewer_id, competition_id, deadline, status) 
                       VALUES (?, (SELECT competition_id 
                                   FROM Applications 
                                   WHERE application_id = ? ) 
                               , ?, ?) ; ''', (reviewerID, proposalID, deadline, status))
    except sqlite3.IntegrityError:
        print("ERROR: There was a problem in inserting into the database!\n")
    print("New assignment has been inserted into the table!")
    again = input("Do you want to try this task again! (y or n): ")
    if not again == "y":
        print("\n")
        break


# task 6
print("Task 6: For a user-specified name,  find the proposal(s) he/she needs to review.")
while True:
    fullname = input("Enter a full name for task 6 (e.g. Jane Smith or Michael Johnson): ")
    try:
        cursor.execute('''SELECT Researchers.researcher_id, Researchers.first_name, Researchers.last_name, 
                            Competitions.competition_id, Competitions.title 
                       FROM Assignments 
                            JOIN Competitions ON Assignments.competition_id = Competitions.competition_id 
                            JOIN Reviewers ON Assignments.reviewer_id = Reviewers.reviewer_id 
                            JOIN Researchers ON Reviewers.researcher_id = Researchers.researcher_id 
                       WHERE Researchers.first_name = ? 
                             AND Researchers.last_name = ? ;''', (fullname.split(" ")))
    except sqlite3.ProgrammingError:
        print("Make sure you write first and last name separated with a space (e.g. Jane Smith or Michael Johnson)!")
    rows = cursor.fetchall()
    if rows:
        for row in rows:
            print(row)
    else:
        print("Unfortunately, we do not have any matched items in the table!")
    again = input("Do you want to try this task again! (y or n): ")
    if not again == "y":
        print("\n")
        break


# Printing all data in all tables
for table in tables:
    cursor.execute("SELECT * FROM " + table + " ;")
    print(f'-------------{table}-------------')
    rows = cursor.fetchall()
    if rows:
        for row in rows:
            print(row)
        print("\n")
    else:
        print("Table is empty!\n")


print('committing...')
connection.commit()
print('closing the database...')
connection.close()
