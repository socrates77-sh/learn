import pygeoip


gi = pygeoip.GeoIP('GeoLiteCity.dat')


def printRecord(tgt):
    rec = gi.record_by_addr(tgt)
    # print(rec)
    city = rec['city']
    region = rec['region_code']
    country = rec['country_name']
    longi = rec['longitude']
    lat = rec['latitude']
    print('[*] Target: %s Geo-located' % tgt)
    print('[+] %s, %s, %s' % (city, region, country))
    print('[+] Latitude: %f, Longitude: %f' % (lat, longi))


tgt = '173.255.226.98'
tgt = '116.228.89.23'
tgt = '202.102.94.124'
printRecord(tgt)
