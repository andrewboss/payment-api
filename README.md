# Payment System REST API
```text
         _._._                       _._._
        _|   |_                     _|   |_
        | ... |_._._._._._._._._._._| ... |
        | | o Bank of Hong Kong Luna o  | |
        | """ |  """    """    """  | """ |
   ())  |[-|-]| [-|-]  [-|-]  [-|-] |[-|-]|  ())
  (())) |     |---------------------|     | (()))
 (())())| """ |  """    """    """  | """ |(())())
 (()))()|[-|-]|  :::   .-"-.   :::  |[-|-]|(()))()
 ()))(()|     | |~|~|  |_|_|  |~|~| |     |()))(()
    ||  |_____|_|_|_|__|_|_|__|_|_|_|_____|  ||
 ~ ~^^ @@@@@@@@@@@@@@/=======\@@@@@@@@@@@@@@ ^^~ ~
      ^~^~                                ~^~^

* Bank of Hong Kong Luna - Robert A. Heinlein's - The Moon is a Harsh Mistress
```

## Summary

This is a new **Bank of Hong Kong Luna** Payments System REST API which does not exist yet.
Main aim of this project is to implement HTTP REST API to Payments DB.

## Database

### Payments

Database is a super powerful but lightweight SQLLite3 and is provided in file `/db/database.db` 
with schema: `/db/schema.sql`

## REST Endpoints

- ```GET /payment/{id}``` Get specific payment
- ```GET /payments/all``` Get all payments
- ```GET /payments/user/{userId}``` Get all user payments
- ```PUT /payment/{id}``` Record new payment
- ```POST /payment/{id}``` Update existing payment

## Development

### Initial Setup
- Creating virtual environment and activating it:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
- Installing pip packages from requirements file:
    ```bash
   pip install --upgrade -r requirements.txt 
   ```
### Running REST API

- Executing locally:
  ```bash
  FLASK_APP=api/app.py FLASK_ENV=development FLASK_DEBUG=1 flask run --host=0.0.0.0
  ```
   
### Unit Tests

- Running unit tests:
  ```bash
  python -m xmlrunner discover -s tests -o test-reports
  ```
