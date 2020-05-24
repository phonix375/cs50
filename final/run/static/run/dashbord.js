var date = new Date();
var locations = []
var distance = 0;
var hours = 0;
var minuts = 0;
var seconds = 0;
var startDate = '';
var startTime = '';
var endDate = '';
var endTime ='';
var templocations = {};

window.addEventListener('DOMContentLoaded', function (){

let start = document.querySelector('#start');


//click the start / stop button
start.addEventListener('click', function () {
          var start = new Date();
          startTime = start.getHours()+','+start.getMinutes()+','+start.getSeconds()
          startDate = start.getFullYear()+','+(start.getMonth()+1)+','+start.getDate()
          locations = []
          distance = 0;
          distance = 0;
          hours = 0;
          minuts = 0;
          seconds = 0;
          document.querySelector('#distanceSelect').disabled = true;
          let clock = document.querySelector('#timer')
          var myVar = setInterval(function () {
               var options = {
                    enableHighAccuracy: true,
                    timeout: 5000,
                    maximumAge: 0
                  };
               navigator.geolocation.getCurrentPosition(showPosition, if_error, options);
               if (distance * 1000 >= parseInt(document.querySelector('#distanceSelect').value)) {
                    clearInterval(myVar);
                    alert(`congratulations you finished ${document.querySelector('#distanceSelect').value} in ${clock.innerHTML}`);
                    var endT = new Date();
                    endTime = endT.getHours()+','+endT.getMinutes()+','+endT.getSeconds()
                    endDate = endT.getFullYear()+','+(endT.getMonth()+1)+','+endT.getDate()
                    finishrun();
               };
               seconds++;
               if (seconds == 60) {
                    minuts++;
                    seconds = 0;
               }
               if (minuts == 60) {
                    hours++;
                    minuts = 0;
               }
               displayMinuts = '';
               displayhours = '';
               displaySeconds = '';
               if (seconds <= 9) { displaySeconds = '0' + seconds } else { displaySeconds = seconds };
               if (minuts <= 9) { displayMinuts = '0' + minuts } else { displayMinuts = minuts };
               if (hours <= 9) { displayhours = '0' + hours } else { displayhours = hours };

               clock.innerHTML = `${displayhours}:${displayMinuts}:${displaySeconds}`;


          }, 1000);


          let end = document.querySelector('#stop')
          end.addEventListener('click', function () {
               document.querySelector('#distanceSelect').disabled = false;
               clearInterval(myVar);
               for (i = 0; i < locations.length - 1; i++) {
                    distance += distancecal(locations[i][0], locations[i][1], locations[i + 1][0], locations[i + 1][1], 'K')
               };
          }); // closing Click for end run
});


// clicking the new run on the side menu
document.querySelector('#new_run').addEventListener('click', function(){
          clocseAllContent();
          document.querySelector('#run').style.display = 'block';
});
  
// clicking the friends on the side menu
document.querySelector('#friendsbtn').addEventListener('click', function(){
     clocseAllContent();
     document.querySelector('#friendsBlock').style.display = 'block';
});

// click the dashbord on the side menu
document.querySelector('#dashbordbtn').addEventListener('click',function(){
     clocseAllContent();
     document.querySelector('#dashbord').style.display = 'block';
});

document.querySelectorAll('.friendbtn').forEach(function(item){
     item.addEventListener('click', function(){
          friendStat(this.innerHTML);
     });
});

document.querySelectorAll('.changeStatus').forEach(function(item){
     item.addEventListener('click', function(){
          document.querySelector('#statusChangeName').innerHTML = `change status for Frandship with ${this.dataset.whatever}`
          document.querySelector('#UserNameToChange').value = this.dataset.whatever
     });

});

document.querySelectorAll('.changeStatus1').forEach(function(item){
     item.addEventListener('click', function(){
          document.querySelector('#statusChangeName').innerHTML = `change status for Frandship with ${this.dataset.whatever}`
          document.querySelector('#UserNameToChange').value = this.dataset.whatever
     });

});
document.querySelectorAll('.changeStatus1').forEach(function(item){
     item.addEventListener('click', function(){
          document.querySelector('#statusChangeName1').innerHTML = `change status for Frandship with ${this.dataset.whatever}`
          document.querySelector('#UserNameToChange1').value = this.dataset.whatever
     });

});

document.querySelector('#showDistance').addEventListener("change", function(){
     drowChartAverageSpeed(this.value);
});

document.querySelector('#Averagebtn').addEventListener('click', function(){
     document.querySelector('#avrageSelector').style.display = 'block';
     drowChartAverageSpeed('All')
});

document.querySelector('#distancebtn').addEventListener('click', function(){
     document.querySelector('#avrageSelector').style.display = 'none';
     drowChartDistance('All')
});
document.querySelector("#sendFriendRequest").onsubmit = function(){
     // check if the request is valid :
     var xhttp = new XMLHttpRequest();
     xhttp.onreadystatechange = function () {
          if (this.readyState == 4 && this.status == 200) {
               let foo = JSON.parse(this.response)
               if(foo.status == '1'){
                   alert('No user with this email in the system')
               }
               if(foo.status == '2'){
                    alert('You alredy have an frend request with this user')
               }
               if(foo.status == '3'){
                    alert("You can't send friend request for yourself")
               }
               if(foo.status == 'good'){
                    sendFrendRequest();
               }
          }

     };
     var email = document.querySelector('#email').value;
     params = 'email=' + email;
     xhttp.open("GET", "FriendVerification" +'?'+ params, true);
     let csrftoken = document.querySelector('input[name="csrfmiddlewaretoken"]').value
     xhttp.setRequestHeader('X-CSRFToken', csrftoken);
     xhttp.send();
     
     
     
     
     return false;
};
document.querySelectorAll('.mapsbtn').forEach(function(item){
     item.addEventListener('click',function(){
          showmap(this.dataset.runid)
     })
});


var date_input = document.getElementById('date_input');
date_input.valueAsDate = new Date();

date_input.onchange = function(){
     drowChartDistance(filter=this.value)
}


}); // closing DOMContentLoaded





// __________________________________________ General Functions section _________________________________________

//closing all sections 
function clocseAllContent(){
     let content = document.querySelectorAll('.mainContent')
          content.forEach(function(item){
               item.style.display = 'none' 
     });
}


// __________________________________________ dashbord section _________________________________________________

function drowChartDistance(filter = null){
     alert(filter)
     var myRuns = window.myRuns;
     var dates = []
     var rundistance = []
     for (i in Object.keys(myRuns)) {
          dates.push(myRuns[i].start_time.slice(0, 10));
          rundistance.push(myRuns[i].distance)
     };
     var ctx = document.getElementById("myChart");
     var myChart = new Chart(ctx, {
          type: 'line',
          data: {
               labels: dates,
               datasets: [{
                    data: rundistance,
                    lineTension: 0,
                    backgroundColor: 'transparent',
                    borderColor: '#007bff',
                    borderWidth: 4,
                    pointBackgroundColor: '#007bff'
               }]
          },
          options: {
               scales: {
                    yAxes: [{
                         ticks: {
                              beginAtZero: false
                         }
                    }]
               },
               legend: {
                    display: false,
               }
          }
     });
}
function drowChartAverageSpeed(distance){
     var myRuns = window.myRuns;
     var dates = []
     var AavregeSpeed = []
     for (i in Object.keys(myRuns)) {
          if(myRuns[i].distance === distance+'.00' || distance == 'All'){
               dates.push(myRuns[i].start_time.slice(0, 10));
               AavregeSpeed.push(myRuns[i].everageSpeed)
          };
         
     };
     var ctx = document.getElementById("myChart");
     var myChart = new Chart(ctx, {
          type: 'line',
          data: {
               labels: dates,
               datasets: [{
                    data: AavregeSpeed,
                    lineTension: 0,
                    backgroundColor: 'transparent',
                    borderColor: '#007bff',
                    borderWidth: 4,
                    pointBackgroundColor: '#007bff'
               }]
          },
          options: {
               scales: {
                    yAxes: [{
                         ticks: {
                              beginAtZero: false
                         }
                    }]
               },
               legend: {
                    display: false,
               }
          }
     });
}

// ______________________________________________run section ___________________________________________________



// finish a run
function finishrun(){

     var xhttp = new XMLHttpRequest();
          xhttp.onreadystatechange = function () {
               if (this.readyState == 4 && this.status == 200) {
                    sendLocationPointes();
               }

          };
          params = `?run={"distance":${parseInt(document.querySelector('#distanceSelect').value)},"startTime":"${startTime}","startDate":"${startDate}","endTime":"${endTime}","endDate":"${endDate}"}`
          xhttp.open("GET", "finishrun" + params, true);
          let csrftoken = document.querySelector('input[name="csrfmiddlewaretoken"]').value
          xhttp.setRequestHeader('X-CSRFToken', csrftoken);
          xhttp.send();

};

/* calculate the distance */
function distancecal(lat1, lon1, lat2, lon2, unit) {
     if (lat1 == lat2 && lon1 == lon2) {
          return 0; 
     };
     var radlat1 = Math.PI * lat1 / 180;
     var radlat2 = Math.PI * lat2 / 180;
     var theta = lon1 - lon2;
     var radtheta = Math.PI * theta / 180;
     var dist = Math.sin(radlat1) * Math.sin(radlat2) + Math.cos(radlat1) * Math.cos(radlat2) * Math.cos(radtheta);
     if (dist > 1) {
          dist = 1;
     }
     dist = Math.acos(dist);
     dist = dist * 180 / Math.PI;
     dist = dist * 60 * 1.1515;
     if (unit == "K") { dist = dist * 1.609344 }
     if (unit == "N") { dist = dist * 0.8684 }
     if(dist *1000 > 12 ){
          return 0;
     }
     else{
          return dist;
     }
     
};

function showPosition(position) {
     if (locations.length === 0) {
          locations.push([position.coords.latitude, position.coords.longitude])
     }
     else {
          distance += distancecal(position.coords.latitude, position.coords.longitude, locations[locations.length - 1][0], locations[locations.length - 1][1], 'K')
          locations.push([position.coords.latitude, position.coords.longitude])
          document.querySelector('#distance').innerHTML = "distance now :" + distance
     };

};



// ______________________________________________Friends section _______________________________________________

function friendStat(fname){

     var xhttp = new XMLHttpRequest();
     xhttp.onreadystatechange = function () {
          if (this.readyState == 4 && this.status == 200) {
               let x = this.response
               var blat = JSON.parse(this.response)
               var myRuns = blat;
               var dates = []
               var rundistance = []
               for (i in Object.keys(myRuns)) {
                    dates.push(myRuns[i].start_time.slice(0, 10));
                    rundistance.push(myRuns[i].distance)
               };
               var ctx = document.getElementById("myChart1");
               ctx.style.display = 'block';
               var myChart = new Chart(ctx, {
                    type: 'line',
                    data: {
                         labels: dates,
                         datasets: [{
                              data: rundistance,
                              lineTension: 0,
                              backgroundColor: 'transparent',
                              borderColor: '#007bff',
                              borderWidth: 4,
                              pointBackgroundColor: '#007bff'
                         }]
                    },
                    options: {
                         scales: {
                              yAxes: [{
                                   ticks: {
                                        beginAtZero: false
                                   }
                              }]
                         },
                         legend: {
                              display: false,
                         }
                    }
               });

          };

     };
     params = `?user=${fname}`
     xhttp.open("GET", "GetFriendStat" + params, true);
     let csrftoken = document.querySelector('input[name="csrfmiddlewaretoken"]').value
     xhttp.setRequestHeader('X-CSRFToken', csrftoken);
     xhttp.send();

};

function sendFrendRequest(){
     var xhr = new XMLHttpRequest(),
     fd = new FormData();

     fd.append( 'email', document.querySelector('#email').value );
     fd.append('note', document.querySelector('#note').value )
     
     xhr.onreadystatechange = function () {
          if (this.readyState == 4 && this.status == 200) {
          };
     };
     xhr.open( 'POST', 'send_request', true );
     let csrftoken = document.querySelector('input[name="csrfmiddlewaretoken"]').value
     xhr.setRequestHeader('X-CSRFToken', csrftoken);
     
     xhr.send( fd );
}


function sendLocationPointes(){
     var xhr = new XMLHttpRequest(),
     fd = new FormData();
     fd.append('locations', locations )
     
     xhr.onreadystatechange = function () {
          };

     xhr.open( 'POST', 'sendLocationPointes', true );
     let csrftoken = document.querySelector('input[name="csrfmiddlewaretoken"]').value
     xhr.setRequestHeader('X-CSRFToken', csrftoken);
     
     xhr.send( fd );
};



function showmap(runid){
     var xhr = new XMLHttpRequest(),
     fd = new FormData();
     fd.append('runid', runid)
     
     xhr.onload = function(){
          if (xhr.status >= 200 && xhr.status < 300) {
               let foofoo = document.querySelector('#mapsscript');
               if(foofoo != null){
                    foofoo.remove()
               }
               var head= document.getElementsByTagName('head')[0];
               var script= document.createElement('script');
               script.type= 'text/javascript';
               script.setAttribute('id','mapsscript');
               templocations = JSON.parse(this.response)
               script.src= 'https://maps.googleapis.com/maps/api/js?key=AIzaSyAiZkAzv78fEialBf2ITaCyRIaH78zKhWU&callback=initMap';
               head.appendChild(script);
               console.log(templocations.locations)
               let x= [];
               for(i=0;i<templocations.locations.length;i = i+2){
                    x.push({lat: templocations.locations[i],lng: templocations.locations[i+1]})
               }
               templocations = x
               console.log(templocations)
          } else {
               // This will run when it's not
               console.log('The request failed!');
          }
     }
     xhr.open( 'POST', 'getlocations', true );
     let csrftoken = document.querySelector('input[name="csrfmiddlewaretoken"]').value
     xhr.setRequestHeader('X-CSRFToken', csrftoken);
     
     xhr.send( fd );

}

function initMap() {

     console.log(templocations.locations)
     var map = new google.maps.Map(document.getElementById('map'), {
       zoom: 16,
       center: templocations[0],
       mapTypeId: 'terrain'
     });
     
     var flightPlanCoordinates = templocations;
     var flightPath = new google.maps.Polyline({
       path: flightPlanCoordinates,
       geodesic: true,
       strokeColor: '#FF0000',
       strokeOpacity: 1.0,
       strokeWeight: 2
     });

     flightPath.setMap(map);
   }

function if_error(){
     console.log('tvau mat')
}