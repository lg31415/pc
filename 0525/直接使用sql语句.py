import pandas
import sqlalchemy


# 创建引擎
sql = sqlalchemy.create_engine("sqlite:///bra_all.sqlite")
pandas.read_sql(sql)