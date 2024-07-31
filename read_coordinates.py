from osgeo import gdal
import sys
from pyproj import Transformer

# function to get the coordinates of the corners of a raster
def get_raster_corners(raster_path):
    """
    Retrieves the coordinates of the corners and center of a raster image.

    Args:
        raster_path (str): The path to the raster image.

    Returns:
        dict: A dictionary containing the coordinates of the corners and center of the raster image.
              The keys of the dictionary are:
              - "Upper Left": The coordinates of the upper left corner.
              - "Lower Left": The coordinates of the lower left corner.
              - "Upper Right": The coordinates of the upper right corner.
              - "Lower Right": The coordinates of the lower right corner.
              - "Center": The coordinates of the center of the raster image.
    """
    dataset = gdal.Open(raster_path)
    width = dataset.RasterXSize
    height = dataset.RasterYSize
    gt = dataset.GetGeoTransform()

    def get_coords(x, y):
        x_coord = gt[0] + x * gt[1] + y * gt[2]
        y_coord = gt[3] + x * gt[4] + y * gt[5]
        return (x_coord, y_coord)

    corners = {
        "Upper Left": get_coords(0, 0),
        "Lower Left": get_coords(0, height),
        "Upper Right": get_coords(width, 0),
        "Lower Right": get_coords(width, height),
        "Center": get_coords(width // 2, height // 2)
    }
    
    return corners

# function to convert coordinates from EPSG:3857 to EPSG:4326
from pyproj import Transformer

def convert_coordinates(coords):
    """
    Converts coordinates from EPSG:3857 to EPSG:4326.

    Args:
        coords (tuple): A tuple containing the x and y coordinates.

    Returns:
        tuple: A tuple containing the converted latitude and longitude coordinates.
    """
    transformer = Transformer.from_crs("epsg:3857", "epsg:4326", always_xy=True)
    return transformer.transform(coords[0], coords[1])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python read_coordinates.py <raster_path>")
        sys.exit(1)

    raster_path = sys.argv[1]
    corners = get_raster_corners(raster_path)

    for corner, coords in corners.items():
        lat_long = convert_coordinates(coords)
        print(f"{corner}: {lat_long}")
