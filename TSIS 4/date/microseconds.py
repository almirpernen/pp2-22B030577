from datetime import datetime

current_datetime = datetime.now()

truncated_datetime = current_datetime.replace(microsecond=0)

print("Текущая дата и время с микросекундами:", current_datetime)
print("Текущая дата и время без микросекунд:", truncated_datetime)