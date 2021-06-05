var editor = ace.edit("editor");
editor.setTheme("ace/theme/monokai");
editor.session.setMode("ace/mode/javascript");


function capitalize(s)
{
    return s && s[0].toUpperCase() + s.slice(1);
}

function langaugeSelector(language){
    console.log(language);
    $("#dropdownMenu2 span").text(capitalize(language));
    if(language ==='cpp'){
        language = "c_cpp";
    }
    editor.session.setMode("ace/mode/"+language)
}

function toggleCustomInput(){
    //document.getElementById("#output-container").scrollIntoView();
    let current = $("#custom-input").css("display");
    if(current == "none"){
        $("#custom-input").css("display","");
        $('.custom-input-text:input:visible').first().focus()


    }else{
        $("#custom-input").css("display","none");
    }
}