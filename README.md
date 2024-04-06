# Research Grant Management System (dbDesign)

This project involves creating and managing a database for a council that oversees research grant applications, competitions, and reviewer assignments.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Dependencies](#Dependencies)
- [Contributing](#contributing)

## Introduction

This project implements a database schema and functionalities for managing research grant competitions, applications, reviewers, and related entities. It includes functionalities to perform tasks such as querying competitions, assigning reviewers, and retrieving information about proposals.

## Features

1. Database Creation: The script creates and initializes a SQLite database with the following tables:<br>
    - Researchers: Stores information about researchers who submit applications.
    - Competitions: Stores information about research grant competitions, including their status (open or closed).
    - Applications: Stores information about research grant applications, including their status (submitted, awarded, or not awarded).
    - Collaborators: Stores information about researchers who collaborate on a specific application.
    - Reviewers: Stores information about researchers who serve as reviewers.
    - Conflicts: Stores information about conflicts between reviewers and researchers.
    - Assignments: Stores information about the assignment of reviewers to specific competitions.
    - Committees: Stores information about committee meetings.
    - Discussions: Stores information about which competitions were discussed at specific committee meetings.
2.   Task 1: Find all competitions that are open in a specified month and have at least one large proposal (requesting more than $20,000 or with more than 10 participants) that has been submitted.
3.   Task 2: For a specified area, find the proposal(s) that request the largest amount of money.
4.   Task 3: For a specified date, find the proposals that were submitted before that date and awarded the largest amount of money.
5.   Task 4: For a specified area, calculate the average discrepancy between the requested and awarded amounts for awarded proposals.
6.   Task 5: Assign a reviewer to a specific grant application, ensuring that the reviewer is not in conflict with the application and has not exceeded the maximum of 3 assigned proposals.
7.   Task 6: For a specified researcher's name, find the proposals they need to review.

## Getting Started
To get started with dbDesign, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/erfanshafagh/dbDesign.git
    ```

2. run the program:
    ```bash
    python council.py
    ```

## Usage

Once the program is ready to run, follow these steps to use the database:

1. Run the council.py script to create the database and perform the specified tasks.
2. The script will prompt the user for input when necessary to complete the tasks.
3. The script will print the results of each task to the console.

## Dependencies

- Python 3.x
- SQLite3 (built-in)



## Contributing

- Matthew Lee
- If you find any issues or have suggestions for improvement, feel free to open an [issue](https://github.com/erfanshafagh/dbDesign/issues) or create a [pull request](https://github.com/erfanshafagh/dbDesign/pulls).

