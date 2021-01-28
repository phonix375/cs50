function close_all() {
    document.querySelector("#edit").style.display = "none";
    document.querySelector("#Contracts").style.display = "none";
    document.querySelector("#Generate").style.display = "none";
};

function edit_contract(contract_id) {
    var req = new XMLHttpRequest()
    req.onreadystatechange = function () {
        if (req.readyState == 4) {
            if (req.status != 200) {
                alert('request cannot be complited')
            }
            else {
                close_all()
                var response = JSON.parse(req.responseText)
                document.querySelector('#edit').style.display = "block"
                tinyMCE.get('mytextarea').setContent(response.body);
                document.querySelector('#Edit_title').value = response.title;
                document.querySelector('#edit_btn').setAttribute("onclick","edit_existing_contract("+response.id+")")
            }
        }
    }

    req.open('POST', '/get_contract')
    const data = new FormData();
    data.append('id',contract_id)
    req.send(data)

    return false
};
function show_contract(contract_id) {
    window.open("/show_contract" + "?" + "id=" + contract_id);
};

function save_contract() {
    var req = new XMLHttpRequest()
    req.onreadystatechange = function () {
        if (req.readyState == 4) {
            if (req.status != 200) {
                alert('request cud not be complited')
            }
            else {
                location.reload();
            }
        }
    }

    req.open('POST', '/contract_save')
    const data = new FormData();
    data.append('form',tinymce.get("mytextarea").getContent())
    data.append('title',document.querySelector('#Edit_title').value)

    //send request
    req.send(data);


    return false;
};

function delete_contract(contract_id) {
    var req = new XMLHttpRequest()
    req.onreadystatechange = function () {
        if (req.readyState == 4) {
            if (req.status != 200) {
                alert('request cud not be complited')
            }
            else {
                location.reload();
            }
        }
    }

    req.open('POST', '/delete_contract')
    req.setRequestHeader("Content-type", "application/x-www-form-urlencoded")

    var postVars = 'id=' + contract_id;
    req.send(postVars)

    return false
}
function edit_existing_contract(contract_id) {
    var req = new XMLHttpRequest()
    req.onreadystatechange = function () {
        if (req.readyState == 4) {
            if (req.status != 200) {
                alert('request cud not be complited')
            }
            else {
                location.reload();
            }
        }
    }

    req.open('POST', '/edit_existing_contract')
    req.setRequestHeader("Content-type", "application/x-www-form-urlencoded")

    var postVars = 'form=' + tinymce.get("mytextarea").getContent() + '&' + 'title=' + document.querySelector('#Edit_title').value + '&' + 'id=' + contract_id;
    req.send(postVars)



    return false
}
function genarate_link(){
    selected_contracts = [];
    document.querySelectorAll('.Contract_select_generate_link').forEach(seclection =>{
        if(seclection.checked){
            selected_contracts.push(seclection.value);
        };
    });
    var re = /\S+@\S+\.\S+/;
    if(re.test(document.querySelector('#send_to_email').value) && selected_contracts.length > 0){
        var req = new XMLHttpRequest()
        req.onreadystatechange = function () {
            if (req.readyState == 4) {
                if (req.status != 200) {
                    alert('request cannot be complited');
                }
                else {
                    close_all()
                    var response = req.responseText;
                    alert(response);
                    location.reload();
                }
            }
        }
    }
    else{
        alert('please enter a valid email address')
        return false;
    }


    req.open('POST', '/generate_link')
    const data = new FormData();
    data.append('contracts',selected_contracts)
    data.append('email',document.querySelector('#send_to_email').value)

    //send request
    req.send(data);


    return false;


}

window.addEventListener('DOMContentLoaded', (event) => {
    tinymce.init({
        selector: '#mytextarea'
    });
    close_all();
    document.querySelector("#Contracts").style.display = "block";
    document.querySelector('#My_Contract').onclick = function () {
    document.querySelector('#Contracts').style.display = "block";

    };
    document.querySelector('#Add_Contract').onclick = function () {
        close_all();
        document.querySelector('#edit').style.display = "block";
        tinyMCE.get('mytextarea').setContent('');
        document.querySelector('#Edit_title').placeholder = '';

    };
    document.querySelector('#Genarate_Link').onclick = function () {
        close_all();
        document.querySelector('#Generate').style.display = "block";

    };
    document.querySelector('#save').onclick = function () {
        var myContent = tinymce.get("mytextarea").getContent();
        if (document.querySelector('#Edit_title').value == '') {
            alert('Please type a title')
        }
        else {
            save_contract();
        };

    }
    document.querySelector('#My_Contract').onclick = function () {
        close_all();
        document.querySelector('#Contracts').style.display = 'block';
    }

});