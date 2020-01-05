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

    road_map2 = [("London", "England", 51.5074, -0.1278), \
                 ("Rome", "Italy", 41.9028, 12.4964), \
                 ("Amsterdam", "The Netherlands", 52.3667, 4.8945)]

    assert cities.swap_cities(road_map, 0, 2) == ([("Minnesota", "Saint Paul", 44.95, -93.094), \
                 ("Delaware", "Dover", 39.161921, -75.526755), \
                 ("Kentucky", "Frankfort", 38.197274, -84.86311)], pytest.approx(38.5, 0.1))

    assert road_map[0][1] == "Saint Paul"
    assert road_map[-1][2] == pytest.approx(38.2, 0.1)

    assert cities.swap_cities(road_map2, 0, 1)
    assert road_map2[0][0] == "Rome"
    assert road_map2[1][2] == pytest.approx(51.5, 0.1)

def test_shift_cities():
    road_map = [("Kentucky", "Frankfort", 38.197274, -84.86311),
                ("Delaware", "Dover", 39.161921, -75.526755),
                ("Minnesota", "Saint Paul", 44.95, -93.094)]

    road_map2 = [("London", "England", 51.5074, -0.1278), \
                 ("Rome", "Italy", 41.9028, 12.4964), \
                 ("Amsterdam", "The Netherlands", 52.3667, 4.8945)]

    assert cities.shift_cities(road_map) == [("Minnesota", "Saint Paul", 44.95, -93.094),
                                             ("Kentucky", "Frankfort", 38.197274, -84.86311),
                                             ("Delaware", "Dover", 39.161921, -75.526755)]

    assert road_map[0][2] == pytest.approx(44.9, 0.1)
    assert road_map[2][1] == "Dover"
    assert cities.shift_cities(road_map2)
    assert road_map2[0][0] == "Amsterdam"
    assert road_map2[1][1] == "England"


    '''add your tests'''


