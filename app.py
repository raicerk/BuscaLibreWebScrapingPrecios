import Database as database

if __name__ == "__main__":
    db = database.database()
    listaidprecios = db.getListalink()
    print(listaidprecios)