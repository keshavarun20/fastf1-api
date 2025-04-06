# main.py
from fastapi import FastAPI
import fastf1

app = FastAPI()
fastf1.Cache.enable_cache('cache')  # Enables disk caching to avoid refetching

@app.get("/telemetry")
def get_telemetry(driver: str = "VER", year: int = 2023, gp: str = "Monza"):
    session = fastf1.get_session(year, gp, 'R')
    session.load()
    laps = session.laps.pick_driver(driver).pick_fastest()
    tel = laps.get_car_data().add_distance()

    return {
        "time": tel['Time'].astype(str).tolist(),
        "speed": tel['Speed'].tolist(),
        "distance": tel['Distance'].tolist()
    }
