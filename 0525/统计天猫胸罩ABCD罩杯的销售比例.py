import sqlalchemy
import pandas

engine = sqlalchemy.create_engine("sqlite:///bra.sqlite")


sql = "select * from sales;"
df = pandas.read_sql(sql,engine)
print(df)
