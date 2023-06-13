import requests

URL = "http://api.open-notify.org/iss-now.json"

def main():
    resp = requests.get(URL).json()

    print("CURRENT LOCATION OF ISS:")
    print("Lon:", resp["iss_position"]["longitude"])
    print("Lat:", resp["iss_position"]["latitude"])

if __name__ == "__main__":
    main()

