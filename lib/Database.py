class Books(Model):
    title = CharField()
    author = CharField()
    location = CharField()

    class Meta:
        database = db