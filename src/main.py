# # import datetime
# #
# # import pandas as pd
# # from pvlib.forecast import GFS
# #
# # latitude, longitude, tz = 32.2, -110.9, 'US/Arizona'
# # start = pd.Timestamp(datetime.date.today(), tz=tz)
# # end = start + pd.Timedelta(days=7)
# # model = GFS()
# # raw_data = model.get_data(latitude, longitude, start, end)
# # print(raw_data.head())
# # print('')
#
#
from siphon.catalog import TDSCatalog
import xarray as xr
import datetime

#
# Latest GFS TDSCatalog
url = 'https://thredds-jumbo.unidata.ucar.edu/thredds/catalog/grib/NCEP/GFS/Global_0p25deg/latest.xml'
catalog = TDSCatalog(url)

obs = datetime.date.today() + datetime.timedelta(days = 1)
obs_time = datetime.datetime(obs.year, obs.month, obs.day,
                             hour = 6, minute = 0)


def get_netcdf_subset(catalog, variable, obs_time):
    # Boundaries
    south = -15.0
    north = 15.0
    west = 90
    east = 150

    # NetCDF Subset Service Query
    ncss = catalog.datasets[0].subset()
    query = ncss.query()

    query.lonlat_box(west=west, east=east, south=south, north=north)
    query.variables(variable)
    query.time(obs_time)

    data = ncss.get_data(query)
    store = xr.backends.NetCDF4DataStore(data)
    dataset = xr.open_dataset(store)
    return dataset


rain = 'Total_precipitation_surface_Mixed_intervals_Accumulation'
ds_rain = get_netcdf_subset(catalog, rain, obs_time)
    # .sel(time = obs_time)

print(ds_rain.head())


#
#
# import ee
# import eemont
#
#
# ee.Initialize()
# from datetime import date, datetime
#
# # Forecast generated on 10 July 2021 06:00 UTC
# forecast = datetime(2021, 7, 10, 6).strftime('%Y%m%d%H')
# image_name = f'NOAA/GFS0P25/{forecast}F024'
# data = ee.Image(image_name)
# bounds = ee.Geometry.BBox(90, -15, 150, 15)

#
# import getgfs
# f=getgfs.Forecast()
# print('')

nc = xr.open_dataset(r'C:\Users\evvEn\PycharmProjects\wealther\src\Global_0p25deg_GFS_Global_0p25deg_20220812_0600_t.nc')
dd=nc.to_dataframe()
dd.to_csv(r'C:\Users\evvEn\PycharmProjects\wealther\src\t.csv')







