import datetime
from datetime import date,timedelta
from dateutil.relativedelta import relativedelta

def calculate_age_withFormat(age):
    today = datetime.datetime.utcnow()
    diff = today - relativedelta(years=age)
    myTime = '%02d:%02d:%02d' % (diff.days*24 + diff.seconds // 3600, (diff.seconds % 3600) // 60, diff.seconds // 60)
    print("Age with format", myTime)