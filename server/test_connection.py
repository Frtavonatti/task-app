from sqlalchemy import text 
from database import engine, Base

def init_db():
    print("Creating tables...")
    Base.metadata.create_all(bind=engine)
    print("Tables created succesfully.")

def test_connection():
    try:
        with engine.connect() as connection:
            print("Succesfully connected to the database.")
            # Usa text para ejecutar la consulta SQL
            result = connection.execute(text("SELECT 1"))
            print("Result of the test:", result.fetchone())
    except Exception as e:
        print("Error connecting to the database", e)

if __name__ == "__main__":
    init_db()
    test_connection()