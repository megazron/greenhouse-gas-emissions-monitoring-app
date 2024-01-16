var geometry = 
    /* color: #d63000 */
    /* displayProperties: [
      {
        "type": "rectangle"
      }
    ] */
    ee.Geometry.Polygon(
        [[[79.99994473167, 13.307394504203499],
          [79.99994473167, 12.646318705761495],
          [80.57947354026375, 12.646318705761495],
          [80.57947354026375, 13.307394504203499]]], null, false);


var countries = ee.FeatureCollection('USDOS/LSIB_SIMPLE/2017');


  
  var collection = ee.ImageCollection('COPERNICUS/S5P/NRTI/L3_CO')
  .select('CO_column_number_density')
  .filterDate('2023-01-01', '2023-12-31');
  

var band_viz = {
  min: 0,
  max: 0.05,
  palette: ['black', 'blue', 'purple', 'cyan', 'green', 'yellow', 'red']
};

Map.addLayer(collection.mean().clip(countries), band_viz, 'S5P CO');

var start_time = '2023-01-01'
var end_time = '2023-12-31'

var CO_collection = ee.ImageCollection('COPERNICUS/S5P/NRTI/L3_CO')
.filterBounds(geometry)
.filterDate(start_time,end_time)
.select('CO_column_number_density')
.map(function(a){
  return a.set('month', ee.Image(a).date().get('month'))
})

print(CO_collection)

var months = ee.List(CO_collection.aggregate_array('month')).distinct()
print(months)

var CO_monthly_conc = months.map(function(x){
  return CO_collection.filterMetadata('month', 'equals', x).mean().set('month', x)
})
var CO_final = ee.ImageCollection.fromImages(CO_monthly_conc)

var chart = ui.Chart.image.series(CO_final, geometry,ee.Reducer.mean(), 5000,'month')
.setOptions({
title: 'CO Concentration Year 2023',
vAxis: {title: 'Concentration(μg/m²)'},
hAxis: {title: 'Month'}
})
print(chart)
