from fastapi import FastAPI, HTTPException
import json

app = FastAPI()

with open("data.json", "r", encoding="utf-8") as f:
    cities = json.load(f)

@app.get("/")
def root():
    return {"message": "Hello!"}

@app.get("/city/city_name_by_id/{id}")
def name_to_id(id: int):
    for city in cities:
        if city["plaka"] == id:
            return {"name": city["il"]}
    raise HTTPException(status_code=404, detail="Şehir bulunamadı!")

@app.get("/city/city_id_by_name/{city_name}")
def id_to_name(city_name: str):
    city_name_lower = city_name.lower()
    for city in cities:
        if city["il"].lower() == city_name_lower:
            return {"id": city["plaka"]}
    raise HTTPException(status_code=404, detail="Şehir bulunamadı!")

@app.get("/city/city_districts_by_name/{city_name}")
def city_districts_to_name(city_name: str):
    city_name_lower = city_name.lower()
    for city in cities:
        if city["il"].lower() == city_name_lower:
            return {
                "name": city["il"],
                "id": city["plaka"],
                "districts": city.get("ilceleri", [])
            }
    raise HTTPException(status_code=404, detail="Şehir bulunamadı!")

@app.get("/city/city_districts_by_id/{id}")
def city_name_to_districts(id: int):
    for city in cities:
        if city["plaka"] == id:
            return {
                "name": city["il"],
                "id": id,
                "districts": city.get("ilceleri", [])
            }
    raise HTTPException(status_code=404, detail="Şehir bulunamadı!")
