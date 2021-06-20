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


function runcode(){
    const xhr = new XMLHttpRequest();

    // USE THIS FOR POST REQUEST
    xhr.open('POST', 'http://127.0.0.1:8000/ide/snippets/', true);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.onprogress = function(){
        console.log('On progress');
    }


    // What to do when response is ready
    xhr.onload = function () {
        const obj = JSON.parse(this.response);
        console.log(obj);
        async function setlocation(){
            if(slug == ""){
                window.location.href="http://127.0.0.1:8000/ide/"+obj.slug;
            }
            return;
        }
        async function updatepage(){
            await setlocation();
            code.val(obj.code);
            language.val(obj.language);
            customInput.val(obj.customInput);
            expectedOutput.val(obj.expectedOutput);
        };
        updatepage();
        
        
    }
    
    params = {
        slug:slug,
        code:code.val(),
        language:language.val(),
        customInput:customInput.val(),
        expectedOutput:expectedOutput.val()
    };
    xhr.send(JSON.stringify(params));

}