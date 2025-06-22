from datetime import datetime
from config import db, app
import bcrypt
from models import User, Guest, Episode, Appearance

def seed_data():
    print("Starting seed...")
    
    print("Clearing existing data...")
    db.drop_all()
    db.create_all()

    print("Creating test user...")
    test_user = User(
        username="admin",
        _password_hash=bcrypt.hashpw(b"admin123", bcrypt.gensalt()).decode('utf-8')
    )
    db.session.add(test_user)

    print("Creating guests...")
    guests = [
        Guest(name="John Doe", occupation="Comedian"),
        Guest(name="Jane Smith", occupation="Actor"),
        Guest(name="Mike Johnson", occupation="Musician"),
        Guest(name="Sarah Williams", occupation="Writer"),
        Guest(name="David Brown", occupation="Scientist"),
        Guest(name="Lisa Davis", occupation="Chef"),
        Guest(name="Robert Wilson", occupation="Athlete"),
        Guest(name="Emily Taylor", occupation="Journalist")
    ]
    for guest in guests:
        db.session.add(guest)

    print("Creating episodes...")
    episodes = [
        Episode(date=datetime(2023, 1, 15), number="S1E1"),
        Episode(date=datetime(2023, 2, 1), number="S1E2"),
        Episode(date=datetime(2023, 3, 10), number="S1E3"),
        Episode(date=datetime(2023, 4, 5), number="S1E4"),
        Episode(date=datetime(2023, 5, 20), number="S1E5")
    ]
    for episode in episodes:
        db.session.add(episode)

    db.session.commit()

    print("Creating appearances...")
    appearances = [
        Appearance(rating=4, guest_id=1, episode_id=1),
        Appearance(rating=5, guest_id=2, episode_id=1),
        Appearance(rating=3, guest_id=3, episode_id=2),
        Appearance(rating=4, guest_id=4, episode_id=2),
        Appearance(rating=5, guest_id=5, episode_id=3),
        Appearance(rating=2, guest_id=6, episode_id=3),
        Appearance(rating=4, guest_id=7, episode_id=4),
        Appearance(rating=3, guest_id=8, episode_id=4),
        Appearance(rating=5, guest_id=1, episode_id=5),
        Appearance(rating=4, guest_id=3, episode_id=5),
        Appearance(rating=5, guest_id=5, episode_id=5)
    ]
    for appearance in appearances:
        db.session.add(appearance)

    db.session.commit()
    print("Seed complete!")

if __name__ == '__main__':
    with app.app_context():
        seed_data()