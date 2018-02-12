from geopy.geocoders import ArcGIS


def get_loc(loc):
    """
    (str) -> tuple(float, float)
    Function gets place and returns its coordinates

    param loc: string that is place where the film was filmed
    return: tuple of two floats that are longitude and latitude

    >>> get_loc("North Hollywood, Los Angeles, California, USA")
    (34.2, -118.4)
    >>> get_loc("Jo's Cafe, San Marcos, Texas, USA")
    (29.9, -97.9)
    """
    location = ArcGIS(timeout=10)
    place = location.geocode(loc)
    return (round(place.latitude, 1), round(place.longitude, 1))


if "__main__" == __name__:
    import doctest

    doctest.testmod()
