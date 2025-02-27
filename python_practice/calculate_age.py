import datetime

def get_age(yyyy: int, mm: int, dd: int) -> int:
    dob = datetime.date(yyyy, mm, dd)
    today = datetime.date.today()
    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    return age
