
![Logo](https://i.imgur.com/AgGGdHb.png)


###

#### Still WIP:

<details>
<summary>English:</summary>
The project is a support ticket web application that allows users to create, manage and track support requests. The web application is based on Flask and SQLAlchemy and uses Bootstrap 5.3 for the front-end.

Users can create tickets and select from a predefined category and importance. They can also edit their tickets and update the status, such as when the issue has been resolved.

The application has a filtering feature that allows users to search tickets based on various criteria, such as category, importance, status, or search query. The search results are displayed in a paginated list.
</details>

<details>
<summary>German:</summary>
Das Projekt ist eine Support-Ticket-Webanwendung, die es Benutzern ermöglicht, Support-Anfragen zu erstellen, zu verwalten und zu verfolgen. Die Webanwendung basiert auf Flask und SQLAlchemy und nutzt Bootstrap 5.3 für das Frontend.

Die Benutzer können Tickets erstellen und aus einer vorgegebenen Kategorie und Wichtigkeit auswählen. Sie können auch ihre Tickets bearbeiten und den Status aktualisieren, z.B. wenn das Problem gelöst wurde.

Die Anwendung verfügt über eine Filterfunktion, die es den Benutzern ermöglicht, Tickets anhand verschiedener Kriterien zu suchen, wie z.B. Kategorie, Wichtigkeit, Status oder Suchanfrage. Die Suchergebnisse werden in einer paginierten Liste angezeigt.
</details>



## Features

- [X] Creation of tickets with categories, priorities and descriptions
- [X] Filtering and sorting of tickets by category, priority and status
- [X] Dashboard for support staff with overview of open tickets and closed tickets
- [X] Pagination for the display of tickets

#### Soon available:
- [ ] Login functionality for users and support employees
- [ ] Light/dark mode toggle
- [ ] Assignment of tickets to support employees with status tracking
- [ ] Overview of tickets assigned to the support employee
- [ ] Ability for support employees to add comments and updates to tickets
- [ ] Ability for users to edit and close their created tickets
- [ ] Easy configuration of database connection and application settings by using environment variables

## Web UI
#### Tickets overview for support employees:
![Imgur](https://i.imgur.com/KgxH0qG.png)

## Creating Tickets

So far, only at the first start of the script, test tickets are generated to work with. The functionality will be implemented later with the login function and employee overview.

```python
def create_test_tickets(num_tickets):
        ticket_topics = [
            "Error in Login Page",
            "Database Connection Error",
            "Unable to save settings",
            "Website not loading properly",
            "Missing information in profile",
        ]
        categories = ["Hardware", "Software", "Networl", "Other"]
        importances = ["low", "medium", "high"]
        users = User.query.all()

        for i in range(num_tickets):
            ticket = SupportTicket(
                ticket_topic=random.choice(ticket_topics),
                description=f"This is a test ticket number {i+1}.",
                opened_by=random.choice(users).id,
                category=random.choice(categories),
                importance=random.choice(importances),
            )
            db.session.add(ticket)

        db.session.commit()

    @app.before_first_request
    def create_test_data():
        db.create_all()

        # Benutzerkonten
        user1 = User(
            name="Max",
            lastname="Mustermann",
            username="mmustermann",
            email="max.mustermann@example.com",
            password="pass123",
            role="Support",
            office="Berlin",
        )
        user2 = User(
            name="Erika",
            lastname="Musterfrau",
            username="emusterfrau",
            email="erika.musterfrau@example.com",
            password="password123",
            role="Admin",
            office="Hamburg",
        )
        user3 = User(
            name="Hans",
            lastname="Wurst",
            username="hwurst",
            email="hans.wurst@example.com",
            password="1234pass",
            role="User",
            office="Frankfurt",
        )

        # Benutzerkonten der Datenbank hinzufügen
        db.session.add(user1)
        db.session.add(user2)
        db.session.add(user3)

        # Änderungen in die Datenbank übernehmen
        db.session.commit()

        create_test_tickets(150)
```
## Project License

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)

## 3rd Party librarys:

![PyPI - License](https://img.shields.io/pypi/l/Flask?label=Flask)

![PyPI - License](https://img.shields.io/pypi/l/Flask-Login?label=Flask-Login)

![PyPI - License](https://img.shields.io/pypi/l/Flask-SQLAlchemy?label=Flask-SQLAlchemy)

![PyPI - License](https://img.shields.io/pypi/l/SQLAlchemy?label=SQLAlchemy)
