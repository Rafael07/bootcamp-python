from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Cria a engine do banco
engine = create_engine("sqlite:///banco.db", echo=True)

# Declara a base
Base = declarative_base()


# Define o modelo e declara a tabela
class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True)
    nome = Column(String)
    idade = Column(Integer)


# Cria a tabela
Base.metadata.create_all(engine)

# Cria a sessão
Session = sessionmaker(bind=engine)

# Usa gerenciador de contexto com a sessão
with Session() as session:
    novo_usuario = Usuario(nome="João", idade=30)
    session.add(novo_usuario)

    usuarios = session.query(Usuario).all()
    for u in usuarios:
        print(u.id, u.nome, u.idade)
