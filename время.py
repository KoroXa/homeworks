import datetime		#новый модуль, который показывает дату и время

now = datetime.datetime.today()
newyear = datetime.datetime(2023, 1, 1)
d = newyear - now
mm, ss = divmod(d.seconds, 60)
hh, mm = divmod(mm, 60)
#print("До Нового года осталось:",d.days,"дней", hh,"часов", mm,"минут", ss,"секунд")
print("До Нового года осталось: {} дней {} часов  {} минут  {} секунд".format(d.days, hh, mm, ss))




























