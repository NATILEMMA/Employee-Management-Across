

const dates = {};
attendace_data= {{ attendace_data }};


for(var i =0;i< attendace_data.length;i++ ){

    if(attendace_data[i][0] == "Present"){
      dates[attendace_data[i][1]] = 4;
       }
    else if (attendace_data[i][0] == "Absent") {
      dates[attendace_data[i][1]] = 2;
    } 
    else if (attendace_data[i][0] == "Work From Home"){
      dates[attendace_data[i][1]] = 3;
    }
    else {
      dates[attendace_data[i][1]] = 1;
    }
}

const getTimestamp = (date) =>
  Math.round(new Date(date).getTime() / 1000).toString();
  

// Dates in normal format (mm-dd-yyyy)

const timestamp = new Date().getTime();
const today = new Date(timestamp);
let today1 = today.toLocaleDateString('en-US');




const toDataPointsV2 = (dates) => {
  const normalDates = Object.keys(dates);
  let dataPoints = {};
  normalDates.forEach((item) => {
    const timeStamp = getTimestamp(item);
    dataPoints[timeStamp] = dates[item];
  });

  return dataPoints;
};

let data = {
  dataPoints: toDataPointsV2(dates),
  start: new Date("01-01-2022"), // a JS date object
  end: new Date(today.toLocaleString('sv'))
};

new Chart("#chart", {
  type: "heatmap",
  data,
  colors: ['#FFFFFF','#FFFFFF', '#ff0000', '#FFFF00', '#00FF00'],
});




