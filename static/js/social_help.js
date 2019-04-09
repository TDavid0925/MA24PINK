$(document).ready(function(){
    $('#submit_btn').on('click', function(){
        var location = $('#searchInput').val();
        addSearchResult(location);
    })
})

function addSearchResult(location){
    console.log(location)
    var hospitals = getHospitals(location);
    var emergency_services = getEmerServ(location);
    var charities = getCharities(location);

    //addHospitals(hospitals);
    //addEmergency_services(emergency_services);
    //addCharities(charities);
}

function addHospitals(hospitals){
    hospitals.forEach(function(hospital){
        addHospitals();
    });
}

function addHospital(hospital){
    var newHospital = $();
}

function getHospitals(location){
    var geturl = '/api/hospitals/' + location;
    var hospitals = []
    $.getJSON(geturl).then(function(hospitallist){
       hospitallist.forEach(function(data){
            hospitals.push(data);
            console.log(data);
        })
    })
    return hospitals
}

function getCharities(location){
    var geturl = '/api/charities/' + location;
    var charities = [];
    $.getJSON(geturl).then(function(charitiesList){
        charitiesList.forEach(function(data){
             charities.push(data);
             console.log(data);
         })
     })
    return charities;
}

function getEmerServ(location){
    var geturl = '/api/emergencies/' + location;
    var emer_servs = [];
    $.getJSON(geturl).then(function(emergencyList){
        emergencyList.forEach(function(data){
            emer_servs.push(data);
            console.log(data);
         })
     })
    return emer_servs;
}



var suburb = ["caulfield", "caulfield east", "caufield north", "caulfield jucnction", "carnegie", "elsternwick", "glen huntly", "murrumbeena", "ormond", "ormond east"]