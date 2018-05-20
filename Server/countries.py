import os,json
def getCountries():
    countriesFile = os.path.join(os.path.dirname(__file__),'countries.json')
    countriesDict = {}
    with open(countriesFile,'r',encoding="utf8") as file:
       countriesDict = json.load(file)
    countries = []
    print(countriesDict)
    for country in countriesDict:
        countries.append(countriesDict[country]['name'])

    if len(countries)==0:
        return None
    return countries