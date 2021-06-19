function renderRegister() {
    $(".login-container").css("display", "none");
    $(".register-container").css("display", "");
}

function loginHandler() {
    let userName = $('#loginUName').val();
    let password = $('#loginPassword').val()
    const xhr = new XMLHttpRequest();   
    xhr.open('GET',"http://127.0.0.1:8000/login/"+userName+','+password);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.getResponseHeader("Content-Type", "application/json");


    xhr.onload = function(){
        const response = JSON.parse(this.response);
        console.log(response.detail);
        if(response.detail == 'Not found.'){
            alert("user name or password incorrect");
        }else{
            alert("success");
        }
    }
    xhr.send();
}


function registerHandler(){
    let email = $('#registerEmail').val();
    let userName = $('#registerUName').val();
    let password = $('#registerPassword').val();

    const xhr = new XMLHttpRequest();
    xhr.open('POST',"http://127.0.0.1:8000/login",true);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.getResponseHeader("Content-Type", "application/json");


    xhr.onload = function(){
        const response = JSON.parse(this.response);
        console.log(response);
        if(response.detail == 'Successfully created'){
            alert("user registered succesfully");
            $(".login-container").css("display", "");
            $(".register-container").css("display", "none");
        }else if(response.detail == 'Already Registered'){
            alert("User already registered");
            $(".login-container").css("display", "");
            $(".register-container").css("display", "none");
        }else{
            alert(response);
        }
    }
    const params = JSON.stringify({
        'email':email,
        'userName':userName,
        'password':password
    });
    xhr.send(params);


}