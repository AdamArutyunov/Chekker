import sqlalchemy
import sqlalchemy.orm as orm
from sqlalchemy import *
from sqlalchemy_serializer import SerializerMixin
from ..db_session import SqlAlchemyBase


class Test(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'tests'

    id = Column(Integer, primary_key=True, autoincrement=True)
    labour_id = Column(Integer, ForeignKey("labours.id"))
    labour = orm.relation("Labour")

    statement = Column(String, nullable=False)

    answer_type = Column(Integer, default=0, nullable=False)
    # 0: Raw input
    # 1: Single answer (radio button)
    # 2: Multiply answers (checkbox)

    answers = orm.relation("Answer", back_populates="test")