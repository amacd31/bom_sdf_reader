7-day Streamflow Forecast web access
=======================================

Basic library for reading 7-day Streamflow Forecasts supplied by the Australian Bureau of Meteorology.

At present CSV data is only provided to registered users of the 7-day Streamflow service.
Therefore this code requires the credentials to be able to log into the 7-Day Streamflow service and fetch data.

Dependencies
------------

Requires Python 2.7, 3.4 or greater (mostly tested with Python 2.7 on Linux).
Depends on pandas and requests.

Usage
-----

The SDFReader class can be imported then instantiated as an object containing meta-information about the available forecast locations. Site information for all available locations are stored on the object after instantiation. Forecasts are retrieved from the Bureau of Meteorology web site on each request for the forecast data.

.. code:: python

    import bom_sdf_reader
    # Replace the credentials here with the username and password used to
    # access the 7-day streamflow website
    sdf_reader = bom_sdf_reader.SDFReader(('sdf_reg_username', 'sdf_reg_user_password'))

    # Retrieve the current forecast for '410730'
    sdf_reader.get_forecast('410730')

Notes
-----

This is an experiment against what is currently available on the Bureau of Meteorology website and should not be considered a stable API.
