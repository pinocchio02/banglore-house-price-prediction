# Bangalore House Price Prediction
-This project uses a Machine Learning model to predict house prices in Bangalore based on various factors. It includes a Flask API for serving predictions and is deployed on AWS.

* Table of Contents :
1) Project Overview

2) Tech Stack

3) How to Run Locally

4) Deployment on AWS

5) API Endpoints

6) Contributing

# Project Overview :
This project predicts house prices in Bangalore using a trained ML model. It provides a simple frontend and a REST API backend for predictions.

# Tech Stack :
Backend: Flask, Python

Frontend: HTML, CSS, JavaScript

ML Model: Scikit-learn, Pandas, NumPy

Deployment: AWS EC2, Nginx, Gunicorn

# How to Run Locally :
  
Prerequisites -

1) Install Python (3.x).
2) Install required libraries:
pip install -r requirements.txt (In bash)

Running the Flask Server - 

3) Navigate to the server directory: 
cd BHP/Server (bash)

4) Run the Flask server: 
python3 server.py (bash)

5) Access the API at: 
http://127.0.0.1:5000(cpp)

- you can use postman for seding API requests using this link

Running the Frontend -

6) Navigate to the client folder:  
cd BHP/Client (bash)

7) Run it using:
start app.html

# Deployment on AWS :
  
1) Launch an EC2 Instance

    Use Ubuntu 20.04 or Amazon Linux.

    Allow inbound rules for ports 22, 80, 5000.

2) Transfer Files to the Instance

    scp -i BHP.pem -r BHP ubuntu@ec2-3-146-221-191.us-east-2.compute.amazonaws.com (bash)

3) Setup and Start Flask

    cd BHP/Server
    python3 server.py
  
4) Configure Nginx

  Edit /etc/nginx/sites-available/BHP.conf:

nginx server: 
    
    {

    listen 80;
    
    server_name ec2-3-146-221-191.us-east-2.compute.amazonaws.com;

    root /home/ubuntu/BHP/Client;
    index app.html;

    location / {
        try_files $uri $uri/ /app.html;
    }

    location /api/ {
        rewrite ^/api(.*) $1 break;
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }  # <-- Closing brace for location /api/ block
    }  # <-- Closing brace for server block   

Enable Nginx:

sudo ln -s /etc/nginx/sites-available/BHP.conf /etc/nginx/sites-enabled/ (bash)
sudo systemctl restart nginx (bash)

Access Your Website

http://ec2-3-146-221-191.us-east-2.compute.amazonaws.com/

# API Endpoints :

1) Method	Endpoint	Description

GET	- /get_location_names	Returns a list of available locations,
POST	- /predict_home_price	Predicts house price based on input parameters

Sample Request (POST)
(Postman)
{ 
    "location": "Indira Nagar",
    "sqft": 1500,
    "bhk": 3,
    "bath": 2
}

Sample Response
{
    "estimated_price": 125.5
}

# Contributing :

Contributions are welcome! Feel free to open issues or submit pull requests.
