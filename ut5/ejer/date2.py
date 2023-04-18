weekdays = [
    "Lunes",
    "Martes",
    "Miércoles",
    "Jueves",
    "Viernes",
    "Sábado",
    "Domingo",
]

MONTHS = {
    1: "Enero",
    2: "Febrero",
    3: "Marzo",
    4: "Abril",
    5: "Mayo",
    6: "Junio",
    7: "Julio",
    8: "Agosto",
    9: "Septiebre",
    10: "Octubre",
    11: "Noviembre",
    12: "Diciembre",
}
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
        return past_days

    def weekday(self) -> str:
        """día de la semana de la fecha (0 para domingo, ..., 6 para sábado).
        El 1-1-1900 fue domingo."""
        weekday_index = 0
        delta_counter = 1
        while delta_counter <= self.delta_days():
            delta_counter += 1
            weekday = weekdays[weekday_index]
            if weekday_index == 6:
                weekday_index = 0
            else:
                weekday_index += 1
        return f"El {self.day}-{self.month}-{self.year} fue {weekday}"

    def is_weekend(self) -> bool:
        weekend = ["Viernes", "Sábado", "Domingo"]
        if self.weekday().split()[-1] in weekend:
            return True
        else:
            return False

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
        day = self.weekday().split()[-1]
        month = MONTHS[self.month]
        return f"{day} {self.day} de {month} de {self.year}"

    # operador + suma días a la fecha

    # operador - resta días a la fecha o calcula la diferencia entre dos fechas

    # operador == dice si dos fechas son iguales
    def __eq__(self, date: Date):
        return self == date

    # operador > dice si una fecha es mayor que otra
    def __gt__(self, date):
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

    # operador < dice si una fecha es menor que otra
    def __lt__(self, date):
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


fecha1 = Date(2, 4, 2023)
dias = fecha1.delta_days()
diasemana = fecha1.weekday()
isweekend = fecha1.is_weekend()
sdate = fecha1.short_date()
print(str(fecha1))
