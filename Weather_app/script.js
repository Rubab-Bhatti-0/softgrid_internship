const apiKey = "1863cd8856bf4da1a68c39dd0d1dc441";
const apiUrl = "https://api.openweathermap.org/data/2.5/weather?units=metric&q=";

// Grab all elements using your exact IDs from HTML
const searchBtn = document.getElementById("searchBtn");
const cityInput = document.getElementById("city");
const cityName = document.getElementById("city_name");
const weatherIcon = document.getElementById("weather_icon");
const temperature = document.getElementById("temperature");
const weatherDescription = document.getElementById("weather_description");
const humidityPercent = document.getElementById("humidity_percent");
const windSpeedMph = document.getElementById("wind_speed_mph");
const weatherInfo = document.getElementById("weather_info");
const detailCol = document.getElementById("detail_col");
const errorMsg = document.getElementById("error_msg");

async function checkWeather(city) {
    try {
        const response = await fetch(apiUrl + city + "&appid=" + apiKey);

        // City not found
        if (response.status === 404) {
            errorMsg.style.display = "block";
            errorMsg.innerHTML = "City not found. Please try again.";
            weatherInfo.style.display = "none";
            detailCol.style.display = "none";
            return;
        }

        const data = await response.json();

        // Hide error, show weather sections
        errorMsg.style.display = "none";
        weatherInfo.style.display = "block";
        detailCol.style.display = "flex";

        // Fill in the data
        cityName.innerHTML = data.name + ", " + data.sys.country;
        temperature.innerHTML = Math.round(data.main.temp) + "°C";
        weatherDescription.innerHTML = data.weather[0].description;
        humidityPercent.innerHTML = data.main.humidity + "%";
        windSpeedMph.innerHTML = data.wind.speed + " km/h";

        // Change icon based on weather condition
        const condition = data.weather[0].main;

        if (condition === "Clear") {
            weatherIcon.src = "images/clear_hot.jpg";
        } else if (condition === "Clouds") {
            weatherIcon.src = "images/clouds.jpg";
        } else if (condition === "Rain") {
            weatherIcon.src = "images/rain.jpg";
        } else if (condition === "Drizzle") {
            weatherIcon.src = "images/drizzle.jpg";
        } else if (condition === "Snow") {
            weatherIcon.src = "images/snow.jpg";
        } else if (condition === "Mist" || condition === "Fog" || condition === "Haze") {
            weatherIcon.src = "images/mist.jpg";
        } else if (condition === "Thunderstorm") {
            weatherIcon.src = "images/thunderstorm.jpg";
        } else {
            weatherIcon.src = "images/clear_hot.jpg";
        }

    } catch (error) {
        errorMsg.style.display = "block";
        errorMsg.innerHTML = "Unable to connect. Check your internet.";
        weatherInfo.style.display = "none";
        detailCol.style.display = "none";
    }
}

// Search button click
searchBtn.addEventListener("click", () => {
    const city = cityInput.value.trim();

    if (city === "") {
        errorMsg.style.display = "block";
        errorMsg.innerHTML = "Please enter a city name.";
        weatherInfo.style.display = "none";
        detailCol.style.display = "none";
        return;
    }

    checkWeather(city);
});

// Enter key press
cityInput.addEventListener("keypress", (e) => {
    if (e.key === "Enter") {
        searchBtn.click();
    }
});