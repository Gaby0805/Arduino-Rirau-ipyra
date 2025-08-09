from app.repo.users import create_user
from app.core.database import SessionLocal 
from app.core.database import Base, engine



def test_repo_user_create():
    Base.metadata.create_all(bind=engine) # obrigado para criar as tabelas antes de usar o banco de dados
    db = SessionLocal()
    user = create_user(db, "tre", "dois")
    assert user.name == "tre"
    db.close()
