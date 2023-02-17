from datetime import datetime

current_datetime = datetime.now()

truncated_datetime = current_datetime.replace(microsecond=0)

print(current_datetime)
print(truncated_datetime)