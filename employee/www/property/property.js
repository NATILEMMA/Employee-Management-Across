// Copyright (c) 2016, Anthony Emmanuel (@Ghorz) and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Property"] = {
	"filters": [
		{
			"fieldname": "property",
			"label": __("Property Name"),
			"fieldtype": "Data",
			"width": 100,
			"reqd": 0,
		},
		{
			"fieldname": "from",
			"label": __("From Date"),
			"fieldtype": "Date",
			"width": 80,
			"reqd": 1,
			"default":dateutil.year_start()
		},
		{
			"fieldname": "to",
			"label": __("To Date"),
			"fieldtype": "Date",
			"width": 80,
			"reqd": 1,
			"default":dateutil.year_end()
		},
		{
			"fieldname": "agent",
			"label": __("Agent Name"),
			"fieldtype": "Link",
			"options": "Agent",
			"width": 100,
			"reqd": 0,
		},
		{
			"fieldname": "status",
			"label": __("Status"),
			"fieldtype": "Select",
			"default": "",
			"options": ['', 'Sale', 'Rent', 'Lease'],
			"width": 100,
			"reqd": 0,
		}
	]
};

map: function(frm){
	console.log(JSON.parse(frm.doc.map));
	let mapdata= JSON.parse(cur_frm.doc.map).features[0];
	if(mapdata && mapdata.geometry.type =='Point'){
	  let lat=mapdata.geometry.coordinates[1];
	  let lon=mapdata.geometry.coordinates[0];
	  console.log(lat,lon);
	  // make an api call
	  frappe.call({
			 type:"GET",
			url:`https://nominatim.openstreetmap.org/reverse?format=json&lat= ${lat}& lon=${lon}`,
			 callback:function(){
				 // code snippet
				 console.log(r);
				   JSON.parse(cur_frm.doc.map).features[0];
			 }
			})
			
		}
	}