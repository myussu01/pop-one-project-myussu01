import pytest
import cities


def test_compute_total_distance():
    road_map = [("Kentucky", "Frankfort", 38.197274, -84.86311),\
                ("Delaware", "Dover", 39.161921, -75.526755),\
                ("Minnesota", "Saint Paul", 44.95, -93.094)]

    '''add your tests'''

    assert cities.compute_total_distance(road_map) == pytest.approx(38.5, 0.1)

def test_swap_cities():
    '''add your tests'''
    road_map = [("Kentucky", "Frankfort", 38.197274, -84.86311), \
                 ("Delaware", "Dover", 39.161921, -75.526755), \
                 ("Minnesota", "Saint Paul", 44.95, -93.094)]


    assert cities.swap_cities(road_map, 0, 2) == (road_map, 33334.3)

def test_shift_cities():
    road_map1 = [("Kentucky", "Frankfort", 38.197274, -84.86311), \
                 ("Delaware", "Dover", 39.161921, -75.526755), \
                 ("Minnesota", "Saint Paul", 44.95, -93.094)]
    road_map2 = []

    assert shift_cities(road_map1) == road_map2
    '''add your tests'''


