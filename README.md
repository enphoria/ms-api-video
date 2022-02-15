# MS API VIDEO Flask Application

This microservice has the objective of generating a video and sending it by whatsapp through watti.io

---

## Installation

From source:

```bash
git clone https://github.com/kmilo95/prb-api-video prb_api_video
cd prb_api_video
make install
```

From pypi:

```bash
pip install prb_api_video
```

## Executing

This application has a CLI interface that extends the Flask CLI.

Just run:

```bash
$ prb_api_video
```

or

```bash
$ python -m prb_api_video run
```

To see the help message and usage instructions.

## First run

```bash
$ python -m prb_api_video create-db   # Create database sqlite in prb_api_video/database/development.db
$ python -m prb_api_video populate-db  # Populate tables
$ python -m prb_api_video add-user -u admin -p 1234  # ads a user
$ python -m prb_api_video run # Run microservices
```

Go to:

- Host: http://localhost:5000
- Admin: http://localhost:5000/admin/
  - user: admin, pass: 1234
- API GET:
  - http://localhost:5000/api/v1/persons/
- API POST:
  - http://localhost:5000/api/v1/send/message
  Payload:
  ```bash
    {
      "interest": "Seguridad"
    }
  ```


> **Note**: You can also use `flask run` to run the application.
