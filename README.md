# API-INTEGRATION-AND-DATA-VISUALIZATION

*COMPANY*: CODTECH IT SOLUTIONS 

*NAME*: DINESH

*INTERN ID*: CT04DH1263

*DOMAIN*: PYTHON

*DURATION*: 4 WEEKS

*MENTOR*: NEELA SANTHOSH 

# TASK DESCRPITION

This project focuses on building a weather data visualization dashboard using Python. The goal was to collect live weather data from multiple cities across the world, process that data, and represent it in a visual format that makes interpretation easy and intuitive. This type of application is useful for monitoring real-time environmental conditions and can be extended for use in various fields such as urban planning, agriculture, logistics, and education.

The task began with identifying a reliable source for weather data. OpenWeatherMap, a public API provider, was chosen for this purpose. After registering on the platform, an API key was generated, which acts as a secure way to access real-time data. This key was later integrated into the Python script to make requests to the API for specific city weather data.

Once the API was ready, Python was used as the core development language. A list of cities (including London, New York, Tokyo, Chennai, Berlin, and Paris) was selected for demonstration. Using Python's requests library, the script made HTTP GET calls to the OpenWeatherMap API, requesting weather data for each city. The response from the API came in JSON format, which included details like temperature, humidity, pressure, and other weather conditions. For this dashboard, temperature and humidity were chosen as the main parameters to visualize.

The next step was to process and clean the data. The script extracted the required temperature and humidity values from the JSON responses and stored them in Python lists. These values were then used for creating visualizations. Libraries like matplotlib and seaborn were employed for plotting. These tools made it possible to represent the data in bar charts and scatter plots with clear labels, color gradients, and a clean layout.

The dashboard includes three types of plots:

A bar chart showing the temperature of each city.

A bar chart for humidity levels by city.

A scatter plot mapping the relationship between temperature and humidity across cities.

Each plot helps to quickly understand which cities are hotter, which ones are more humid, and how those two factors relate. This type of visual comparison is especially helpful when monitoring multiple locations at once.

The project also involved resolving a few technical challenges. One such issue was related to how Seaborn handles color palettes without hue values. A warning message indicated a deprecation in future versions, which required a small code tweak to ensure compatibility going forward. Also, validating the API key and understanding how the OpenWeatherMap response structure works was a key part of the learning process.

In terms of real-world applications, this type of weather dashboard can be used in:

Smart city monitoring systems to keep track of environmental conditions

Agriculture, where weather patterns significantly impact irrigation and crop planning

Logistics and transportation for better route planning in adverse weather

Education to help students understand how to work with APIs, process data, and visualize results

Home automation or personal weather stations that trigger alerts based on real-time data

This hands-on project brought together several essential elements — API integration, data parsing, real-time data analysis, and data visualization. It showcases the power of Python and how a few libraries can be combined to build something meaningful and visually insightful. The script is lightweight, runs efficiently, and can be further extended to include more weather variables or longer-term forecasts.

Overall, this task provided practical exposure to working with APIs and visualizing live data, making it a solid foundation for larger data science or IoT-based weather monitoring applications.

# OUTPUT

<img width="1920" height="938" alt="Image" src="https://github.com/user-attachments/assets/674e7d31-ad57-4f3d-85f5-fa376421d36b" />

