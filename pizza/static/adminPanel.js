document.addEventListener('DOMContentLoaded', () => { 
    var csrftoken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;
    request = new XMLHttpRequest();
    request.open('GET','getAllOrders',true);
    request.setRequestHeader('X-CSRFToken', csrftoken);
    request.responseType = 'json';
    request.send();
    request.onload = function() {
        let myOrder = request.response
        let orderIds = Object.keys(myOrder.orders)
        for(i = 0; i < orderIds.length; i++){

            let header = document.createElement('h3');
            header.innerHTML = 'order number: ' + orderIds[i] + '<br> Status:' + myOrder.orders[orderIds[i]]['status'] +' user :  '+ myOrder.orders[orderIds[i]]['user'];
            document.querySelector('#blat').appendChild(header);
            for(let x = 0; x <  myOrder.orders[orderIds[i]]['items'].length;x++ )  {
                let itemName = myOrder.orders[orderIds[i]]['items'][x].name;
                let itemSize = myOrder.orders[orderIds[i]]['items'][x].size
                let p = document.createElement('p');
                p.innerHTML = 'item : ' + itemName + ', size: ' + itemSize + ' topings: ';
                if(myOrder.orders[orderIds[i]]['items'][x]['topings'].length == 0) {
                    p.innerHTML += 'no topings'
                }
                else {
                for( y in myOrder.orders[orderIds[i]]['items'][x]['topings']){
                    p.innerHTML += myOrder.orders[orderIds[i]]['items'][x]['topings'][y] + ','
                };
            };
                p.innerHTML +='<hr>'
                document.querySelector('#blat').appendChild(p);
            };

        };
    };

    });