from fastapi import FastAPI, Query
import swisseph as swe

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Swiss Ephemeris API is running"}

@app.get("/planet-position/")
def get_planet_position(
    julian_day: float = Query(2451545.0, description="Julian day"),
    planet: str = Query("SUN", description="Planet name (e.g., SUN, MOON, etc.)")
):
    try:
        planet_id = getattr(swe, planet.upper(), None)
        if not planet_id:
            return {"error": f"Invalid planet name: {planet}"}
        
        position, ret_flag = swe.calc(julian_day, planet_id)
        return {"planet": planet, "position": position}
    except Exception as e:
        return {"error": str(e)}
