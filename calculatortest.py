''' Tests GDD calculator by passing variant inputs'''
from numpy.testing import assert_allclose
from GDDcalculate import *


def test_in_range():
    ''' Tests if GDDcalculate.py works with temperatures between upper and lower '''
    obs = GDDcalculate([15, 16, 18, 19], [23, 24, 26, 27], 14, 28, 4)
    exp = ([4, 6, 8, 10])
    assert_allclose(obs, exp, err_msg='GDD calculation Error',  rtol=1e-5, atol=0)


def test_out_range():
    ''' Tests if GDDcalculate.py works with temperatures out of upper and lower's range '''
    obs = GDDcalculate([15, 16, 18, 19], [23, 24, 26, 27], 20, 22, 4)
    exp = (1.0, 1.0, 1.0, 1.0)
    assert_allclose(obs, exp, err_msg='GDD calculation Error', rtol=1e-5, atol=0)


def test_overlap():
    ''' Tests if GDDcalculate.py works with mintemp bigger than tbase and maxtemp smaller than tupper '''
    obs = GDDcalculate([15, 16, 18, 19], [23, 24, 26, 27], 14, 22, 4)
    exp = ([4.5, 5, 6, 6.5])
    assert_allclose(obs, exp, err_msg='GDD calculation Error', rtol=1e-5, atol=0)

def test_length():
    ''' Tests if GDDcalculate.py works with mismatching GDD length '''
    obs = GDDcalculate([15, 16, 18, 19], [23, 24, 26, 27], 14, 28, 4)
    exp = ([4, 6, 8, None])
    assert_allclose(obs, exp, err_msg='GDD calculation Error', rtol=1e-5, atol=0)