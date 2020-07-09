window.addEventListener('DOMContentLoaded', (event) => {
    document.querySelectorAll('.registeration').forEach(function(item){
        item.oninput = function(){
            checkentry();
        }
    })
    document.querySelectorAll('.loginFild').forEach(function(item){
        item.oninput = function() {
            checkentryLogin();
        }
    })

    let register = document.querySelector("#register");
    register.addEventListener('click', function () {
        document.querySelector('#loginForm').style.display = 'none';
        document.querySelector('#loginText').style.display = 'none';
        document.querySelector('#registerForm').style.display = 'flex';
        document.querySelector('#registerText').style.display = 'flex';
    });
    let loginbtn = document.querySelector('#loginbtn');
    loginbtn.addEventListener('click', function () {
        document.querySelector('#loginForm').style.display = 'flex';
        document.querySelector('#loginText').style.display = 'flex';
        document.querySelector('#registerForm').style.display = 'none';
        document.querySelector('#registerText').style.display = 'none';
    });
});

function checkentry() {
    if (/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(document.querySelector('#email').value)) {
        if (document.querySelector('#first_name').value != '') {
            if (document.querySelector('#last_name').value != '') {
                if (document.querySelector('#user_name').value != '') {
                    if (document.querySelector('#email').value != '') {
                        if (document.querySelector('#password_register').value != '') {
                                document.querySelector('#submit_register').disabled = false;
                                return;
                        }
                    }

                }
            }
        }
    }
    document.querySelector('#submit_register').disabled = true;
};

function checkentryLogin(){
    if(document.querySelector('#password').value != '' && document.querySelector('#username').value != ''){
        document.querySelector('#submit_login').disabled = false;
    }
    else{
        document.querySelector('#submit_login').disabled = true;
    }
}