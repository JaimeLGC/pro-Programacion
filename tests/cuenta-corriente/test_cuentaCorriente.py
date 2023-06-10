from __future__ import annotations
from cuentaCorriente import *

dni1 = Dni('43389674D')
dni2 = Dni('44489674V')
cuenta1 = CuentaCorriente('Jose', 'Pérez', 'La Calle', '666733123', '44489674')
cuenta2 = CuentaCorriente('Sara', 'Martín', 'La Plaza', '666883123', '44489674V')

def test_build_dni():
    assert dni1.dni == '43389674D'
    assert dni1.sano == False

def test_set_dni():
    dni2.setDni('111111111D')
    assert dni2.dni == '111111111D'

def test_get_dni():
    assert dni1.getDni() == '43389674D'

def test_set_sano():
    dni1.setSano(True)
    assert dni1.sano == True

def test_check_longitud():
    assert dni1.checkLongitud() == True

def test_check_numero():
    assert dni1.checkNumero() == True

def test_check_letra():
    assert dni1.checkLetra() == True

def test_check_dni():
    dni1.setSano(False)
    dni1.checkDni()
    assert dni1.sano == True

def test_build_cuenta():
    assert cuenta1.nombre == 'Jose'
    assert cuenta1.apellido == 'Pérez'
    assert cuenta1.direccion == 'La Calle'
    assert cuenta1.telefono == '666733123'
    assert cuenta1.saldo == 0.0

def test_set_nombre():
    cuenta1.setNombre('Juan')
    assert cuenta1.nombre == 'Juan'

def test_get_nombre():
    assert cuenta1.getNombre() == 'Juan'

def test_set_apellido():
    cuenta1.setApellido('González')
    assert cuenta1.apellido == 'González'

def test_get_apellido():
    assert cuenta1.getApellido() == 'González'

def test_set_direccion():
    cuenta1.setDireccion('Jardín')
    assert cuenta1.direccion == 'Jardín'

def test_get_direccion():
    assert cuenta1.getDireccion() == 'Jardín'

def test_set_telefono():
    cuenta1.setTelefono('665777897')
    assert cuenta1.telefono == '665777897'

def test_get_telefono():
    assert cuenta1.getTelefono() == '665777897'

def test_set_nif():
    cuenta1.setNif('45594827B')
    assert cuenta1.nif == '45594827B'

def test_get_nif():
    assert cuenta1.getNif() == '45594827B'

def test_set_saldo():
    cuenta1.setSaldo(23.5)
    assert cuenta1.saldo == 23.5

def test_get_saldo():
    assert cuenta1.getSaldo() == 23.5

def test_retirar_dinero():
    cuenta1.retirarDinero(10) == (10, 13.5)
    assert cuenta1.saldo == 13.5

def test_ingresar_dinero():
    cuenta1.ingresarDinero(10) == (10, 23.5)
    assert cuenta1.saldo == 23.5

def test_saldo_negativo():
    assert cuenta1.saldoNegativo() == True


    

