from sqlalchemy import MetaData, Integer, String, TIMESTAMP, ForeignKey, Table, Column, VARCHAR, Float

metadata = MetaData()

article = Table(
    "article",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("article_id", VARCHAR(128)),
    Column("title", VARCHAR(256)),
    Column("url", VARCHAR(128)),
    Column("published_dt", VARCHAR(128)),
    Column("meta_description", VARCHAR(256)),
    Column("currency_curs", Float),
    Column("text", String),
    Column("tags", VARCHAR(256)),
)
