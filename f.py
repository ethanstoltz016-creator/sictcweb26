import pandas as pd
import sqlalchemy as sa
from sqlalchemy.orm import declarative_base, sessionmaker, Mapped, mapped_column as Col
from sqlalchemy.orm.decl_api import DeclarativeBase

usernm = "rayden"
passwd = "Pencil1"

engine = sa.create_engine(f"mariadb+mariadbconnector://{usernm}:{passwd}@localhost/ExampleDB")
Base: type[DeclarativeBase] = declarative_base()

class States(Base):
    __tablename__ = 'States'
    id: Mapped[int] = Col('Id', sa.Integer, primary_key=True, index=True)
    #state: Mapped[str] = Col('State', sa.BINARY(16), index=True)
    abbr: Mapped[str] = Col('State', sa.String(2), nullable=True, unique=True)

    def __init__(self, state: str, abbr: str) -> None:
        #self.state = state
        self.abbr = abbr


Base.metadata.create_all(engine)
session = sessionmaker(bind=engine)()


df = pd.read_csv("./states.csv", header=0)
print(df)

df_sorted = df.sort_values(by='Abbreviation')

for row in df_sorted.itertuples(index=True, name='Panda'):
    print(row.State)
    st = States(
        state=row.State,
        abbr=row.Abbreviation
    )
    session.add(st)


session.commit()