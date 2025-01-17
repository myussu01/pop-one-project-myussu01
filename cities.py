import math
import random

def read_cities(file_name):
    """
    Read in the cities from the given `file_name`, and return  them as a list of four-tuples:  [(state, city, latitude, longitude), ...]  Use this as your initial `road_map`, that is, the cycle   Alabama -> Alaska -> Arizona -> ... -> Wyoming -> Alabama.
    """
    road_map = []
    inputFileName = file_name
    try:
        infile = open(inputFileName, "r")
        line = infile.readline()
        while line:
            x = line.split("\t")
            for i in range(len(x)-1, (len(x)-3), -1):
                x[i] = float(x[i])
            x = tuple(x)
            road_map.append(x)
            line = infile.readline()
    finally:
        infile.close()
    return road_map

def print_cities(road_map):
    """
    Prints a list of cities, along with their locations.
    Print only one or two digits after the decimal point.
    """

    n = []

    for i in range(len(road_map)):
        n.extend(road_map[i][1:])
    print(n)

def compute_total_distance(road_map):
    """
    Returns, as a floating point number, the sum of the distances of all 
    the connections in the `road_map`. Remember that it's a cycle, so that 
    (for example) in the initial `road_map`, Wyoming connects to Alabama...
    """

    d = 0.0
    for i in range(0, len(road_map)):
        d += math.sqrt((road_map[i][2] - road_map[(i + 1) % len(road_map)][2])**2 + (road_map[i][3] - road_map[(i + 1) % len(road_map)][3])**2)

    return d

def swap_cities(road_map, index1, index2):
    """
    Take the city at location `index` in the `road_map`, and the 
    city at location `index2`, swap their positions in the `road_map`, 
    compute the new total distance, and return the tuple 

        (new_road_map, new_total_distance)

    Allow for the possibility that `index1=index2`,
    and handle this case correctly.
    """
    road_map[index1], road_map[index2] = road_map[index2], road_map[index1]
    return road_map, compute_total_distance(road_map)


def shift_cities(road_map):
    """
    For every index i in the `road_map`, the city at the position i moves
    to the position i+1. The city at the last position moves to the position
    0. Return the new road map. 
    """
    road_map[:] = road_map[-1:] + road_map[:-1]
    return road_map


def find_best_cycle(road_map):
    """
    Using a combination of `swap_cities` and `shift_cities`, 
    try `10000` swaps/shifts, and each time keep the best cycle found so far. 
    After `10000` swaps/shifts, return the best cycle found so far.
    Use randomly generated indices for swapping.
    """

    shortest_distance = compute_total_distance(road_map)
    for i in range(0, 10001):
        swap_cities(road_map, random.randint(0, 49), random.randint(0, 49))
        shift_cities(road_map)
        if compute_total_distance(road_map) < shortest_distance:
            shortest_distance = compute_total_distance(road_map)
    return shortest_distance

def print_map(road_map):
    """
    Prints, in an easily understandable format, the cities and 
    their connections, along with the cost for each connection 
    and the total cost.
    """

    for i in range(0, len(road_map)):
        dist = math.sqrt((road_map[i][2] - road_map[(i + 1) % len(road_map)][2])**2 + (road_map[i][3] - road_map[(i + 1) % len(road_map)][3])**2)
        print(f"City: {road_map[i][1]}, State: {road_map[i][0]}, Distance to the next City ({road_map[(i + 1) % len(road_map)][1]}) is: {round(dist, 2)}")


    print("Total distance starting from point 1 to the last point 50: ", compute_total_distance(road_map))

def main():
    """
    Reads in, and prints out, the city data, then creates the "best"
    cycle and prints it out."""
    try:
        x = read_cities('city-data.txt')
        find_best_cycle(x)
        print_map(x)
    except Exception as error:
        print("Your file could no be opened because of the following reason: ", error)


if __name__ == "__main__": #keep this in
    main()

cities = read_cities("city-data.txt")
