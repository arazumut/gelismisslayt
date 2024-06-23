import requests

def get_location(ip_address):
    # ipstack API anahtar�n�z� buraya ekleyin
    api_key = 'AP� anahtar�n�z� girmelisiniz'
    url = f'http://api.ipstack.com/{ip_address}?access_key={api_key}'

    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        return {
            'IP': data.get('ip'),
            'Country': data.get('country_name'),
            'Region': data.get('region_name'),
            'City': data.get('city'),
            'Latitude': data.get('latitude'),
            'Longitude': data.get('longitude')
        }
    else:
        return {'Error': data.get('error', {}).get('info', 'An error occurred')}

# Kullan�c�dan IP adresi al�n�r
ip_address = input("L�tfen konumunu ��renmek istedi�iniz IP adresini girin: ")
location = get_location(ip_address)

if 'Error' in location:
    print(f"Bir hata olu�tu: {location['Error']}")
else:
    print(f"IP Adresi: {location['IP']}")
    print(f"�lke: {location['Country']}")
    print(f"B�lge: {location['Region']}")
    print(f"�ehir: {location['City']}")
    print(f"Enlem: {location['Latitude']}")
    print(f"Boylam: {location['Longitude']}")
