<?php

function convertXmlToCsvString($xmlString) {
	$xml = simplexml_load_string($xmlString);
	
	$header = false;
	
	$csv = '';
	
	foreach($xml as $key => $value){
		if(!$header) {
			//$csv .= implode(array_keys(get_object_vars($value)), ',');
			$csv .= implode(',', array_keys(get_object_vars($value)));
			$header = true;
		}
		
		$csv .= nl2br("\n");
		//$csv .= implode(get_object_vars($value), ',');
		$csv .= implode(',', get_object_vars($value));
	}
	
	return $csv;
}

$xml_string = '<?xml version="1.0"?><policies><policy><policyID>119736</policyID><statecode>FL</statecode><county>CLAY COUNTY</county><eq_site_limit>498960</eq_site_limit><hu_site_limit>498960</hu_site_limit><fl_site_limit>498960</fl_site_limit><fr_site_limit>498960</fr_site_limit><tiv_2011>498960</tiv_2011><tiv_2012>792148.9</tiv_2012><eq_site_deductible>0</eq_site_deductible><hu_site_deductible>9979.2</hu_site_deductible><fl_site_deductible>0</fl_site_deductible><fr_site_deductible>0</fr_site_deductible><point_latitude>30.102261</point_latitude><point_longitude>-81.711777</point_longitude><line>Residential</line><construction>Masonry</construction><point_granularity>1</point_granularity></policy><policy><policyID>448094</policyID><statecode>FL</statecode><county>CLAY COUNTY</county><eq_site_limit>1322376.3</eq_site_limit><hu_site_limit>1322376.3</hu_site_limit><fl_site_limit>1322376.3</fl_site_limit><fr_site_limit>1322376.3</fr_site_limit><tiv_2011>1322376.3</tiv_2011><tiv_2012>1438163.57</tiv_2012><eq_site_deductible>0</eq_site_deductible><hu_site_deductible>0</hu_site_deductible><fl_site_deductible>0</fl_site_deductible><fr_site_deductible>0</fr_site_deductible><point_latitude>30.063936</point_latitude><point_longitude>-81.707664</point_longitude><line>Residential</line><construction>Masonry</construction><point_granularity>3</point_granularity></policy><policy><policyID>206893</policyID><statecode>FL</statecode><county>CLAY COUNTY</county><eq_site_limit>190724.4</eq_site_limit><hu_site_limit>190724.4</hu_site_limit><fl_site_limit>190724.4</fl_site_limit><fr_site_limit>190724.4</fr_site_limit><tiv_2011>190724.4</tiv_2011><tiv_2012>192476.78</tiv_2012><eq_site_deductible>0</eq_site_deductible><hu_site_deductible>0</hu_site_deductible><fl_site_deductible>0</fl_site_deductible><fr_site_deductible>0</fr_site_deductible><point_latitude>30.089579</point_latitude><point_longitude>-81.700455</point_longitude><line>Residential</line><construction>Wood</construction><point_granularity>1</point_granularity></policy><policy><policyID>333743</policyID><statecode>FL</statecode><county>CLAY COUNTY</county><eq_site_limit>0</eq_site_limit><hu_site_limit>79520.76</hu_site_limit><fl_site_limit>0</fl_site_limit><fr_site_limit>0</fr_site_limit><tiv_2011>79520.76</tiv_2011><tiv_2012>86854.48</tiv_2012><eq_site_deductible>0</eq_site_deductible><hu_site_deductible>0</hu_site_deductible><fl_site_deductible>0</fl_site_deductible><fr_site_deductible>0</fr_site_deductible><point_latitude>30.063236</point_latitude><point_longitude>-81.707703</point_longitude><line>Residential</line><construction>Wood</construction><point_granularity>3</point_granularity></policy></policies>';

//$csv = convertXmlToCsvString($xml_string);
//echo $csv;

//Convert File
function convertXmlToCsvFile($xml_file_input, $csv_file_output) {
	$xml = simplexml_load_file($xml_file_input);
	
	$output_file = fopen($csv_file_output, 'w');
	
	$header = false;
	
	foreach($xml as $key => $value){
		if(!$header) {
			fputcsv($output_file, array_keys(get_object_vars($value)));
			$header = true;
		}
		fputcsv($output_file, get_object_vars($value));
	}
	
	fclose($output_file);
}

convertXmlToCsvFile("FL_insurance.xml", "FL_insurance.csv");