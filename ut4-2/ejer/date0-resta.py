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

        self.year = year
        if 1990 <= year <= 2050:
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

        """Validar día, mes y año. Se comprobará si la fecha es correcta
        (entre el 1-1-1900 y el 31-12-2050); si el día no es correcto, lo pondrá a 1;
        si el mes no es correcto, lo pondrá a 1; y si el año no es correcto, lo pondrá a 1900.
        Ojo con los años bisiestos.
        """

    def is_leap_year(self, year: int) -> bool:
        if year % 400 == 0:
            return True
        if year % 4 == 0 and year % 100 == 0:
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

    def weekday(self) -> int:
        """día de la semana de la fecha (0 para domingo, ..., 6 para sábado).
        El 1-1-1900 fue domingo."""
        pass
        return 1

    def is_weekend(self) -> bool:
        pass
        return True

    def short_date(self) -> str:
        """02/09/2003"""
        pass
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


fecha1 = Date(29, 3, 1899)
print(fecha1.day, fecha1.month, fecha1.year)

# if isinstance(other, int):
#     while other > 0:
#         if other > 365:
#             self.year -= 1
#             other -= 365
#         elif other > self.days_in_month:
#             self.month -= 1
#             if self.month <= 0:
#                 self.year -= 1
#                 self.month = 12
#             other -= self.days_in_month
#         elif other < self.day:
#             self.day -= other
#             other = 0
#         elif self.day < other < self.days_in_month:
#             rest = other - self.day
#             self.month -= 1
