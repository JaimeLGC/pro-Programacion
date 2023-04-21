from __future__ import annotations

weekdays = {
    0: "DOMINGO",
    1: "LUNES",
    2: "MARTES",
    3: "MIÉRCOLES",
    4: "JUEVES",
    5: "VIERNES",
    6: "SÁBADO",
}

MONTHS = {
    1: "ENERO",
    2: "FEBRERO",
    3: "MARZO",
    4: "ABRIL",
    5: "MAYO",
    6: "JUNIO",
    7: "JULIO",
    8: "AGOSTO",
    9: "SEPTIEMBRE",
    10: "OCTUBRE",
    11: "NOVIEMBRE",
    12: "DICIEMBRE",
}
LONG_MONTHS = [1, 3, 5, 7, 8, 10, 12]
SHORT_MONTHS = [4, 6, 9, 11]
FEBRUARY = 2
YEAR_LENGTH = 365


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
        if 0 < day <= self.days_in_month:
            self.day = day
        else:
            self.day = 1

    @staticmethod
    def is_leap_year(year: int) -> bool:
        if year % 400 == 0:
            return True
        return year % 4 == 0 and year % 100 != 0

    @property
    def days_in_month(self) -> int:
        if self.month in LONG_MONTHS:
            return 31
        if self.month in SHORT_MONTHS:
            return 30
        if self.month == 2:
            if self.is_leap_year(self.year):
                return 29
            return 28

    def get_delta_days(self) -> int:
        """Número de días transcurridos desde el 1-1-1900 hasta la fecha"""
        past_days = 0
        # Se cuentan los años
        for y in range(1900, self.year):
            if self.is_leap_year(y) == True:
                past_days += 1
<<<<<<< HEAD
            past_days += 365
        # Se cuentan los meses
=======
            past_days += YEAR_LENGTH
>>>>>>> e32a8733608442f3917ff67883f8bfb9d25c7b72
        for m in range(self.month):
            if m in LONG_MONTHS:
                past_days += 31
            if m in SHORT_MONTHS:
                past_days += 30
            if m == 2:
                if self.is_leap_year(self.year):
                    past_days += 29
                else:
                    past_days += 28
        # Se cuenta el resto de días
        past_days += self.day - 1
        return past_days

    @property
    def weekday(self) -> str:
        """día de la semana de la fecha (0 para domingo, ..., 6 para sábado).
        El 1-1-1900 fue domingo."""
        weekday_index = 1
        delta_counter = 1
        while delta_counter <= self.get_delta_days():
            delta_counter += 1
            if weekday_index == 6:
                weekday_index = 0
            else:
                weekday_index += 1
        return weekday_index

    @property
    def is_weekend(self) -> bool:
        weekend = ["VIERNES", "SÄBADO", "DOMINGO"]
        return weekdays[self.weekday] in weekend

    @property
    def short_date(self) -> str:
        """02/09/2003"""
        day = self.day
        month = self.month
        if self.day <= 9:
            day = f"0{self.day}"
        if self.month <= 9:
            month = f"0{self.month}"
        return f"{day}/{month}/{self.year}"

    def __str__(self):
        """martes 2 de septiembre de 2003"""
        day = weekdays[self.weekday]
        month = MONTHS[self.month]
        return f"{day} {self.day} DE {month} DE {self.year}"

    def __add__(self, days: int) -> Date:
        """Sumar un número de días a la fecha"""
        while days > 0:
            if self.month == 13:
                self.year += 1
                self.month == 1
            if days > YEAR_LENGTH:
                self.year += 1
                days -= YEAR_LENGTH
            if days > self.days_in_month:
                self.month += 1
                days -= self.days_in_month
            if self.day + days < self.days_in_month:
                self.day += days
                days = 0
        return Date(self.day, self.month, self.year)

    @property
    def reset_month(self) -> None:
        self.month -= 1
        if self.month <= 0:
            self.year -= 1
            self.month = 12

    def __sub__(self, other: Date | int) -> int | Date:
        """Dos opciones:
        1) Restar una fecha a otra fecha -> Número de días
        2) Restar un número de días la fecha -> Nueva fecha"""
        if isinstance(other, Date):
            difference = self.get_delta_days() - other.get_delta_days()
            if difference < 0:
                difference = -difference
            return difference
<<<<<<< HEAD
        else:
=======

        if isinstance(other, int):
            while other > 0:
                while other > YEAR_LENGTH:
                    self.year -= 1
                    other -= YEAR_LENGTH
                while YEAR_LENGTH > other > self.days_in_month:
                    self.reset_month
                    other -= self.days_in_month
                if self.day - other <= 0:
                    other -= self.day
                    self.reset_month
                    self.day = self.days_in_month
                self.day -= other
                other = 0

>>>>>>> e32a8733608442f3917ff67883f8bfb9d25c7b72
            return Date(self.day, self.month, self.year)

    def __gt__(self, date: Date) -> bool:
        if self.year > date.year:
            return True
        if self.year < date.year:
            return False
        else:
            if self.month > date.month:
                return True
            if self.month < date.month:
                return False
            else:
                return self.day > date.day

    def __lt__(self, date: Date) -> bool:
        if date.year > self.year:
            return True
        if date.year < self.year:
            return False
        else:
            if date.month > self.month:
                return True
            if date.month < self.month:
                return False
            else:
                return date.day > self.day

    def __eq__(self, other: Date) -> bool:
        if self > other:
            return False
        if self < other:
            return False
        else:
            return True


fecha1 = Date(8, 4, 2023)
fecha2 = Date(2, 4, 2023)
dias = fecha1.get_delta_days
diasemana = fecha1.weekday
isweekend = fecha1.is_weekend
sdate = fecha1.short_date
print(fecha1 - 200)
