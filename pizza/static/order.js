document.addEventListener('DOMContentLoaded', () => { 
    
    document.querySelector('#conform').onclick = function() {
        sendOrder();
        localStorage.removeItem('myOrder');
        document.querySelector('#myOrderList').innerHTML = '';
        document.querySelector('#myOrder').style.display = 'none';
        document.querySelector('#numberOfItems').innerHTML = 0;
        document.querySelector('#numberOfItems1').innerHTML = 0;


    };
    
    
    let cl = document.querySelectorAll('.close');
    cl.forEach(function(item){
        item.onclick = function() {
            this.parentElement.style.display = 'none'
        };
    });
    
    document.querySelector('#registerBtn').onclick = function() {
        closeAllPopups();
        document.querySelector('#register').style.display = 'block';
        return false;
    }

    document.querySelector('#OpenRegister').onclick = function() {
        closeAllPopups();
        document.querySelector('#register').style.display = 'block';
        return false
    };

    document.querySelector('#OpenRegister1').onclick = function() {
        closeAllPopups();
        document.querySelector('#register').style.display = 'block';
        return false
    };
    
    
    document.querySelector('#closetest').onclick = function() {
        this.parentElement.style.display = 'none';
        document.querySelector('#itemName').innerHTML = '';
        document.querySelector('#toppingsList').innerHTML = '';
        document.querySelector('#option').innerHTML = '';
    };

    const mi = document.querySelectorAll('.plus');
    mi.forEach(bt => {
        bt.onclick = function () {
            popup(bt, bt.dataset.user, bt.dataset.id);
        };
    });

    document.querySelector('#login').onclick = () => {
        document.querySelector('#loginForm').style.display = 'block';
        return false;
    };

    document.querySelector('#login1').onclick = () => {
        document.querySelector('#loginForm').style.display = 'block';
        return false;
    };

    document.querySelector('#openLogin').onclick = function () {
        document.querySelector('#PleaseLogin').style.display = 'none';
        document.querySelector('#loginForm').style.display = 'block';
        return false;
    };
    document.querySelector('#openLogin1').onclick = function () {
        document.querySelector('#PleaseLogin').style.display = 'none';
        document.querySelector('#loginForm').style.display = 'block';
        return false;
    };

    

    document.querySelectorAll('.close').forEach(function(value) {
        value.addEventListener('click', function(){
            this.parentElement.style.display = 'none';
        });
    });

});

function popup(bt, user, itemId) {
    if (user == 'none'){
        let forms = document.querySelectorAll('.form-popup');
        forms.forEach(function(item){
            item.style.display = 'none'
        });
        document.querySelector('#PleaseLogin').style.display = 'block';
    }
    else {
        let form = document.querySelector('#addToOrder');
        let title = document.querySelector('#itemName');
        title.innerHTML = bt.dataset.name;
        requestTopings(bt.dataset.id);
        form.style.display = 'block';
        

    };
};

function closePopup() {
    document.querySelector('.form-popup').innerHTML = '';
    document.querySelector('.form-popup').style.display = 'none';   
};

function callBack() {
    topingsOption.forEach(function(item){
        let li = document.createElement('li');
        let y = document.createElement('input');
        let label = document.createElement('label');
        label.setAttribute('for',item);
        label.innerHTML = item;
        y,id = item;
        y.setAttribute('type','checkbox');
        y.setAttribute('class','topings1');
        y.onchange = priceCalculate;
        y.innerHTML = item;
        li.appendChild(y);
        li.appendChild(label);
        document.querySelector('#toppingsList').appendChild(li);

    });
    if(largePrice != 0) {
        let form = document.querySelector('#option')
        let select = document.createElement('select');
        select.id = 'itemOptions';
        let option1 = document.createElement('option');
        option1.setAttribute('value', itemPrice);
        option1.innerHTML = 'Small ' + itemPrice;
        option1.setAttribute('data-option','small');
        let option2 = document.createElement('option');
        option2.setAttribute('value', largePrice);
        option2.innerHTML = 'Large ' + largePrice;
        option2.setAttribute('data-option','large');
        select.appendChild(option1);
        select.appendChild(option2);
        form.appendChild(select);
        select.onchange = priceCalculate;
        priceCalculate();

    };
    if(largePrice == 0) {
        let form = document.querySelector('#option')
        let select = document.createElement('select');
        select.id = 'itemOptions';
        let option1 = document.createElement('option');
        option1.setAttribute('value', itemPrice);
        option1.innerHTML = 'regular ' + itemPrice;
        option1.setAttribute('data-option','small');
        select.appendChild(option1);
        form.appendChild(select);
        select.onchange = priceCalculate;
        priceCalculate();

    };

};


function requestTopings(itemId) {
    var csrftoken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;
    var parameter = 'itemId=' + itemId;
    request = new XMLHttpRequest();
    request.open('POST','gettopings'+'?' + parameter,true);
    request.setRequestHeader('X-CSRFToken', csrftoken);
    request.responseType = 'json';
    request.send();
    request.onload = function() {
        topingsOption = request.response.data;
        itemPrice = request.response.price;
        largePrice = request.response.large;
        callBack();
    };
};


function priceCalculate() {
    let numOfTopings = 0
    let price = 0;
    let base = parseFloat(document.querySelector('#itemOptions').value);
    topings = document.querySelectorAll('.topings1')
    let select = document.querySelector('#itemOptions');
    topings.forEach(function(item){
        if(item.checked) {
            numOfTopings+=1;
        };
    });
    if(numOfTopings == 1){
        if(select.options[select.selectedIndex].dataset.option == 'small'){
        price += 1;
        }
        else {
            price += 2;
        };
    };
    if(numOfTopings == 2){
        if(select.options[select.selectedIndex].dataset.option == 'small'){
            price += 2.5;
        }
        else {
            price += numOfTopings * 2;
        }
    };
    if(numOfTopings == 3){
        if(select.options[select.selectedIndex].dataset.option == 'small'){
            price += 3.5;
        }
        else {
            price += numOfTopings *2;
        };
    
    };
    if(numOfTopings > 3){
        if(select.options[select.selectedIndex].dataset.option == 'small'){
            price += 5.05;
        }
        else {
            price += 8;
        }
    
    };
    price += base;
    let btn = document.createElement('button');
    btn.innerHTML = 'add to my order';
    document.querySelector('#product_price').innerHTML = '';
    document.querySelector('#product_price').innerHTML += price;

};

function addToOrder() {
    let price = document.querySelector('#product_price').innerHTML;
    let item = document.querySelector('#itemName').innerHTML;
    let topings = document.querySelector('#toppingsList').getElementsByClassName('topings1');
    let topingsCheked = [];
    if(document.body.contains(document.querySelector('#itemOptions')) == true){
        console.log('going into true')
        var option = document.querySelector('#itemOptions').options[document.querySelector('#itemOptions').selectedIndex].dataset.option;
    }
    else {
        console.log('going into else')
        var option = 'regular'
    };
    
    for(var i=0; i < topings.length; i++) {
        if(topings[i].checked){
            topingsCheked.push(topings[i].nextElementSibling.innerHTML);
        };
    };
    if (localStorage.getItem('myOrder') != null) {
        
        let myOrder = JSON.parse(localStorage.getItem('myOrder'));
        myOrder.push({'item':item,'topings':topingsCheked,'price':price, 'size':option})
        localStorage.setItem('myOrder',JSON.stringify(myOrder));
    }
    else{
        localStorage.removeItem('myOrder');
        localStorage.setItem('myOrder', JSON.stringify([{'item':item,'topings':topingsCheked,'price':price, 'size':option}]));
    };
    document.querySelector('#addToOrder').style.display = 'none';
    document.querySelector('#itemName').innerHTML = '';
    document.querySelector('#option').innerHTML = '';
    document.querySelector('#toppingsList').innerHTML = '';
    document.querySelector('#addedToOrder').style.display = 'block';
    let orderItems = JSON.parse(localStorage.getItem('myOrder'));
    document.querySelector('#numberOfItems').innerHTML = orderItems.length;
    document.querySelector('#numberOfItems1').innerHTML = orderItems.length;

};


function myorder() {
    let orderItems = JSON.parse(localStorage.getItem('myOrder'));
    document.querySelector('#myOrderList').innerHTML ='';
    let totalPrice = 0;
    if(orderItems.length != 0){
        
    for(let i=0; i<orderItems.length;i++){

        let itemOrder = document.createElement('div');

        let divHeader = document.createElement('p');
        divHeader.innerHTML = orderItems[i].item + '-' + orderItems[i].size;
        totalPrice += parseFloat(orderItems[i].price);
        itemOrder.appendChild(divHeader);


        let ditals = document.createElement('p');
        ditals.innerHTML = orderItems[i].topings + ' price: ' + orderItems[i].price;
        itemOrder.appendChild(ditals);
        let btn = document.createElement('button');
        btn.innerHTML = 'X';
        btn.setAttribute('onclick',`deleteItem(${i})`);
        itemOrder.appendChild(btn);
        let hr = document.createElement('hr');
        document.querySelector('#myOrderList').appendChild(itemOrder);
        document.querySelector('#myOrderList').appendChild(hr);
        
    };
};
    let total = document.createElement('p');
    total.innerHTML = 'Total Order Price : ' + totalPrice;
    document.querySelector('#myOrderList').appendChild(total);

    document.querySelector('#myOrder').style.display = 'block';

};

function myorders() {
    var csrftoken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;
    document.querySelector('#myOrders').innerHTML = '';
    let order = localStorage.getItem('myOrder');
    request = new XMLHttpRequest();
    request.open('GET','myorders',true);
    request.setRequestHeader('X-CSRFToken', csrftoken);
    request.responseType = 'json';
    request.send();
    request.onload = function() {
        let myOrder = request.response
        //console.log(myOrder)
        let orderIds = Object.keys(myOrder.orders)
        for(i = 0; i < orderIds.length; i++){
            //console.log(myOrder.orders[orderIds[i]]['items'][0]['topings']);

            let header = document.createElement('h3');
            header.innerHTML = 'order number: ' + orderIds[i] + '<br> Status:' + myOrder.orders[orderIds[i]]['status'];
            //console.log('this is the header : ' + header.innerHTML);
            document.querySelector('#myOrders').appendChild(header);
            for(let x = 0; x <  myOrder.orders[orderIds[i]]['items'].length;x++ )  {
                let itemName = myOrder.orders[orderIds[i]]['items'][x].name;
                let itemSize = myOrder.orders[orderIds[i]]['items'][x].size
                let p = document.createElement('p');
                p.innerHTML = 'item : ' + itemName + ', size: ' + itemSize + ' <br>topings: ';
                if(myOrder.orders[orderIds[i]]['items'][x]['topings'].length == 0) {
                    p.innerHTML += 'no topings'
                }
                else {
                for( y in myOrder.orders[orderIds[i]]['items'][x]['topings']){
                    p.innerHTML += myOrder.orders[orderIds[i]]['items'][x]['topings'][y] + ','
                };
            };
                p.innerHTML +='<hr>'
                document.querySelector('#myOrders').appendChild(p);
            };

        };
        document.querySelector('#myOrdersForm').style.display = 'block';
    };
    return false;
}

function deleteItem(i){
    console.log('deliting item ' + i);
    let orderItems = JSON.parse(localStorage.getItem('myOrder'));
    orderItems.splice(i,1);
    console.log(orderItems);
    localStorage.setItem('myOrder',JSON.stringify(orderItems));
    myorder();
    document.querySelector('#numberOfItems').innerHTML = orderItems.length;
    document.querySelector('#numberOfItems1').innerHTML = orderItems.length;
};


function closeAllPopups() {
    let popups = document.querySelectorAll('.form-popup');
    popups.forEach(function(item){
        item.style.display = 'none';
    });
    return false;
};


function sendOrder() {
    var csrftoken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;
    let order = localStorage.getItem('myOrder');
    var parameter = 'order=' + order;
    request = new XMLHttpRequest();
    request.open('POST','order'+'?' + parameter,true);
    request.setRequestHeader('X-CSRFToken', csrftoken);
    request.send();
    request.onload = function() {
        console.log('send :' + request.response)
    };
};