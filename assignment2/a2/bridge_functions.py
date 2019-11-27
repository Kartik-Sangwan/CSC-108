""" 
Assignment 2: Bridges

The data used for this assignment is a subset of the data found in:
https://www.ontario.ca/data/bridge-conditions
"""

import csv
import math
from typing import List, TextIO

ID_INDEX = 0
NAME_INDEX = 1
HIGHWAY_INDEX = 2
LAT_INDEX = 3
LON_INDEX = 4
YEAR_INDEX = 5
LAST_MAJOR_INDEX = 6
LAST_MINOR_INDEX = 7
NUM_SPANS_INDEX = 8
SPAN_LENGTH_INDEX = 9
LENGTH_INDEX = 10
LAST_INSPECTED_INDEX = 11
BCIS_INDEX = 12

HIGH_PRIORITY_BCI = 60   
MEDIUM_PRIORITY_BCI = 70
LOW_PRIORITY_BCI = 100

HIGH_PRIORITY_RADIUS = 500  
MEDIUM_PRIORITY_RADIUS = 250
LOW_PRIORITY_RADIUS = 100

EARTH_RADIUS = 6371

####### BEGIN HELPER FUNCTIONS ####################

def read_data(csv_file: TextIO) -> List[List[str]]:
    """Read and return the contents of the open CSV file csv_file as a list of
    lists, where each inner list contains the values from one line of csv_file.

    Docstring examples not given since results depend on csv_file.
    """ 

    data = []
    lines = csv.reader(csv_file)
    for line in lines:            
        data.append(line)
    data = data[2:]
    return data


def calculate_distance(lat1: float, lon1: float,
                       lat2: float, lon2: float) -> float:
    """Return the distance in kilometers between the two locations defined by   
    (lat1, lon1) and (lat2, lon2), rounded to the nearest meter.
    
    >>> calculate_distance(43.659777, -79.397383, 43.657129, -79.399439)
    0.338
    >>> calculate_distance(43.42, -79.24, 53.32, -113.30)
    2713.226
    """

    # This function uses the haversine function to find the
    # distance between two locations. You do NOT need to understand why it
    # works. You will just need to call on the function and work with what it
    # returns.
    # Based on code at goo.gl/JrPG4j

    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = (math.radians(lon1), math.radians(lat1), 
                              math.radians(lon2), math.radians(lat2))

    # haversine formula t
    lon_diff = lon2 - lon1 
    lat_diff = lat2 - lat1 
    a = (math.sin(lat_diff / 2) ** 2
         + math.cos(lat1) * math.cos(lat2) * math.sin(lon_diff / 2) ** 2)
    c = 2 * math.asin(math.sqrt(a))
    
    return round(c * EARTH_RADIUS, 3)


####### END HELPER FUNCTIONS ####################

### SAMPLE DATA TO USE IN DOCSTRING EXAMPLES ####

THREE_BRIDGES_UNCLEANED = [
    ['1 -  32/', 'Highway 24 Underpass at Highway 403', '403', '43.167233',
     '-80.275567', '1965', '2014', '2009', '4',
     'Total=64  (1)=12;(2)=19;(3)=21;(4)=12;', '65', '04/13/2012', '72.3', '',
     '72.3', '', '69.5', '', '70', '', '70.3', '', '70.5', '', '70.7', '72.9',
     ''],
    ['1 -  43/', 'WEST STREET UNDERPASS', '403', '43.164531', '-80.251582',
     '1963', '2014', '2007', '4',
     'Total=60.4  (1)=12.2;(2)=18;(3)=18;(4)=12.2;', '61', '04/13/2012',
     '71.5', '', '71.5', '', '68.1', '', '69', '', '69.4', '', '69.4', '',
     '70.3', '73.3', ''],
    ['2 -   4/', 'STOKES RIVER BRIDGE', '6', '45.036739', '-81.33579', '1958',
     '2013', '', '1', 'Total=16  (1)=16;', '18.4', '08/28/2013', '85.1',
     '85.1', '', '67.8', '', '67.4', '', '69.2', '70', '70.5', '', '75.1', '',
     '90.1', '']
    ]

THREE_BRIDGES = [[1, 'Highway 24 Underpass at Highway 403', '403', 43.167233,
                  -80.275567, '1965', '2014', '2009', 4,
                  [12.0, 19.0, 21.0, 12.0], 65.0, '04/13/2012',
                  [72.3, 69.5, 70.0, 70.3, 70.5, 70.7, 72.9]],
                 [2, 'WEST STREET UNDERPASS', '403', 43.164531, -80.251582,
                  '1963', '2014', '2007', 4, [12.2, 18.0, 18.0, 12.2], 61.0, 
                  '04/13/2012', [71.5, 68.1, 69.0, 69.4, 69.4, 70.3,
                                 73.3]],
                 [3, 'STOKES RIVER BRIDGE', '6', 45.036739, -81.33579, '1958',
                  '2013', '', 1, [16.0], 18.4, '08/28/2013',
                  [85.1, 67.8, 67.4, 69.2, 70.0, 70.5, 75.1, 90.1]]
                ]

#################################################
def format_data(data: List[List[str]]) -> None:  
    """Modify data so that it follows the format outlined in the 
    'Data formatting' section of the assignment handout.
    
    >>> d = THREE_BRIDGES_UNCLEANED
    >>> format_data(d)
    >>> d == THREE_BRIDGES
    True
    """
    
    j = 1 
    for bridge in data:
        bridge[ID_INDEX] = j
        j = j + 1
        bridge[LAT_INDEX] = float(bridge[LAT_INDEX])
        bridge[LON_INDEX] = float(bridge[LON_INDEX])
        bridge[NUM_SPANS_INDEX] = int(bridge[NUM_SPANS_INDEX])
        span = bridge[SPAN_LENGTH_INDEX]
        result = []
        for i in range(len(span)):
            if span[i] == ')':
                result = result + [(float(span[i + 2: span.find(';', i)]))]
        bridge[SPAN_LENGTH_INDEX] = result
        if bridge[LENGTH_INDEX] == '':
            bridge[LENGTH_INDEX] = 0.0
        else:
            bridge[LENGTH_INDEX] = float(bridge[LENGTH_INDEX])
        strip_result = []
        strip = bridge[BCIS_INDEX + 1:]
        for value in strip:
            if value != '':
                strip_result = strip_result + [float(value)]
        bridge[BCIS_INDEX] = strip_result
        bridge[:] = bridge[:BCIS_INDEX + 1]  
        
        
def get_bridge(bridge_data: List[list], bridge_id: int) -> list:
    """Return the data for the bridge with id bridge_id from bridge_data. If
    there is no bridge with the given id, return an empty list.  
    
    >>> result = get_bridge(THREE_BRIDGES, 1)
    >>> result == [1, 'Highway 24 Underpass at Highway 403', '403', 43.167233, \
                  -80.275567, '1965', '2014', '2009', 4, \
                  [12.0, 19.0, 21.0, 12.0], 65, '04/13/2012', \
                  [72.3, 69.5, 70.0, 70.3, 70.5, 70.7, 72.9]]
    True
    """
    
    if bridge_id <= len(bridge_data):
        return bridge_data[bridge_id - 1]
    else:
        return []

def get_average_bci(bridge_data: List[list], bridge_id: int) -> float:
    """Return the average BCI for the bridge with bridge_id from bridge_data.
    If there is no bridge with the id bridge_id, return 0.0. If there are no
    BCIs for the bridge with id bridge_id, return 0.0.
    
    >>> get_average_bci(THREE_BRIDGES, 1)   
    70.88571428571429
    >>> get_average_bci(THREE_BRIDGES, 4)
    0.0
    """
    
    sum = 0
    bridge_details = get_bridge(bridge_data, bridge_id)
    if bridge_details == []:
        return 0.0
    elif bridge_details[BCIS_INDEX] == []:
        return 0.0
    else:
        length = len(bridge_details[BCIS_INDEX])
        for bci in bridge_details[BCIS_INDEX]:
            sum = sum + bci
        return sum/length    
            
def get_total_length_on_highway(bridge_data: List[list], highway: str) -> float:
    """Return the total length of bridges in bridge_data on highway.
    Use zero for the length of bridges that do not have a length provided.
    If there are no bridges on highway, return 0.0.
    
    >>> get_total_length_on_highway(THREE_BRIDGES, '403')
    126.0
    >>> get_total_length_on_highway(THREE_BRIDGES, '401')
    0.0
    """
    
    sum = 0.0
    for item in bridge_data:  
        if item[HIGHWAY_INDEX] == highway:
            sum = sum + item[LENGTH_INDEX] 
    return sum
         

def get_distance_between(bridge1: list, bridge2: list) -> float:
    """Return the distance in kilometres, rounded to the nearest metre
    (i.e., 3 decimal places), between the two bridges bridge1 and bridge2.
        
    >>> get_distance_between(get_bridge(THREE_BRIDGES, 1), \
                                 get_bridge(THREE_BRIDGES, 2))
    1.968
    """
    
    lat1 = bridge1[LAT_INDEX]
    lon1 = bridge1[LON_INDEX]
    lat2 = bridge2[LAT_INDEX]
    lon2 = bridge2[LON_INDEX]
    return calculate_distance(lat1, lon1, lat2, lon2)
    
def find_closest_bridge(bridge_data: List[list], bridge_id: int) -> int:
    """Return the id of the bridge in bridge_data that has the shortest
    distance to the bridge with id bridge_id.
    
    Precondition: a bridge with bridge_id is in bridge_data, and there are
    at least two bridges in bridge_data
    
    >>> find_closest_bridge(THREE_BRIDGES, 2)
    1
    """
    
    bridge_details = get_bridge(bridge_data, bridge_id)
    lat1 = bridge_details[LAT_INDEX]
    lon1 = bridge_details[LON_INDEX]
    lat2 = bridge_data[0][LAT_INDEX]
    lon2 = bridge_data[0][LON_INDEX]
    if bridge_data[0] != bridge_details:
        shortest_distance = calculate_distance(lat1, lon1, lat2, lon2)
        id = bridge_data[0][ID_INDEX]
    else:
        lat4 = bridge_data[1][LAT_INDEX]
        lon4 = bridge_data[1][LON_INDEX]
        shortest_distance = calculate_distance(lat1, lon1, lat4, lon4)
        id = bridge_data[1][ID_INDEX]
    for bridge in bridge_data:
        lat3 = bridge[LAT_INDEX]
        lon3 = bridge[LON_INDEX]
        new_shortest_distance = calculate_distance(lat1, lon1, lat3, lon3)
        if bridge != bridge_details and new_shortest_distance < \
                                         shortest_distance:
            shortest_distance = new_shortest_distance
            id = bridge[ID_INDEX]
    return id
def find_bridges_in_radius(bridge_data: List[list], lat: float, long: float,
                           distance: float) -> List[int]:
    """Return the IDs of the bridges that are within radius distance
    from (lat, long).
    
    >>> find_bridges_in_radius(THREE_BRIDGES, 43.10, -80.15, 50)
    [1, 2]
    """
  
    id = []
    for bridge in bridge_data:
        lat1 = bridge[LAT_INDEX]
        lon1 = bridge[LON_INDEX]
        distance1 = calculate_distance(lat, long, lat1, lon1)
        if distance1 < distance:
            id = id + [bridge[ID_INDEX]]
    return id

def get_bridges_with_bci_below(bridge_data: List[list], bridge_ids: List[int],
                               bci_limit: float) -> List[int]:
    """Return the IDs of the bridges with ids in bridge_ids whose most
    recent BCIs are less than or equal to bci_limit.
    
    >>> get_bridges_with_bci_below(THREE_BRIDGES, [1, 2], 72)
    [2]
    """
    
    id = []
    for bridge in bridge_data:
        if bridge[ID_INDEX] in bridge_ids:
            if bridge[BCIS_INDEX][0] <= bci_limit:
                id = id + [bridge[ID_INDEX]]
    return id
def get_bridges_containing(bridge_data: List[list], search: str) -> List[int]:
    """
    Return a list of IDs of bridges whose names contain search (case
    insensitive).
    
    >>> get_bridges_containing(THREE_BRIDGES, 'underpass')
    [1, 2]
    >>> get_bridges_containing(THREE_BRIDGES, 'Highway')
    [1]
    """

    id = []
    search = search.lower()
    for bridge in bridge_data:
        bridge[NAME_INDEX] = bridge[NAME_INDEX].lower()
        if search in bridge[NAME_INDEX]:
            id = id + [bridge[ID_INDEX]]
    return id
def assign_inspectors(bridge_data: List[list], inspectors: List[List[float]],
                      max_bridges: int) -> List[List[int]]:
    """Return a list of bridge IDs to be assigned to each inspector in
    inspectors. inspectors is a list containing (latitude, longitude) pairs
    representing each inspector's location.
    
    At most max_bridges bridges should be assigned to an inspector, and each
    bridge should only be assigned once (to the first inspector that can
    inspect that bridge).
    
    See the "Assigning Inspectors" section of the handout for more details.
    
    >>> assign_inspectors(THREE_BRIDGES, [[43.10, -80.15]], 1)
    [[1]]
    >>> assign_inspectors(THREE_BRIDGES, [[43.10, -80.15]], 2)
    [[1, 2]]
    >>> assign_inspectors(THREE_BRIDGES, [[43.10, -80.15]], 3)
    [[1, 2]]
    >>> assign_inspectors(THREE_BRIDGES, [[43.20, -80.35], [43.10, -80.15]], 1)
    [[1], [2]]
    >>> assign_inspectors(THREE_BRIDGES, [[43.20, -80.35], [43.10, -80.15]], 2)
    [[1, 2], []]
    >>> assign_inspectors(THREE_BRIDGES, [[43.20, -80.35], [45.0368, -81.34]], 2)
    [[1, 2], [3]]
    >>> assign_inspectors(THREE_BRIDGES, [[38.691, -80.85], [43.20, -80.35]], 2)
    [[], [1, 2]]
    """

    f_result = []
    t_result = []
    for item in inspectors:
        
        result = []    
        h_bridge_ids = find_bridges_in_radius(bridge_data, item[0], item[1], \
                                              HIGH_PRIORITY_RADIUS)
        h_ids = get_bridges_with_bci_below(bridge_data, h_bridge_ids, \
                                           HIGH_PRIORITY_BCI)
        m_bridge_ids = find_bridges_in_radius(bridge_data, item[0], \
                                              item[1], MEDIUM_PRIORITY_RADIUS)
        m_ids = get_bridges_with_bci_below(bridge_data, m_bridge_ids, \
                                           MEDIUM_PRIORITY_BCI)
        l_bridge_ids = find_bridges_in_radius(bridge_data, item[0], \
                                              item[1], LOW_PRIORITY_RADIUS)
        l_ids = get_bridges_with_bci_below(bridge_data, l_bridge_ids, \
                                           LOW_PRIORITY_BCI)
        all_ids = h_ids + m_ids + l_ids
        for id in all_ids:
            if len(result) < max_bridges:
                if not ([id] in f_result or id in t_result):
                    t_result = t_result + [id]
                    result = result + [id]
        f_result.append(result)   
 
    return f_result
             

def inspect_bridges(bridge_data: List[list], bridge_ids: List[int], date: str, 
                    bci: float) -> None:
    """Update the bridges in bridge_data with id in bridge_ids with the new
    date and BCI score for a new inspection.
    
    >>> bridges = [[1, 'Highway 24 Underpass at Highway 403', '403', 43.167233,\
                  -80.275567, '1965', '2014', '2009', 4, \
                  [12.0, 19.0, 21.0, 12.0], 65, '04/13/2012', \
                  [72.3, 69.5, 70.0, 70.3, 70.5, 70.7, 72.9]], \
                 [2, 'WEST STREET UNDERPASS', '403', 43.164531, -80.251582, \
                  '1963', '2014', '2007', 4, [12.2, 18.0, 18.0, 12.2], 61, \
                  '04/13/2012', [71.5, 68.1, 69.0, 69.4, 69.4, 70.3,\
                                 73.3]], \
                 [3, 'STOKES RIVER BRIDGE', '6', 45.036739, -81.33579, '1958', \
                  '2013', '', 1, [16.0], 18.4, '08/28/2013', \
                  [85.1, 67.8, 67.4, 69.2, 70.0, 70.5, 75.1, 90.1]] \
                 ]
    >>> inspect_bridges(bridges, [1], '09/15/2018', 71.9)
    >>> bridges == [[1, 'Highway 24 Underpass at Highway 403', '403', \
                     43.167233, -80.275567, '1965', '2014', '2009', 4, \
                     [12.0, 19.0, 21.0, 12.0], 65, '09/15/2018', \
                     [71.9, 72.3, 69.5, 70.0, 70.3, 70.5, 70.7, 72.9]], \
                    [2, 'WEST STREET UNDERPASS', '403', 43.164531, -80.251582, \
                     '1963', '2014', '2007', 4, [12.2, 18.0, 18.0, 12.2], \
                     61, '04/13/2012', [71.5, 68.1, 69.0, 69.4, 69.4, \
                                          70.3, 73.3]], \
                    [3, 'STOKES RIVER BRIDGE', '6', 45.036739, -81.33579, \
                     '1958', '2013', '', 1, [16.0], 18.4, '08/28/2013', \
                     [85.1, 67.8, 67.4, 69.2, 70.0, 70.5, 75.1, 90.1]] \
                   ]
    True
    """
    
    for id in bridge_ids:
        bridge = get_bridge(bridge_data, id)
        bridge[LAST_INSPECTED_INDEX] = date
        bridge[BCIS_INDEX] = [bci] + bridge[BCIS_INDEX]


def add_rehab(bridge_data: List[list], bridge_id: int, new_date: str, 
              is_major: bool) -> None:
    """
    Update the bridge with the id bridge_id to have its last rehab set to
    new_date. If is_major is True, update the major rehab date. Otherwise,
    update the minor rehab date.
    
    >>> bridges = [[1, 'Highway 24 Underpass at Highway 403', '403', 43.167233,\
                  -80.275567, '1965', '2014', '2009', 4, \
                  [12.0, 19.0, 21.0, 12.0], 65, '04/13/2012', \
                  [72.3, 69.5, 70.0, 70.3, 70.5, 70.7, 72.9]], \
                 [2, 'WEST STREET UNDERPASS', '403', 43.164531, -80.251582, \
                  '1963', '2014', '2007', 4, [12.2, 18.0, 18.0, 12.2], 61, \
                  '04/13/2012', [71.5, 68.1, 69.0, 69.4, 69.4, 70.3,\
                                 73.3]], \
                 [3, 'STOKES RIVER BRIDGE', '6', 45.036739, -81.33579, '1958', \
                  '2013', '', 1, [16.0], 18.4, '08/28/2013', \
                  [85.1, 67.8, 67.4, 69.2, 70.0, 70.5, 75.1, 90.1]] \
                 ]
    >>> add_rehab(bridges, 1, '2018', False)
    >>> bridges == [[1, 'Highway 24 Underpass at Highway 403', '403', \
                     43.167233, -80.275567, '1965', '2014', '2018', 4, \
                     [12.0, 19.0, 21.0, 12.0], 65, '04/13/2012', \
                     [72.3, 69.5, 70.0, 70.3, 70.5, 70.7, 72.9]], \
                    [2, 'WEST STREET UNDERPASS', '403', 43.164531, -80.251582, \
                     '1963', '2014', '2007', 4, [12.2, 18.0, 18.0, 12.2], \
                     61, '04/13/2012', [71.5, 68.1, 69.0, 69.4, 69.4, \
                                          70.3, 73.3]], \
                    [3, 'STOKES RIVER BRIDGE', '6', 45.036739, -81.33579, \
                     '1958', '2013', '', 1, [16.0], 18.4, '08/28/2013', \
                     [85.1, 67.8, 67.4, 69.2, 70.0, 70.5, 75.1, 90.1]] \
                   ]
    True
    """
  
    bridge = get_bridge(bridge_data, bridge_id)
    if is_major:
        bridge[LAST_MAJOR_INDEX] = new_date
    else:
        bridge[LAST_MINOR_INDEX] = new_date
        



if __name__ == '__main__':
    #pass 

    # To test your code with larger lists, you can uncomment the code below to
    # read data from the provided CSV file.
    bridges = read_data(open('bridge_data_small.csv'))
    format_data(bridges)
    
    #For example,
    print(get_bridge(bridges, 3))
    expected = [3, 'NORTH PARK STEET UNDERPASS', '403', 43.165918, -80.263791,
                '1962', '2013', '2009', 4, [12.2, 18.0, 18.0, 12.2], 60.8,
                '04/13/2012', [71.4, 69.9, 67.7, 68.9, 69.1, 69.9, 72.8]]
    print('Testing get_bridge: ', \
         get_bridge(bridges, 3) == expected)
    
