# Turkey Cities API

🇹🇷 Türkiye illeri ve ilçeleri için ücretsiz ve açık kaynak API.

---

## 📌 Proje Hakkında

Bu API, Türkiye'deki iller (şehirler) ve ilçeler hakkında kolayca bilgi almanızı sağlar.  
FastAPI kullanılarak geliştirilmiş olup JSON formatında veri döner.  
Proje, "Audi A4 Alana Kadar Yazılım İşleri" serisinin bir parçasıdır 🚗💻

---

## 🚀 Özellikler

- Plaka koduna göre şehir ismi öğrenme  
- Şehir adına göre plaka kodu öğrenme  
- Şehir adına/plaka koduna göre ilçeleri listeleme  
- Basit, hızlı ve kullanımı kolay REST API

---

## 🛠 Teknolojiler

- Python 3.11+  
- FastAPI  
- JSON veri kaynağı

---

## 📖 API Endpoints

| Endpoint                                | Açıklama                              | Parametre        |
|----------------------------------------|-------------------------------------|------------------|
| `GET /`                                | Hoşgeldiniz mesajı                   | -                |
| `GET /city/city_name_by_id/{id}`       | Plaka koduna göre şehir ismi         | `id` (int)       |
| `GET /city/city_id_by_name/{city_name}`| Şehir adına göre plaka kodu           | `city_name` (str)|
| `GET /city/city_districts_by_name/{city_name}` | Şehir adına göre ilçeleri listeler | `city_name` (str)|
| `GET /city/city_districts_by_id/{id}`  | Plaka koduna göre ilçeleri listeler | `id` (int)       |

---

## 🔧 Kullanım Örneği

```bash
curl http://localhost:8000/city/city_name_by_id/34

{
  "name": "İstanbul"
}
```

# 📁 Veri Formatı (data.json)

```json

[
  {
    "il": "İstanbul",
    "plaka": 34,
    "ilceleri": ["Kadıköy", "Beşiktaş", "Üsküdar"]
  },
  {
    "il": "İzmir",
    "plaka": 35,
    "ilceleri": ["Bornova", "Karşıyaka", "Konak"]
  }
]
```

# 📥 Kurulum ve Çalıştırma

```bash
git clone https://github.com/sairus-cyr/turkey-il-ilce-api.git
cd turkey-il-ilce-api
pip install -r requirements.txt
uvicorn main:app --reload
```

# 📄 Lisans
MIT License © 2025 [Burak Eminç]
