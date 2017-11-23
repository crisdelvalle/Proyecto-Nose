# -*- coding:utf-8 -*
import nose
from nose.tools import timed, ok_, eq_, raises

def test_suma():
    ok_(23 + 50 == 80, "Fallo en la suma")

def test_equals():
    eq_(21 + 21, 42)

@raises(TypeError, ValueError)
def test_raises_type_error():
    raise TypeError("Esta prueba pasa")

@raises(Exception)
def test_that_fails_by_passing():
    pass

def testA():
    assert "hola" == "hollas"

def test_that_fails():
    timed(.30)

