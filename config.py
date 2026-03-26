import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = os.getenv("ADMIN_ID")

SERVICES = {
    "1": ("🛢 May almastrıw", "150 000 so'm"),
    "2": ("🔧 Dvigatel tamirlew", "500 000 so'm"),
    "3": ("🧪 Kompyuter diagnostikası", "60 000 so'm"),
    "4": ("⚙️ Transmissiya tekseriw", "120 000 so'm"),
    "5": ("🛞 Balansirovka", "40 000 so'm"),
    "6": ("🔩 Shina almastrıw", "50 000 so'm"),
    "7": ("🛞 Disk tüzelew", "80 000 so'm"),
    "8": ("🔋 Akkumulyator tekseriw", "30 000 so'm"),
    "9": ("💡 Faralar sazlaw", "25 000 so'm"),
    "10": ("📡 Sensor tekseriw", "70 000 so'm"),
    "11": ("🛑 Tormoz kolodkası almastrıw", "180 000 so'm"),
    "12": ("🛑 Tormoz diskleri tekseriw", "90 000 so'm"),
    "13": ("❄️ Kondicioner toldırıw", "200 000 so'm"),
    "14": ("🧼 Avto jıwıw", "40 000 so'm"),
    "15": ("🧽 Salon tazalaw", "120 000 so'm"),
}