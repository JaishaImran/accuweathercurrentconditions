import json
import urllib.request

from django.shortcuts import render


def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        api_key = 'IQ1LiACniv8nvl5ellykJYSRykRsqkyx'

        source = urllib.request.urlopen(
            'http://dataservice.accuweather.com/locations/v1/cities/search?apikey=' + api_key + '&q=' + city + '&details=true').read()
        # myList1 = requests.get(source).json()
        myList1 = json.loads(source)
        location_key = myList1[0]['Key']
        source2 = urllib.request.urlopen(
            'https://dataservice.accuweather.com/currentconditions/v1/' + location_key + '?apikey=' + api_key + '&details=true').read()
        # myList = requests.get(api).json()
        myList = json.loads(source2)

        data = {
            "LocalObservationDateTime": str(myList[0]['LocalObservationDateTime']),
            "EpochTime": str(myList[0]['EpochTime']),
            "WeatherText": str(myList[0]['WeatherText']),
            "PrecipitationType": str(myList[0]['PrecipitationType']),
            "IsDayTime": str(myList[0]['IsDayTime']),
            "TemperatureMetricValue": str(myList[0]['Temperature']['Metric']['Value']),
            "TemperatureMetricUnitType": str(myList[0]['Temperature']['Metric']['UnitType']),
            "TemperatureImperialValue": str(myList[0]['Temperature']['Imperial']['Value']),
            "TemperatureImperialUnitType": str(myList[0]['Temperature']['Imperial']['UnitType']),
            "RealFeelTemperatureMetricUnitType": str(myList[0]['RealFeelTemperature']['Metric']['UnitType']),
            "RealFeelTemperatureMetricPhrase": str(myList[0]['RealFeelTemperature']['Metric']['Phrase']),
            "RealFeelTemperatureImperialValue": str(myList[0]['RealFeelTemperature']['Imperial']['Value']),
            "RealFeelTemperatureImperialUnitType": str(myList[0]['RealFeelTemperature']['Imperial']['UnitType']),
            "RealFeelTemperatureShadeImperialPhrase": str(myList[0]['RealFeelTemperatureShade']['Imperial']['Phrase']),
            "RelativeHumidity": str(myList[0]['RelativeHumidity']),
            "IndoorRelativeHumidity": str(myList[0]['IndoorRelativeHumidity']),
            "DewPointMetricValue": str(myList[0]['DewPoint']['Metric']['Value']),
            "DewPointImperialValue": str(myList[0]['DewPoint']['Imperial']['Value']),
            "DewPointImperialUnitType": str(myList[0]['DewPoint']['Imperial']['UnitType']),
            'WindDirectionDegrees': str(myList[0]['Wind']['Direction']['Degrees']),
            "WindDirectionLocalized": str(myList[0]['Wind']['Direction']['Localized']),
            "WindDirectionEnglish": str(myList[0]['Wind']['Direction']['English']),
            "WindSpeedMetricValue": str(myList[0]['Wind']['Speed']['Metric']['Value']),
            "WindSpeedMetricUnitType": str(myList[0]['Wind']['Speed']['Metric']['UnitType']),
            "WindSpeedImperialValue": str(myList[0]['Wind']['Speed']['Imperial']['Value']),
            "WindGustSpeedMetricValue": str(myList[0]['WindGust']['Speed']['Metric']['Value']),
            "WindGustSpeedImperialValue": str(myList[0]['WindGust']['Speed']['Imperial']['Value']),
            "UVIndex": str(myList[0]['UVIndex']),
            "UVIndexText": str(myList[0]['UVIndexText']),
            'VisibilityMetricValue': str(myList[0]['Visibility']['Metric']['Value']),
            "VisibilityMetricUnit": str(myList[0]['Visibility']['Metric']['Unit']),
            "VisibilityMetricUnitType": str(myList[0]['Visibility']['Metric']['UnitType']),
            "VisibilityImperialValue": str(myList[0]['Visibility']['Imperial']['Value']),
            "VisibilityImperialUnit": str(myList[0]['Visibility']['Imperial']['Unit']),
            "VisibilityImperialUnitType": str(myList[0]['Visibility']['Imperial']['UnitType']),
            "ObstructionsToVisibility": str(myList[0]['ObstructionsToVisibility']),
            'CloudCover': str(myList[0]['CloudCover']),
            "CeilingMetricValue": str(myList[0]['Ceiling']['Metric']['Value']),
            "CeilingMetricUnit": str(myList[0]['Ceiling']['Metric']['Unit']),
            "CeilingMetricUnitType": str(myList[0]['Ceiling']['Metric']['UnitType']),

            "CeilingImperialValue": str(myList[0]['Ceiling']['Imperial']['Value']),
            "CeilingImperialUnit": str(myList[0]['Ceiling']['Imperial']['Unit']),
            "CeilingImperialUnitType": str(myList[0]['Ceiling']['Imperial']['UnitType']),
            "PressureMetricValue": str(myList[0]['Pressure']['Metric']['Value']),
            "PressureMetricUnit": str(myList[0]['Pressure']['Metric']['Unit']),
            "PressureMetricUnitType": str(myList[0]['Pressure']['Metric']['UnitType']),
            "PressureImperialValue": str(myList[0]['Pressure']['Imperial']['Value']),
            "PressureImperialUnit": str(myList[0]['Pressure']['Imperial']['Unit']),
            "PressureImperialUnitType": str(myList[0]['Pressure']['Imperial']['UnitType']),
            "PressureTendencyLocailzedText": str(myList[0]['PressureTendency']['LocalizedText']),
            "PressureTendencyCode": str(myList[0]['PressureTendency']['Code']),
            "ApparentTemperatureMetricValue": str(myList[0]['ApparentTemperature']['Metric']['Value']),
            "ApparentTemperatureMetricUnit": str(myList[0]['ApparentTemperature']['Metric']['Unit']),
            "ApparentTemperatureMetricUnitType": str(myList[0]['ApparentTemperature']['Metric']['UnitType']),
            "ApparentTemperatureImperialValue": str(myList[0]['ApparentTemperature']['Imperial']['Value']),
            "ApparentTemperatureImperialUnit": str(myList[0]['ApparentTemperature']['Imperial']['Unit']),
            "ApparentTemperatureImperialUnitType": str(myList[0]['ApparentTemperature']['Imperial']['UnitType']),
            "WindChillTemperatureMetricValue": str(myList[0]['WindChillTemperature']['Metric']['Value']),
            "WindChillTemperatureMetricUnit": str(myList[0]['WindChillTemperature']['Metric']['Unit']),
            "WindChillTemperatureMetricUnitType": str(myList[0]['WindChillTemperature']['Metric']['UnitType']),
            "WindChillTemperatureImperialValue": str(myList[0]['WindChillTemperature']['Imperial']['Value']),
            "WindChillTemperatureImperialUnit": str(myList[0]['WindChillTemperature']['Imperial']['Unit']),

            "WindChillTemperatureImperialUnitType": str(myList[0]['WindChillTemperature']['Imperial']['UnitType']),
            "WetBulbTemperatureMetricValue": str(myList[0]['WetBulbTemperature']['Metric']['Value']),
            "WetBulbTemperatureMetricUnit": str(myList[0]['WetBulbTemperature']['Metric']['Unit']),
            "WetBulbTemperatureMetricUnitType": str(myList[0]['WetBulbTemperature']['Metric']['UnitType']),
            "WetBulbTemperatureImperialValue": str(myList[0]['WetBulbTemperature']['Imperial']['Value']),
            "WetBulbTemperatureImperialUnit": str(myList[0]['WetBulbTemperature']['Imperial']['Unit']),
            "WetBulbTemperatureImperialUnitType": str(myList[0]['WetBulbTemperature']['Imperial']['UnitType']),
            "PrecipitationSummaryPrecipitationMetricValue": str(
                myList[0]['PrecipitationSummary']['Precipitation']['Metric']['Value']),
            "PrecipitationSummaryPrecipitationMetricUnit": str(
                myList[0]['PrecipitationSummary']['Precipitation']['Metric']['Unit']),
            "PrecipitationSummaryPrecipitationMetricUnitType": str(
                myList[0]['PrecipitationSummary']['Precipitation']['Metric']['UnitType']),
            "PrecipitationSummaryPrecipitationImperialValue": str(
                myList[0]['PrecipitationSummary']['Precipitation']['Imperial']['Value']),
            "PrecipitationSummaryPrecipitationImperialUnit": str(
                myList[0]['PrecipitationSummary']['Precipitation']['Imperial']['Unit']),
            "PrecipitationSummaryPrecipitationImperialUnitType": str(
                myList[0]['PrecipitationSummary']['Precipitation']['Imperial']['UnitType']),
        }
        print(data)
    else:
        data = {}

    return render(request, "main/index.html", data)
