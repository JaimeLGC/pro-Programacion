LONG_MONTHS = {
    "January": 1,
    "March": 3,
    "May": 5,
    "July": 7,
    "August": 8,
    "October": 10,
    "December": 12,
}
SHORT_MONTHS = {"April": 4, "June": 6, "September": 9, "November": 11}
FEBRUARY = 2


class Date:
    def __init__(self, day: int, month: int, year: int):
        """Validar día, mes y año. Se comprobará si la fecha es correcta
        (entre el 1-1-1900 y el 31-12-2050); si el día no es correcto, lo pondrá a 1;
        si el mes no es correcto, lo pondrá a 1; y si el año no es correcto, lo pondrá a 1900.
        Ojo con los años bisiestos.
        """
        self.year = year
        if 1900 <= year <= 2050:
            self.year = year
        else:
            self.year = 1900
        if 1 <= month <= 12:
            self.month = month
        else:
            self.month = 1
        if 0 < day <= self.days_in_month(month, year):
            self.day = day
        else:
            self.day = 1

    def is_leap_year(self, year: int) -> bool:
        if year % 400 == 0:
            return True
        if year % 4 == 0 and year % 100 != 0:
            return True
        else:
            return False

    def days_in_month(self, month, year) -> int:
        if month in LONG_MONTHS.values():
            return 31
        if month in SHORT_MONTHS.values():
            return 30
        if month == 2:
            if self.is_leap_year(year):
                return 29
            return 28

    def delta_days(self) -> int:
        """Número de días transcurridos desde el 1-1-1900 hasta la fecha"""
        past_days = 0
        for y in range(1900, self.year):
            if self.is_leap_year(y) == True:
                past_days += 1
            past_days += 365
        for m in range(self.month):
            if m in LONG_MONTHS.values():
                past_days += 31
            if m in SHORT_MONTHS.values():
                past_days += 30
            if m == 2:
                if self.is_leap_year(self.year):
                    past_days += 29
                else:
                    past_days += 28
        past_days += self.day
        print(
            f"Han pasado {past_days} días desde el 1-1-1900 hasta el {self.day}-{self.month}-{self.year}"
        )
        return past_days

    def weekday(self) -> int:
        """día de la semana de la fecha (0 para domingo, ..., 6 para sábado).
        El 1-1-1900 fue domingo."""
        weekdays = [
            "Lunes",
            "Martes",
            "Miércoles",
            "Jueves",
            "Viernes",
            "Sábado",
            "Domingo",
        ]
        weekday_index = 0
        delta_counter = 1
        while delta_counter <= self.delta_days():
            delta_counter += 1
            weekday = weekdays[weekday_index]
            if weekday_index == 6:
                weekday_index = 0
            else:
                weekday_index += 1
        print(f"El {self.day}-{self.month}-{self.year} fue {weekday}")
        return weekday_index

    def is_weekend(self) -> bool:
        weekend = ["Viernes", "Sábado", "Domingo"]
        if self.weekday().split()[-1] in weekend:
            print(f"El {self.day}-{self.month}-{self.year} fue fin de semana")
            return True
        else:
            return False
            print(f"El {self.day}-{self.month}-{self.year} no fue fin de semana")

    def short_date(self) -> str:
        """02/09/2003"""
        return "1"

    def __str__(self):
        """martes 2 de septiembre de 2003"""
        pass
        return 1

    # operador + suma días a la fecha
    # operador - resta días a la fecha o calcula la diferencia entre dos fechas
    # operador == dice si dos fechas son iguales
    # operador > dice si una fecha es mayor que otra
    # operador < dice si una fecha es menor que otra


fecha1 = Date(22, 4, 2023)
dias = fecha1.delta_days()
diasemana = fecha1.weekday()
isweekend = fecha1.is_weekend()
print(isweekend)
