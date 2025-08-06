from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models.users import Users
from app.core.database import Base

engine = create_engine("sqlite:///:memory:")
Session = sessionmaker(bind=engine)
Base.metadata.create_all(engine)

def test_create_user():
    session = Session()
    user = Users(name="Gaby", password="minha_senha123")
    session.add(user)
    session.commit()
    session.refresh(user)

    assert user.name == "Gaby"

    session.close()
