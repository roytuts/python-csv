from xml.etree.ElementTree import XML

input_xml = """<policies>
	<policy>
		<policyId>119736</policyId>
		<statecode>FL</statecode>
		<eq_site_limit>CLAY COUNTY</eq_site_limit>
		<hu_site_limit>498960</hu_site_limit>
		<fl_site_limit>498960</fl_site_limit>
		<fr_site_limit>498960</fr_site_limit>
		<tiv_2011>498960</tiv_2011>
		<tiv_2012>498960</tiv_2012>
		<eq_site_deductible>792148.9</eq_site_deductible>
		<hu_site_deductible>0</hu_site_deductible>
		<fl_site_deductible>9979.2</fl_site_deductible>
		<fr_site_deductible>0</fr_site_deductible>
		<point_latitude>0</point_latitude>
		<point_longitude>30.102261</point_longitude>
		<line>-81.711777</line>
		<construction>Residential</construction>
		<point_granularity>Masonry</point_granularity>
	</policy>
	<policy>
		<policyId>448094</policyId>
		<statecode>FL</statecode>
		<eq_site_limit>CLAY COUNTY</eq_site_limit>
		<hu_site_limit>1322376.3</hu_site_limit>
		<fl_site_limit>1322376.3</fl_site_limit>
		<fr_site_limit>1322376.3</fr_site_limit>
		<tiv_2011>1322376.3</tiv_2011>
		<tiv_2012>1322376.3</tiv_2012>
		<eq_site_deductible>1438163.57</eq_site_deductible>
		<hu_site_deductible>0</hu_site_deductible>
		<fl_site_deductible>0</fl_site_deductible>
		<fr_site_deductible>0</fr_site_deductible>
		<point_latitude>0</point_latitude>
		<point_longitude>30.063936</point_longitude>
		<line>-81.707664</line>
		<construction>Residential</construction>
		<point_granularity>Masonry</point_granularity>
	</policy>
	<policy>
		<policyId>206893</policyId>
		<statecode>FL</statecode>
		<eq_site_limit>CLAY COUNTY</eq_site_limit>
		<hu_site_limit>190724.4</hu_site_limit>
		<fl_site_limit>190724.4</fl_site_limit>
		<fr_site_limit>190724.4</fr_site_limit>
		<tiv_2011>190724.4</tiv_2011>
		<tiv_2012>190724.4</tiv_2012>
		<eq_site_deductible>192476.78</eq_site_deductible>
		<hu_site_deductible>0</hu_site_deductible>
		<fl_site_deductible>0</fl_site_deductible>
		<fr_site_deductible>0</fr_site_deductible>
		<point_latitude>0</point_latitude>
		<point_longitude>30.089579</point_longitude>
		<line>-81.700455</line>
		<construction>Residential</construction>
		<point_granularity>Wood</point_granularity>
	</policy>
	<policy>
		<policyId>333743</policyId>
		<statecode>FL</statecode>
		<eq_site_limit>CLAY COUNTY</eq_site_limit>
		<hu_site_limit>0</hu_site_limit>
		<fl_site_limit>79520.76</fl_site_limit>
		<fr_site_limit>0</fr_site_limit>
		<tiv_2011>0</tiv_2011>
		<tiv_2012>79520.76</tiv_2012>
		<eq_site_deductible>86854.48</eq_site_deductible>
		<hu_site_deductible>0</hu_site_deductible>
		<fl_site_deductible>0</fl_site_deductible>
		<fr_site_deductible>0</fr_site_deductible>
		<point_latitude>0</point_latitude>
		<point_longitude>30.063236</point_longitude>
		<line>-81.707703</line>
		<construction>Residential</construction>
		<point_granularity>Wood</point_granularity>
	</policy>
	<policy>
		<policyId>172534</policyId>
		<statecode>FL</statecode>
		<eq_site_limit>CLAY COUNTY</eq_site_limit>
		<hu_site_limit>0</hu_site_limit>
		<fl_site_limit>254281.5</fl_site_limit>
		<fr_site_limit>0</fr_site_limit>
		<tiv_2011>254281.5</tiv_2011>
		<tiv_2012>254281.5</tiv_2012>
		<eq_site_deductible>246144.49</eq_site_deductible>
		<hu_site_deductible>0</hu_site_deductible>
		<fl_site_deductible>0</fl_site_deductible>
		<fr_site_deductible>0</fr_site_deductible>
		<point_latitude>0</point_latitude>
		<point_longitude>30.060614</point_longitude>
		<line>-81.702675</line>
		<construction>Residential</construction>
		<point_granularity>Wood</point_granularity>
	</policy>
	<policy>
		<policyId>785275</policyId>
		<statecode>FL</statecode>
		<eq_site_limit>CLAY COUNTY</eq_site_limit>
		<hu_site_limit>0</hu_site_limit>
		<fl_site_limit>515035.62</fl_site_limit>
		<fr_site_limit>0</fr_site_limit>
		<tiv_2011>0</tiv_2011>
		<tiv_2012>515035.62</tiv_2012>
		<eq_site_deductible>884419.17</eq_site_deductible>
		<hu_site_deductible>0</hu_site_deductible>
		<fl_site_deductible>0</fl_site_deductible>
		<fr_site_deductible>0</fr_site_deductible>
		<point_latitude>0</point_latitude>
		<point_longitude>30.063236</point_longitude>
		<line>-81.707703</line>
		<construction>Residential</construction>
		<point_granularity>Masonry</point_granularity>
	</policy>
	<policy>
		<policyId>995932</policyId>
		<statecode>FL</statecode>
		<eq_site_limit>CLAY COUNTY</eq_site_limit>
		<hu_site_limit>0</hu_site_limit>
		<fl_site_limit>19260000</fl_site_limit>
		<fr_site_limit>0</fr_site_limit>
		<tiv_2011>0</tiv_2011>
		<tiv_2012>19260000</tiv_2012>
		<eq_site_deductible>20610000</eq_site_deductible>
		<hu_site_deductible>0</hu_site_deductible>
		<fl_site_deductible>0</fl_site_deductible>
		<fr_site_deductible>0</fr_site_deductible>
		<point_latitude>0</point_latitude>
		<point_longitude>30.102226</point_longitude>
		<line>-81.713882</line>
		<construction>Commercial</construction>
		<point_granularity>Reinforced Concrete</point_granularity>
	</policy>
	<policy>
		<policyId>223488</policyId>
		<statecode>FL</statecode>
		<eq_site_limit>CLAY COUNTY</eq_site_limit>
		<hu_site_limit>328500</hu_site_limit>
		<fl_site_limit>328500</fl_site_limit>
		<fr_site_limit>328500</fr_site_limit>
		<tiv_2011>328500</tiv_2011>
		<tiv_2012>328500</tiv_2012>
		<eq_site_deductible>348374.25</eq_site_deductible>
		<hu_site_deductible>0</hu_site_deductible>
		<fl_site_deductible>16425</fl_site_deductible>
		<fr_site_deductible>0</fr_site_deductible>
		<point_latitude>0</point_latitude>
		<point_longitude>30.102217</point_longitude>
		<line>-81.707146</line>
		<construction>Residential</construction>
		<point_granularity>Wood</point_granularity>
	</policy>
	<policy>
		<policyId>433512</policyId>
		<statecode>FL</statecode>
		<eq_site_limit>CLAY COUNTY</eq_site_limit>
		<hu_site_limit>315000</hu_site_limit>
		<fl_site_limit>315000</fl_site_limit>
		<fr_site_limit>315000</fr_site_limit>
		<tiv_2011>315000</tiv_2011>
		<tiv_2012>315000</tiv_2012>
		<eq_site_deductible>265821.57</eq_site_deductible>
		<hu_site_deductible>0</hu_site_deductible>
		<fl_site_deductible>15750</fl_site_deductible>
		<fr_site_deductible>0</fr_site_deductible>
		<point_latitude>0</point_latitude>
		<point_longitude>30.118774</point_longitude>
		<line>-81.704613</line>
		<construction>Residential</construction>
		<point_granularity>Wood</point_granularity>
	</policy>
</policies>"""

parsed = XML(input_xml)

#print (parsed)

data = []

for policy in parsed:
	policyId = policy.find('policyId').text
	statecode = policy.find('statecode').text
	eq_site_limit = policy.find('eq_site_limit').text
	hu_site_limit = policy.find('hu_site_limit').text
	fl_site_limit = policy.find('fl_site_limit').text
	fr_site_limit = policy.find('fr_site_limit').text
	tiv_2011 = policy.find('tiv_2011').text
	tiv_2012 = policy.find('tiv_2012').text
	eq_site_deductible = policy.find('eq_site_deductible').text
	hu_site_deductible = policy.find('hu_site_deductible').text
	fl_site_deductible = policy.find('fl_site_deductible').text
	fr_site_deductible = policy.find('fr_site_deductible').text
	point_latitude = policy.find('point_latitude').text
	point_longitude = policy.find('point_longitude').text
	line = policy.find('line').text
	construction = policy.find('construction').text
	point_granularity = policy.find('point_granularity').text

	#print('{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}'.format(policyId, statecode, eq_site_limit, hu_site_limit, fl_site_limit, fr_site_limit, tiv_2011, tiv_2012, eq_site_deductible, hu_site_deductible, fl_site_deductible, fr_site_deductible, point_latitude, point_longitude, line, construction, point_granularity))
	
	data.append('{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}'.format(policyId, statecode, eq_site_limit, hu_site_limit, fl_site_limit, fr_site_limit, tiv_2011, tiv_2012, eq_site_deductible, hu_site_deductible, fl_site_deductible, fr_site_deductible, point_latitude, point_longitude, line, construction, point_granularity))

#print (data)

with open('output-string.csv', 'w') as f: f.write('\n'.join([row for row in data[1:]]))