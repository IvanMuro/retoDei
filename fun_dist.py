import numpy as np

from astropy import units as u
import astropy.constants as const
from astropy.coordinates import SkyCoord


def calc_dist(dif_x, dif_y):
    """ 
    Function that calculates the 2D-euclidean distance between two given positions
    
    Parameters:
    dif_x, dif_y (float or list): difference between coordinates x and y

    Returns:
    distance in the units of x and y
    """
    return np.sqrt(dif_x**2 + dif_y**2)

def calc_sep_astropy(lon_i, lon_f, lat_i, lat_f):
    """ 
    Function that uses Astropy separation function (see https://docs.astropy.org/en/stable/coordinates/matchsep.html) 
    to calculate the distance between two given positions

    Parameters:
    lon_i, lon_f, lat_i, lat_f (float): Input longitude and latitude for initial and final positions

    Returns:
    distance in km
    
    """
    
    c1 = SkyCoord(lon_i, lat_i, distance=const.R_earth.to(u.km), frame='icrs')
    c2 = SkyCoord(lon_f, lat_f, distance=const.R_earth.to(u.km), frame='icrs')
    sep = np.abs( (c1.separation_3d(c2)).value )
    
    return sep

def haversine(lat1, lon1, lat2, lon2):
    """
    Calculate the great-circle distance between two points
    on the Earth specified in decimal degrees, using Haversine formula
    (see https://en.wikipedia.org/wiki/Haversine_formula)
    
    Parameters:
    lat1, lon1, lat2, lon2 (float or list): input latitudes and longitudes in degrees
    
    Returns:
    distance in kilometres
    """
    
    lat1, lon1 = lat1.to(u.rad), lon1.to(u.rad)
    lat2, lon2 = lat2.to(u.rad), lon2.to(u.rad)

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = np.sin(dlat / 2)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon / 2)**2
    c = (2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))).value

    # Calculate the distance
    distance = const.R_earth * c
    return float(distance.to(u.km).value)

