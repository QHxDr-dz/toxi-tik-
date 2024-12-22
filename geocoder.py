import pygeocoder
from pygeocoder import Geocoder

if __name__=='__main__':
    adress=input("enter your location")
    print(pygeocoder.geocoder(adress)[0].coordinates)



