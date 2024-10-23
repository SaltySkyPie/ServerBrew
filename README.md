# Server Brew

## Description
A simple proof of concept, that monohlithic applications is the best way for 99% of the cases.

Microservices are just useless complexity for most of the cases. Like for what reason would you want to do something like this, if you can achieve the same thing in 20 minutes of coding and 40 minutes of styling?


Why only have 4 views, 4 templates and 4 urls when you can design an abomination of a project with half of AWS services. (https://github.com/aws-samples/serverless-coffee)

That repository is pure useless complexity, and it's a perfect example of what not to do.



## Installation

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Usage

```bash
python manage.py migrate
python manage.py runserver
```

Then go to http://localhost:8000 and you will see the application.

4 views, 4 templates, 4 urls. That's all you need.


# Live Demo
https://brew.saltyskypie.com/