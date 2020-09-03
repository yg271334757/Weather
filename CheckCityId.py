import json

class CheckCityId():

    def __init__(self, cityname):
        self.cityname = cityname
    

    def CheckId(self):
        with open(r"./CityData/CityId.json","r",encoding="utf8") as f:
            load_dict = json.load(f)
            for item in load_dict:
                if item["city_name"] == self.cityname:
                    return item["city_code"]


if __name__ == "__main__":
    cci = CheckCityId("北京").CheckId()
    print(cci)
