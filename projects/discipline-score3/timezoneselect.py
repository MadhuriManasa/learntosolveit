import pytz
import re

country_timezones = {}
for (country, tzlist) in pytz.country_timezones.iteritems():
    country_name = pytz.country_names[country]
    cities = []
    for timezone in tzlist:
        # remove continent
        city = re.sub(r'^[^/]*/', r'', timezone)
        # Argentina has an extra "Argentina/" on my system (pytz 2010b)
        city = re.sub(country_name + '/', '', city)
        # Indiana and North Dakota have different rules by country
        # change Indiana/Location to Location, Indiana
        city = re.sub(r'^([^/]*)/(.*)', r'\2, \1', city)
        # change underscores to spaces
        city = re.sub(r'_', r' ', city)
        cities.append(city)
    country_timezones[country_name] = cities

for country in sorted(country_timezones):
    print country
    for city in sorted(country_timezones[country]):
        print "\t%s" % (city)
