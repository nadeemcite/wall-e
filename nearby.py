import requests

#now 2 tasks

# 1 change the whole program to Object oriented style
# e.g. a = GoogleMapPlaces("Chittorgarh", "1500", "Pizza", "") should create object
# a.getNearByAddress() should give result


# 2 Get your own API Key from google cloud console
# open terminal arey baba yaha pr
class GoogleMapPlaces:
    API_KEY = "AIzaSyDZMs9AfgNI0fcvENgUK6pM6lS3wbptcbE"

    def __init__(self, address, radius, type, keyword):
        self.address = address
        self.radius = radius
        self.type = type
        self.keyword = keyword


    def addressToCoordinates(self):
        url = "https://maps.googleapis.com/maps/api/geocode/json"

        querystring = {"address":self.address,"key":self.API_KEY}


        response = requests.request("GET", url, params=querystring)

        # check if response is 'ok' then return result
        if response.json()["status"]=="OK":
            return response.json()["results"][0]["geometry"]["location"]
        else:
            print(response.text)
            return { "error": "Not found"}

    def getNearBy(self):
        location = self.addressToCoordinates()
        x= location["lat"]
        y= location["lng"]
        loc=str(x)+","+str(y)
        url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"

        querystring = {"location":loc,"radius":self.radius,"type":self.type,"keyword":self.keyword,"key":self.API_KEY}

        response = requests.request("GET", url, params=querystring)
        print(response.text)
        return response.json()

    def getNearByAddress(self):
        r = self.getNearBy()
        for x in r["results"]:
            print(x["name"]+" "+x.get("vicinity", ""))

a = GoogleMapPlaces("Chittorgarh", "1500", "restaurant", "pizza")
a.getNearByAddress()
