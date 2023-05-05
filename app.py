from flask import Flask, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import *
from datetime import datetime
import random

####
from config import *
from models import db, User, SupportTicket


def createApp():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)
    db.init_app(app)

    @app.route("/")
    def index():
        page = request.args.get("page", 1, type=int)
        per_page = 10
        tickets = (
            SupportTicket.query.filter(SupportTicket.status == "open")
            .order_by(SupportTicket.created_at.desc())
            .paginate(page=page, per_page=per_page)
        )

        closed_tickets = SupportTicket.query.filter(
            SupportTicket.status == "closed"
        ).count()

        all_tickets = SupportTicket.query.filter(SupportTicket.id).count()

        users = User.query.all()

        # Rendern Sie das Template und übergeben Sie die Variablen an das Template
        return render_template(
            "index.html",
            tickets=tickets,
            users=users,
            pagination=tickets,
            closed_tickets=closed_tickets,
            all_tickets=all_tickets,
        )

    @app.route("/filter", methods=["GET", "POST"])
    def filter():
        # default values for filters
        category = request.args.get("category", "")
        importance = request.args.get("importance", "")
        status = request.args.get("status", "")
        # search_query = request.args.get("search_query", "")

        # query all tickets with filters
        filtered_tickets = SupportTicket.query.filter(
            SupportTicket.category.ilike(f"%{category}%"),
            SupportTicket.importance.ilike(f"%{importance}%"),
            SupportTicket.status.ilike(f"%{status}%"),
        ).all()

        # Count the number of filtered tickets
        num_filtered_tickets = len(filtered_tickets)

        # Apply pagination
        page = request.args.get("page", 1, type=int)
        per_page = 10
        tickets = SupportTicket.query.filter(
            SupportTicket.category.ilike(f"%{category}%"),
            SupportTicket.importance.ilike(f"%{importance}%"),
            SupportTicket.status.ilike(f"%{status}%"),
        ).paginate(page=page, per_page=per_page)

        # Render filtered ticket list
        return render_template(
            "filter.html",
            tickets=tickets,
            num_filtered_tickets=num_filtered_tickets,
            category=category,
            importance=importance,
            status=status,
        )

    @app.route("/close_ticket/<int:ticket_id>", methods=["POST"])
    def close_ticket(ticket_id):
        # close the ticket with the given id
        ticket = SupportTicket.query.get_or_404(ticket_id)
        ticket.status = "closed"
        ticket.closed_by = (
            "Test Benutzer"  # TODO: Update to current_user from Flask-Login
        )
        db.session.commit()

        # check if a filter was applied
        category = request.args.get("category")
        importance = request.args.get("importance")
        status = request.args.get("status")
        search_query = request.args.get("search_query")
        filter_applied = category or importance or status or search_query

        # redirect back to the filtered ticket list or index
        if filter_applied:
            return redirect(
                url_for(
                    "filter",
                    category=category,
                    importance=importance,
                    status=status,
                    search_query=search_query,
                )
            )
        else:
            return redirect(url_for("index"))

    """def create_test_tickets(num_tickets):
        ticket_topics = [
            "Error in Login Page",
            "Database Connection Error",
            "Unable to save settings",
            "Website not loading properly",
            "Missing information in profile",
        ]
        categories = ["Hardware", "Software", "Network", "Other"]
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

        create_test_tickets(150)"""

    return app
