from models import db
from sqlalchemy.orm import Mapped, mapped_column

class Usuario(db.Model):
  id_usuario: Mapped[int] = mapped_column(primary_key=True, nullable=False)
  nome: Mapped[str] = mapped_column(nullable=False)
  email: Mapped[str] = mapped_column(unique=True, nullable=False)
  senha: Mapped[str] = mapped_column(nullable=False)
  assinante: Mapped[bool] = mapped_column(nullable=False)