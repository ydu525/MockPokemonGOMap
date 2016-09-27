#!/usr/bin/env python
import s2sphere

from mock_pgoapi import mock_pgoapi as pgoapi

def break_down_area_to_cell(n, s, w, e):
    res = []

    region = s2sphere.RegionCoverer()
    region.min_level = 15
    region.max_level = 15
    p1 = s2sphere.LatLng.from_degrees(n, w)
    p2 = s2sphere.LatLng.from_degrees(s, e)
    cell_ids = region.get_covering(s2sphere.LatLngRect.from_point_pair(p1, p2))
    res += [ cell_id.id() for cell_id in cell_ids ]

    return res

def scan_area(n, s, w, e):
    res = []

    cell_ids = break_down_area_to_cell(n, s, w, e)
    print cell_ids
    #res += s

    return res;

if __name__ == "__main__":
    print scan_area(40.7565138, 40.7473342, -74.0003176, -73.997958)#, api)
