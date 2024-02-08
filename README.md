# School District Locator

The School District Locator is a Python tool designed to map any given street address in the United States to its corresponding school district. Utilizing the U.S. Census Bureau Geocoding Services API for address geocoding and GeoPandas for spatial analysis with school district shapefiles, this tool provides a quick and accurate lookup for determining the school district of a particular address.

## Features

- Address to school district mapping
- Utilizes U.S. Census Bureau Geocoding Services for precise address location
- Spatial analysis with GeoPandas for accurate district identification
- Supports Shapefile boundary file format

## Getting Started

### Prerequisites

Ensure you have Python 3.6+ installed on your system.

### Installation

Clone the repository to your local machine:

```bash
git clone https://github.com/codebyamir/school-district-locator.git
```

Navigate to the cloned directory:

```bash
cd school-district-locator
```

Install the required libraries using pip:

```bash
pip install -r requirements.txt
```

### Download boundary data from NECS

1. Go to https://data-nces.opendata.arcgis.com/datasets/nces::school-district-boundaries-current/about
2. Click Download button to view file formats
3. Look for the Shapefile and click Download
4. This will download a zip file containing the shapefile and associated files
5. Unzip the files into the repo directory
6. Rename the files to:
   - `school_district_boundaries.cpg`
   - `school_district_boundaries.dbf`
   - `school_district_boundaries.prj`
   - `school_district_boundaries.shp`
   - `school_district_boundaries.shx`
   - `school_district_boundaries.xml`

### Usage

To use the School District Locator, run the script from your command line, and enter the requested address information when prompted:

```bash
python3 locator.py
```

Follow the on-screen prompts to input the street address, city, state, and ZIP code for the location you're interested in.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- U.S. Census Bureau for providing the Geocoding Services API.
- The GeoPandas team for their excellent work on the geospatial analysis library.

## Support

For support, please open an issue in the GitHub issue tracker for this project.
