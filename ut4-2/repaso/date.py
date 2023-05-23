from __future__ import annotations

SHORT_MONTHS = {4: "Abril", 6: "Junio", 9: "Septiembre", 11: "Noviembre"}
LONG_MONTHS = {
    1: "Enero",
    3: "Marzo",
    5: "Mayo",
    7: "Julio",
    8: "Agosto",
    10: "Octubre",
    12: "Diciembre",
}
FEBRUARY = (2, "Febrero")
WEEKDAY = {
    1: "Lunes",
    2: "Martes",
    3: "Miércoles",
    4: "Jueves",
    5: "Viernes",
    6: "Sábado",
    0: "Domingo",
}


class Date:
    def __init__(self, day: int, month: int, year: int):
        """Validar día, mes y año. Se comprobará si la fecha es correcta
        (entre el 1-1-1900 y el 31-12-2050); si el día no es correcto, lo pondrá a 1;
        si el mes no es correcto, lo pondrá a 1; y si el año no es correcto, lo pondrá a 1900.
        Ojo con los años bisiestos.
        El 1-1-1900 fue lunes.
        """
        if 1900 <= year <= 2050:
            self.year = year
        else:
            self.year = 1900

        if 1 <= month <= 12:
            self.month = month
        else:
            self.month = 1

        if 1 <= day <= self.days_in_month(month, year):
            self.day = day
        else:
            self.day = 1

    @staticmethod
    def is_leap_year(year: int) -> bool:
        return year % 4 == 0 and year % 100 != 0

    @staticmethod
    def days_in_month(month: int, year: int) -> int:
        if month in SHORT_MONTHS:
            return 30
        if month in LONG_MONTHS:
            return 31
        if month in FEBRUARY and year % 4 == 0 and year % 100 != 0:
            return 29
        return 28

    def get_delta_days(self) -> int:
        """Número de días transcurridos desde el 1-1-1900 hasta la fecha"""
        past_days = 0
        full_years = (self.year) - 1900
        past_days += full_years * 365
        for year in range(1900, self.year + 1, 4):
            if year % 100 != 0:
                past_days += 1
        for month in range(1, self.month):
            past_days += self.days_in_month(month, self.year)
        past_days += self.day - 1
        return past_days

    @property
    def weekday(self) -> int:
        """Día de la semana de la fecha (0 para domingo, ..., 6 para sábado)."""

    @property
    def is_weekend(self) -> bool:
        ...

    @property
    def short_date(self) -> str:
        """02/09/2003"""
        ...

    def __str__(self):
        """MARTES 2 DE SEPTIEMBRE DE 2003"""
        ...

    def __add__(self, days: int) -> Date:
        """Sumar un número de días a la fecha"""
        

    def __sub__(self, other: Date | int) -> int | Date:
        """Dos opciones:
        1) Restar una fecha a otra fecha -> Número de días
        2) Restar un número de días la fecha -> Nueva fecha"""
        ...

    def __lt__(self, other) -> bool:
        ...

    def __gt__(self, other) -> bool:
        ...

    def __eq__(self, other) -> bool:
        ...
