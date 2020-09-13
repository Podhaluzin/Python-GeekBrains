time_in_sec = int(input("Введите время в секундах: "))
hours = time_in_sec // 3600
residue = time_in_sec % 3600
minutes = residue // 60
sec = residue % 60
print(f"Сейчас {hours}:{minutes}:{sec} ")