# Backend for EPAM React Application ( e-R-FrontEnd-React_Mastering-State )

This project is a basic backend developed in Python with the FastAPI framework. It was created as part of the EPAM course to be used as a backend in a React application that makes AJAX requests.

## Table of Contents

- [Installation](#installation)
- [Requirements](#requirements)
- [Usage](#usage)
- [License](#license)
- [Contact](#contact)
  
## Installation

1. Clone this repository or download the source code of the project.
2. pip install -r requirements.txt

```bash
git clone https://github.com/davidfrodri/e-R-FrontEnd-React_Mastering-State-Backend.git
```

## Requirements

- Python 3.x
- FastAPI
- Uvicorn (or similar ASGI server)

Ensure you have a MongoDB instance running, and update the MongoDB connection details in the db.client module to point to your database.

## Usage

Employee Operations
-------------------

Get All Employees
-----------------

To retrieve a list of all employees, make a GET request to the following endpoint:

GET /community

Get Employee by ID
------------------

To retrieve a specific employee by their ID, make a GET request to the following endpoint:

GET /employee/{id}

Create New Employee
-------------------

To create a new employee, make a POST request to the following endpoint:

POST /employee/

Include the employee details in the request body using the `Employee` schema.

Update Employee
---------------

To update an existing employee, make a PUT request to the following endpoint:

PUT /employee/

Include the updated employee details in the request body using the `Employee` schema. Also, ensure to provide the `id` field to identify the employee to be updated.

Delete Employee
---------------

To delete an employee by their ID, make a DELETE request to the following endpoint:

DELETE /employee/{id}

Subscriber Operations
---------------------

Get All Subscribers
-------------------

To retrieve a list of all subscribers, make a GET request to the following endpoint:

GET /subscribe

Create New Subscriber
---------------------

To create a new subscriber, make a POST request to the following endpoint:

POST /subscribe

Include the subscriber details in the request body using the `Subscriber` schema.

Delete Subscriber
-----------------

To delete a subscriber by their ID, make a DELETE request to the following endpoint:

DELETE /subscribe/{id}

Handling Errors
---------------

- If an employee or subscriber is not found when attempting to retrieve them by ID, you will receive an error response with appropriate error details.

- If a subscriber with the same email already exists when attempting to create a new subscriber, you will receive an error response with a status code of 409 (Conflict).

Example Usage
-------------

Here's an example of how to use the API endpoints:

1. Get all employees:

GET /community

2. Get a specific employee by ID:

GET /employee/{id}

3. Create a new employee:

POST /employee/

Request Body:
```json
{
  "id": "1",  // It's not mandatory an id
  "photo_url": "https://picture.jpg",
  "description": "Aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.",
  "name": "Maryanne Smyth",
  "position": "Buyer",
  "company": "Company Name"
}
```

4. Update an existing employee:

PUT /employee/

Request Body:
```json
{
    "id": "employee_id_here",
    "photo_url": "https://picture.jpg",
    "description": "Aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.",
    "name": "Modified name",
    "position": "Modified position",
    "company": "Company Name"
}
```

5. Delete an employee by ID:

DELETE /employee/{id}

6. Get all subscribers:

GET /subscribe

7. Create a new subscriber:

POST /subscribe

Request Body:
```json
{
    "id": "1",
    "email": "email@email.com"
}
```

8. Delete a subscriber by ID:

DELETE /subscribe/{id}

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

The MIT License is a permissive open-source license that allows you to use, modify, and distribute the code for both commercial and non-commercial purposes. It is one of the most popular licenses in the open-source community.

To view the full text of the MIT License, visit [https://opensource.org/licenses/MIT](https://opensource.org/licenses/MIT).

## Contact

If you have questions or suggestions about the project, contact me at [davidfrodricomputerscience@gmail.com](mailto:davidfrodricomputerscience@gmail.com).
