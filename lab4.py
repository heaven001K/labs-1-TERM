class Plane: # опис класу
    def __init__(self, volume_of_fuel_tanks, name, number_of_passengers, public_numeric_field, public_string_field):
        self.__volume_of_fuel_tanks = volume_of_fuel_tanks
        self.__name = name
        self.__number_of_passengers = number_of_passengers 
        self.public_numeric_field = public_numeric_field
        self.public_string_field = public_string_field

    def get_volume_of_fuel_tanks(self): #отримання значень відповідних приватних полів об'єкта.
        return self.__volume_of_fuel_tanks

    def get_name(self): #отримання значень відповідних приватних полів об'єкта.
        return self.__name

    def get_number_of_passengers(self): #отримання значень відповідних приватних полів об'єкта.
        return self.__number_of_passengers

    def __str__(self):
        return f"Plane {self.__name} with {self.__number_of_passengers} number of passengers" #metod str

    def __repr__(self):
        return f"Plane({self.__volume_of_fuel_tanks}, '{self.__name}', {self.__number_of_passengers})" #для виведенння рядка

    def __del__(self):
        print(f"Object {self.__name} has been deleted.") #delete the object

# Функція для виведення інформації про літак
def get_info(plane):
    info = []
    info.append(f"Назва: {plane.get_name()}")
    info.append(f"Кількість пасажирів: {plane.get_number_of_passengers()}")
    info.append(f"Об'єм паливних баків: {plane.get_volume_of_fuel_tanks()}")
    info.append(f"Публічне числове поле: {plane.public_numeric_field}")
    info.append (f"Публічне рядкове поле: {plane.public_string_field}")
    return info

# Основний код
def main():
    # Ініціалізація 3 об'єктів класу Plane
    plane1 = Plane(100000, "Qatar Airways.", 200, 123, "Виконався метод1")
    plane2 = Plane(150000, "Singapore Airlines.", 300, 456, "Виконався метод2")
    plane3 = Plane(80000, "Emirates.", 150, 789, "Виконався метод3")
    planes = [plane1,plane2,plane3]

    for i,plane in enumerate(planes, 1):
        print('====')
        print(f'info about {i }-plane-----')
        plane_info = get_info(plane)
        print("\n".join(plane_info))

if __name__ == "__main__":
    main()
print('lab4_done')


