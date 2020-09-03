import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from UiWeather import Ui_WeatherCheck
import CheckCityId
import requests
import datetime

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_WeatherCheck()
        self.ui.setupUi(self)

    def querWeather(self):
        cityname = self.getCityName()
        cityid = CheckCityId.CheckCityId(cityname).CheckId()
        headers = {'content-type': 'application/json',
           'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'}
        req = requests.get("http://t.weather.itboy.net/api/weather/city/" + str(cityid), headers=headers)
        req.encoding = "utf-8"

        today = datetime.date.today()
        today_info = "今天是:" + str(today) + '\n'
        split_line = '*' * 30 + '\n'

        message = req.json()["data"]

        message_TempNow = "现在温度为:" + message["wendu"] + '\n'
        message_HumiNow = "现在湿度为:" + message["shidu"] + '\n'
        message_Pm25 = "pm2.5为:" + str(message["pm25"]) + '\n'
        message_Pm10 = "pm10为:" + str(message["pm10"]) + '\n'
        message_Quality = "空气质量为:" + message["quality"] + '\n'
        message_Tips = "Tips:" + message["ganmao"]

        result = today_info + split_line + message_TempNow + message_HumiNow + message_Pm25 + message_Pm10 + message_Quality + message_Tips
        self.ui.textEdit_show.setText(result)

    def getCityName(self):
        return self.ui.lineEdit_city.text()





if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())