import simplejson, urllib

orig_coord = (orig)
dest_coord = (dest)


for orig in orig_coord:
	for dest in dest_coord:
		url = "http://maps.googleapis.com/maps/api/distancematrix/json?origins={0}&destinations={1}&mode=driving&language=en-EN&sensor=false".format(str(orig_coord),str(dest_coord))
		result= simplejson.load(urllib.urlopen(url))
		print(result)
		#driving_time = result['rows'][0]['elements'][0]['duration']['value']
		print(orig)
		print(dest)
		#print( driving_time/60.0/60.0)


