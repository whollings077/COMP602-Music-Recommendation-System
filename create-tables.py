# create_tables.py
import logging
from sqlalchemy.orm import Session
from app.database import engine, Base, SessionLocal # Import SessionLocal
from app.models import Song # Import your specific models here (e.g., Song)

# Configure basic logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def clear_and_seed_data():
    """
    Drops all tables, recreates them, and populates with sample data.
    """
    logger.info("--- Starting database reset and seeding process ---")

    try:
        # Drop all tables associated with Base.metadata
        logger.info("Dropping existing tables (if they exist)...")
        Base.metadata.drop_all(bind=engine)
        logger.info("Tables dropped successfully.")

        # Create all tables associated with Base.metadata
        logger.info("Creating database tables...")
        Base.metadata.create_all(bind=engine)
        logger.info("Tables created successfully.")

        # Populate with sample data
        logger.info("Populating tables with initial data...")
        # Use SessionLocal to get a session
        with SessionLocal() as db:
            populate_songs(db)
            # Add calls to populate other tables here if needed
            # populate_users(db)
            # populate_ratings(db)
        logger.info("Data population completed.")

    except Exception as e:
        logger.error(f"An error occurred during database reset/seeding: {e}", exc_info=True)
        # Depending on the error, you might want to exit or handle differently

    logger.info("--- Database reset and seeding process finished ---")


def populate_songs(db: Session):
    """
    Populates the 'songs' table with sample data.
    """
    logger.info("Adding sample songs...")
    # Define some sample songs - add more or modify as needed
    sample_songs = [
        Song(title="Bohemian Rhapsody", artist="Queen", genre="Rock"),
        Song(title="Like a Rolling Stone", artist="Bob Dylan", genre="Folk Rock"),
        Song(title="Billie Jean", artist="Michael Jackson", genre="Pop"),
        Song(title="Stairway to Heaven", artist="Led Zeppelin", genre="Rock"),
        Song(title="Smells Like Teen Spirit", artist="Nirvana", genre="Grunge"),
        Song(title="Hotel California", artist="Eagles", genre="Rock"),
        Song(title="What's Going On", artist="Marvin Gaye", genre="Soul"),
        Song(title="Sweet Child o' Mine", artist="Guns N' Roses", genre="Hard Rock"),
        Song(title="Imagine", artist="John Lennon", genre="Pop"),
        Song(title="One", artist="U2", genre="Rock"),
        # Add more diverse genres/artists if desired
        Song(title="So What", artist="Miles Davis", genre="Jazz"),
        Song(title="Respect", artist="Aretha Franklin", genre="Soul"),
        Song(title="Good Vibrations", artist="The Beach Boys", genre="Pop Rock"),
        Song(title="Johnny B. Goode", artist="Chuck Berry", genre="Rock and Roll"),
        Song(title="No Woman, No Cry", artist="Bob Marley & The Wailers", genre="Reggae")
    ]

    try:
        # Add the sample songs to the session
        db.add_all(sample_songs)
        # Commit the transaction
        db.commit()
        logger.info(f"Successfully added {len(sample_songs)} sample songs.")
        # Optional: Query back to verify (good for debugging)
        # added_count = db.query(Song).count()
        # logger.info(f"Verification: Found {added_count} songs in the database.")
    except Exception as e:
        logger.error(f"Error populating songs: {e}", exc_info=True)
        db.rollback() # Rollback transaction on error


# Add similar functions for other models if you have them (e.g., User, Rating)
# def populate_users(db: Session):
#     logger.info("Adding sample users...")
#     # ... create User instances and add them ...
#     db.commit()

if __name__ == "__main__":
    # This block ensures the function runs only when the script is executed directly
    clear_and_seed_data()