
function getslug(){
    let url = window.location.href;
    let n = url.length;
    let slug = "";
    for(var i = n-1;i>=0;i--){
        if(url[i] == '/'){
            break;
        }else{
            slug=url[i]+slug;
        }
    }
    return slug;
}
slug = getslug();


// function runcode(){
//     const xhr = new XMLHttpRequest();

//     // USE THIS FOR POST REQUEST
//     xhr.open('POST', 'http://127.0.0.1:8000/compiler/', true);
//     xhr.setRequestHeader("Content-Type", "application/json");
//     //xhr.getResponseHeader("Content-Type", "application/json");
//     // What to do on progress (optional)
//     // xhr.onprogress = function(){
//     //     console.log('On progress');
//     // }


//     // What to do when response is ready
//     xhr.onload = function () {
//         //console.log(typeof this.response);
//         const obj = JSON.parse(this.response);
//         //console.log(obj);
//         // console.log(obj.stdout);
//         if(obj.stderr!=""){
//             $('#output').val(obj.stderr);
//         }else{
//             $('#output').val(obj.stdout);
//         }
        

//         let outputContainer = $('#output-container');
//         if(outputContainer.css("display") == "none"){
//             outputContainer.css("display","");
//             $('.output:input:visible').first().focus()
//         }
//     }

//     // send the request
//     let customInput = $('#custom-input-text');
//     params = {code:input.val(),language:language.val(),questionInput:customInput.val()};
//     xhr.send(JSON.stringify(params));

// }