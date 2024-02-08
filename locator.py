import requests
import geopandas as gpd
from shapely.geometry import Point
from typing import Tuple, Optional

def geocode_address(street: str, city: str, state: str, zip_code: str) -> Optional[Tuple[float, float]]:
    """
    Geocode a street address using the U.S. Census Bureau Geocoding Services API.

    Parameters:
    - street: The street address
    - city: The city name
    - state: The state abbreviation
    - zip_code: The ZIP code

    Returns:
    - A tuple containing the latitude and longitude (lat, lon) of the address, or None if not found.
    """
    url = "https://geocoding.geo.census.gov/geocoder/locations/address"
    params = {
        "street": street,
        "city": city,
        "state": state,
        "zip": zip_code,
        "benchmark": "Public_AR_Current",
        "format": "json",
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raises HTTPError for bad responses

        # Parse the JSON response
        data = response.json()
        if data['result']['addressMatches']:
            match = data['result']['addressMatches'][0]
            coordinates = match['coordinates']
            lat = coordinates['y']
            lon = coordinates['x']
            return (lat, lon)
        else:
            print("No match found for this address.")
            return None
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return None

def find_school_district(lat: float, lon: float) -> str:
    """
    Identifies the school district for a given latitude and longitude using a shapefile.

    This function loads a shapefile containing school district boundaries, creates a point
    from the provided latitude and longitude, and checks which school district polygon contains
    the point. It returns the name of the school district if found.

    Parameters:
    - lat (float): The latitude of the address.
    - lon (float): The longitude of the address.

    Returns:
    - str: The name of the school district the address belongs to, or "District not found" if not found.
    """
    
    # Load the shapefile
    gdf = gpd.read_file('school_district_boundaries.shp')
    
    # Create a Point object from the latitude and longitude
    point = Point(lon, lat)
    
    # Check which polygon from the shapefile contains the point
    # The result is a GeoDataFrame with the rows that match the condition
    containing_district = gdf[gdf.contains(point)]
    
    if not containing_district.empty:
        # Assuming the district name is in a column named 'NAME'
        return containing_district.iloc[0]['NAME']
    else:
        return "District not found."

if __name__ == "__main__":
    street = input("Enter the street address: ")
    city = input("Enter the city: ")
    state = input("Enter the state abbreviation: ")
    zip_code = input("Enter the ZIP code: ")

    coordinates = geocode_address(street, city, state, zip_code)
    
    if coordinates:
        lat, lon = coordinates
        district_name = find_school_district(lat, lon)
        print(f"The address is in the school district: {district_name}")
    else:
        print("Unable to geocode the address.")
