
import requests

def get_location(ip_address):
  url = f"http://ipinfo.io/{ip_address}/json"
  response = requests.get(url)
  data = response.json()
  return data

if __name__ == "__main__":
  ip_address = input("Enter IP address: ")
  location_data = get_location(ip_address)
  print("Location Details:")
  
  print(f"IP Address: {location_data['ip']}")
  print(f"City :  {location_data['city']}")
  print(f"Region: {location_data['region']}")
  print(f"Country: {location_data['country']}")
  print(f"Location: {location_data['loc']}")
