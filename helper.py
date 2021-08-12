import datetime

lastId = 0
lastUpdateTime = 0
fiveMinInSecs = (5 * 60)


# def updateData(newId):
#     lastId = newId
#     lastUpdateTime = getCurrentTimestamp()


def isStatusOK():
    global lastUpdateTime
    if (getCurrentTimestamp() - lastUpdateTime) > fiveMinInSecs:
        return False
    lastUpdateTime = getCurrentTimestamp()
    return True


def getCurrentTimestamp():
    current_time = datetime.datetime.now(datetime.timezone.utc)
    unix_timestamp = current_time.timestamp()
    return unix_timestamp