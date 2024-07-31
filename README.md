# gps-coordinates-reader
Tutorial to get georeferenced images and read coordinates

# Get maps images

The gps maps are displayed via latitutinal and longitudinal coordinates and therefore need to be very accurate. We need a way to get images with good resolution that also contain gps coordinates.

We want to obtain a ```.tif``` image that will contain metadata representing the gps coordinates of the map

## QGIS
QGIS is one of the applications that you can use to get satellite images and use them to save the gps coordinates that we need.

### Installation

The application is available for many operating systems, and download instructions are available at the following [link](https://qgis.org/download/).

### Step to get satellite images

- Open QGIS
- Create a new project via ```Project->New```
  
  ![2_NewProject](https://github.com/user-attachments/assets/a9f9f2a1-169b-49db-b0e4-830876db127d)

- Install plugins from ```Plugins->Manage and Install Plugins...```
  
  ![3_GetPlugin](https://github.com/user-attachments/assets/12ade4e0-ca54-4a49-95c2-fa8e7b289fc4)
  - Search ```QuickMapServices``` in the search box and install it

    ![4_SearchQuickMapServices](https://github.com/user-attachments/assets/779bd781-2b99-42d2-b600-8ae3156a3f8f)

- Download more maps

  ![5_SettingsQuickMapServices](https://github.com/user-attachments/assets/577c8f63-332a-4d31-932a-0051fbd7c4bf)

  - Get contributed Pack
    
    ![6_GetContributedMap](https://github.com/user-attachments/assets/8fc8c364-5e21-4b59-88d8-37c016027091)

- Select Google Satellite map
    
  ![7_GoogleSatellite](https://github.com/user-attachments/assets/a723aa3b-6f05-479d-a5ef-4558ede8d563)

- Search ```Raster tools``` in ```Processing Toolbox```. Click [here](https://docs.qgis.org/3.4/en/docs/user_manual/processing_algs/qgis/rastertools.html) to see the documentation

  ![8_RasterTools](https://github.com/user-attachments/assets/21242fa9-516d-4e9d-b738-2e711cfe874c)

  - Select the area of the image you want to create

  ![9_SelectArea](https://github.com/user-attachments/assets/acfcf6bd-9c01-4e92-9619-ee7e3e720c0e)

  - Select the map units per pixels (the lower the value, the better quality the image will have)
    - Be careful, if the image area is large and the value of map units per pixels is too small, the algorithm will take longer to return an image

    ![10_MapsUnitsPerPixel](https://github.com/user-attachments/assets/cb60dd74-7517-49af-92d8-375ec628dc90)

  - Save to file or save a temporary file on QGIS (the output image will be a .tif file)

    ![11_SaveToFileTif](https://github.com/user-attachments/assets/d79d9f31-b007-48ca-b356-fd933a8a250e)

    - If you want to save the image to a temporary file to get a preview, it will be added as a layer and then you will have to export it by right-clicking and going to ```Export->Save As```
   
There may be some problems with the image created:
  - Area of the image different from the one selected:
    - you can try creating the image again by changing the value of ```Tile size```
    - many times this error is given because the selected area is smaller than the ```Tile size``` so you have to decrease that value as well
  - Poor image quality:
    - you can try creating the image one more time by changing the ```map units per pixel``` value

If you need it, you can create a ```.jpg``` file of the image. To do this we can use any application that allows us to export images to ```.jpg``` files
   
If the image quality is still not good enough, you can try increasing the image resolution using other applications such as Photoshop. 

**Be careful** when modifying the ```.tif``` file because it may lose metadata

# Get coordinates from .tif file
Now that we have obtained both the ```.tif``` file we can go ahead and get the gps coordinates saved in the ```.tif``` file

The first step is to install the dependencies via the command:
```
pip install -r requirements.txt
```
Now all that remains is to execute the script via the command:
```
python3 read_coordinates.py <raster_file_path>
```
> [!WARNING]
> ```raster_file_path``` must be the ```.tif``` file created before with the georeferencing metadata.

The result of the script is something like this:
```
corner: (longitude, latitude)
Upper Left: (10.013347232876077, 44.684102509035036)
Lower Left: (10.013347232876077, 44.67756187921092)
Upper Right: (10.031744729894845, 44.684102509035036)
Lower Right: (10.031744729894845, 44.67756187921092)
Center: (10.022545981385461, 44.68083228642004)
```
> [!WARNING]
> The coordinates are given in a ```(longitude, latitude)``` format
