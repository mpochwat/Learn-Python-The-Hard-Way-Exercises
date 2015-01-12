# mapping of province to abbreviation
provinces = {
	"Ontario": "ON",
	"British Columbia": "BC",
	"Quebec":"QC"
	}
	
# mapping of province to capitalize
cities = {
	"ON": "Toronto",
	"QC": "Montreal",
	"NS": "Halifax"
	}
	
# add more cities
cities["BC"] = "Vancouver"

# print out some cities
print '-' * 10
print "ON has cities: %s" % cities["ON"]
print "BC has cities: %s" % cities["BC"] 

# print some provinces
print '-' * 10
print "Quebec's abbreviation is: %s" % provinces["Quebec"]

# using all in one
print '-' * 10
print "Ontario has cities: %s" % cities[provinces["Ontario"]]

# print every province abbreviation
print '-' * 10
for province, abbrev in provinces.items():
	print "%s is the province and %s abbrev" % (province, abbrev)
	
# print every city in province
print '-' * 10
for province, city in cities.items():
	print "%s province has capital %s" % (province, city)
	
print cities.keys()
print cities.items()
print sorted(cities)
print cities.keys()

