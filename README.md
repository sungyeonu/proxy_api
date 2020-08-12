# Proxy
This Flask project serves as the backend for Proxy, a full-stack COVID tracking web application. 

## Set Up
1. In the backend root directory, clone the project using 
```
git clone https://github.com/sungyeonu/proxy_api.git
```

2. Set up a virtual environment
```
python -m venv venv
```

3. Activate the virtual environment
- Windows: `venv\Scripts\activate`
- Linux/Mac: `source venv/bin/activate`

4. Install required packages
```
pip install -r requirements.txt
```

## Usage
To run:
```
python app.py
```

## Endpoints
/api_get - returns all locations
/api_post - adds to locations. Takes in a json and requires 'name', 'time', and 'location'. 
