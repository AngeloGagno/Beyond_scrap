from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

class Config:
    '''Configuração inicial do Banco de Dados - Criação de Engine(através da URL do Banco).
            Métodos:
                engine_creator: Instância que retorna a Engine do banco criada
                get_db: Cria uma sessão no banco de dados para realização do processo de CRUD
    '''
    def __init__(self):
        _ = load_dotenv(override=True)
        
        self.engine = create_engine(os.getenv('DB_URL'))

    def _start_session(self):
        return sessionmaker(autocommit=False, autoflush=False, bind=self.engine)

    def engine_creator(self):
        return self.engine
    
    def get_db(self):
        SessionLocal = self._start_session()
        db = SessionLocal() 
        try:
            return db
        finally:
            db.close()