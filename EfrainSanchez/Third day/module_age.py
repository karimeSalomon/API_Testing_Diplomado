from datetime import datetime
def calculate_age_ondays(edad):
    now = datetime.now()
    year = now.year - edad
    fechaNacimiento = datetime(year,1,1,00,00,00,000000)
    dif= now-fechaNacimiento
    return dif
