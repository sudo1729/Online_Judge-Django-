//GET Request

// let fetchBtn = document.getElementById("fetchBtn");
// fetchBtn.addEventListener('click',buttonClickHandler);

// function buttonClickHandler(){
//     $.ajax({
//         url: "http://127.0.0.1:8000/compiler.json/",
//         type: 'GET',
//         dataType: 'json', // added data type
//         success: function(res) {
//             console.log(res);
//             alert(res);
//         }
//     });

// }


//POST Request
var input = $('input[name="code"]');
var language = $('input[name="language"]');

let runCode = document.getElementById("runCode");
runCode.addEventListener('click', runCodeClickHandler)

function runCodeClickHandler() {
    // console.log('Wait we are Posting data to server');
    // console.log(language.val());
    // console.log(input.val());
    //Instantiate an xhr object
    const xhr = new XMLHttpRequest();

    // USE THIS FOR POST REQUEST
    xhr.open('POST', 'http://127.0.0.1:8000/compiler/', true);
    xhr.setRequestHeader("Content-Type", "application/json");
    //xhr.getResponseHeader("Content-Type", "application/json");
    // What to do on progress (optional)
    // xhr.onprogress = function(){
    //     console.log('On progress');
    // }


    // What to do when response is ready
    xhr.onload = function () {
        //console.log(typeof this.response);
        const obj = JSON.parse(this.response);
        //console.log(obj);
        // console.log(obj.stdout);
        if(obj.stderr!=""){
            $('#output').val(obj.stderr);
        }else{
            $('#output').val(obj.stdout);
        }
        

        let outputContainer = $('#output-container');
        if(outputContainer.css("display") == "none"){
            outputContainer.css("display","");
            $('.output:input:visible').first().focus()
        }
    }

    // send the request
    let customInput = $('#custom-input-text');
    params = {code:input.val(),language:language.val(),questionInput:customInput.val()};
    xhr.send(JSON.stringify(params));


}