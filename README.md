# Weather Caching with Celery, Redis and OpenWeatherMap API

This project fetches the weather data (temperature) of a set of cities using the OpenWeatherMap API, caches the results in Redis for 60 seconds, and uses Celery to schedule periodic updates.

## 🔧 Technologies Used

- **Python 3**
- **Celery** – Task queue for asynchronous processing
- **Redis** – Used as both message broker and caching backend
- **Requests** – To fetch weather data from API
- **OpenWeatherMap API** – Weather data provider

---

## 🚀 How It Works

- When the Celery task runs, it checks Redis cache for the temperature of each city.
- If data exists and is not expired (within 60 seconds), it returns the cached value.
- Otherwise, it makes an API call to OpenWeatherMap, caches the new temperature, and returns it.

---

## ⏱ Periodic Task with Celery Beat

The task `fetch_weather_of_cities` runs every 60 seconds and fetches temperatures for a predefined list of cities.

---

## 🛠 How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/Nasim-Khalili/Weather-Caching-.git
cd Weather-Caching-
```

### 2. Create a virtual environment and install dependencies

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Start Redis server (if not already running)

```bash
sudo service redis-server start
```

### 4. Run Celery worker in one terminal

```bash
celery -A tasks worker --loglevel=info
```

### 5. Run Celery Beat scheduler in another terminal

```bash
celery -A tasks beat --loglevel=info
```

---

## 🌐 Add Your Own Cities

You can edit the list of cities in `tasks.py` to include cities you want:

```python
cities = ['tehran', 'rasht', 'astara', 'london', 'madrid', 'shiraz']
```

Make sure the city names are valid and supported by OpenWeatherMap.

---

## 🔑 API Key

Replace `"YOUR_API_KEY_HERE"` in `cache.py` with your actual [OpenWeatherMap API key](https://openweathermap.org/api).

---

## 🧊 Example Output (Redis cache entries)

```
temp_tehran: 32
temp_london: 21
...
```

### 👩‍💻 Contributing & Support

If you like this project or found it useful, feel free to:

- ⭐ Star this repository  
- 🍴 Fork it and customize it  
- 🐛 Report bugs or request features via Issues  

---

### 📬 Contact

Made with  by **Nasim Khalili**  
