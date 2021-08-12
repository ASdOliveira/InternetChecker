import datetime
import random

fiveMinInSecs = (5 * 60)


def updateData(dbInstance, newId):
    dbInstance.execute("Select * FROM last_update")
    data = dbInstance.fetchone()

    Id = data['counter']
    last_random_Id = data['last_id']

    if last_random_Id != newId:
        sql = "DELETE FROM last_update WHERE counter = {}".format(Id)
        dbInstance.execute(sql)

        Id = random.randint(0, 50)
        sql = "INSERT INTO last_update (counter, last_date, last_id) VALUES (%s, %s, %s)"
        val = (Id, getCurrentTimestamp(), newId)
        dbInstance.execute(sql, val)


def isStatusOK(dbInstance):
    dbInstance.execute("Select last_date FROM last_update;")
    lastUpdateTime = dbInstance.fetchone()

    if (getCurrentTimestamp() - lastUpdateTime['last_date']) > fiveMinInSecs:
        return False

    return True


def getCurrentTimestamp():
    current_time = datetime.datetime.now(datetime.timezone.utc)
    unix_timestamp = current_time.timestamp()
    return unix_timestamp
