# TODO Написать 3 класса с документацией и аннотацией типов
import doctest


class Employers:
    def __init__(self, name: str, sallary: float):
        """
        Создание и подготовка к работе объекта "Сотрудники"

        :param name: Имя сотрдника
        :param sallary: Величина заработной платы сотрудника

        Приммер:
        >>> emp_1 = Employers("Андрей Павлов", 50000.0) # Инициализация экземпляра класса
    """
        if not isinstance(name, str):
            raise TypeError("Имя сотрудниква должно быть данным типа str")
        if not isinstance(sallary, float):
            raise TypeError("Зарпалата должна иметь тип float")
        if sallary < 0:
            raise ValueError("ЗП не может быть отрицательной")
        self.name = name
        self.sallary = sallary

    def salary_after_taxes(self, taxes=0.13, min_sallary=12000.0) -> float:
        """
        Метод который вычитает из налогов

        :param taxes: Величина налоговых вычетов

        :raise ValueError: Если величина чистой прибыли сотрудника меньше чем минимально возможная

        :return: Величина чистой прибыли сотрудника

        Пример:
        >>> emp_1 = Employers("Андрей Павлов", 50000.0)
        >>> emp_1.salary_after_taxes()
        """
        ...

    def absenteeism(self, num_abs: int, min_num=4) -> bool:
        """
        Метод который определет является ли сотрудник прогульщиком

        :param num_abs: Количество прогулов в месяц
        :param min_num: Максимально возможное количество проуглов в месяц

        :raise ValueError: Если величина прогулов больше чем дней в месяце

        :return: True or False

        Пример:
        >>> emp_1 = Employers("Андрей Павлов", 50000.0)
        >>> emp_1.salary_after_taxes(3)
        """
        ...


class CocertHall:
    def __init__(self, num_places: int, num_visitors: int):
        """
        Создание и подготовка к работе объекта Концертный зал

        :param num_places: Количество мест в зале
        :param num_visitors: Количество посетителей

        Приммер:
        >>> g = CocertHall(500, 250)# Инициализация экземпляра класса
        """
        if not isinstance(num_places and num_visitors, int):
            raise TypeError("Количество мест и посетителей должно иметь тип int")
        if num_visitors > num_places:
            raise ValueError("Количество посетителей не может быть больше, чем мест")
        self.num_places = num_places
        self.num_visitors = num_visitors

    def __mul__(self, price: int):

        """
        Подсчет прибыли с проданых мест
        :param price: Цена за один билет

        :return Перемножение количества проданых мест с ценой за билет

        Пример:
        >>> g = CocertHall(500, 250)
        >>> g.__mul__(2000)
        """
        ...

    def profitable(self) -> bool:

        """
        Метод для определения прибыльности проведенного мероприятия

        :return Прибыльное ли вышло мероприятие

        Пример:
        >>> g = CocertHall(500, 250)
        >>> g.profitable()

        """
        ...


class Car:

    def __init__(self, consumption: float, tank_volume: float, mileage=0):

        """
        Создание и подготовка к работе объекта "Машина"

        :param consumption: Параметр потребления топлива
        :param tank_volume: Объем бака
        :param mileage: Пробег
        :param engine_on: Включен двигатель или нет
        """
        self.consumption = consumption
        self.tank_volume = tank_volume
        self.reserve = tank_volume
        self.mileage = mileage
        self.engine_on = False

    def start_engine(self):
        """
        Метод, который возвращает True или False в зависмости от того вклбчен двигатель или нет

        :return запущен ли двигатель или двигатель уже запущен

        пример:
        >>> bmw = Car(20.5, 150)
        >>> bmw.start_engine()
        """
        ...

    def drive(self, distance):
        """
        Метод для который возвращает пройденную дистанцию, а также остаток топлива автомобиля

        :param distance: Пройденная автомобилем дистанция

        :return: f"Проехали {distance} км. Остаток топлива: {self.reserve} л."

        >>> bmw = Car(20.5, 150)
        >>> bmw.drive(50)
        """
        ...


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()
