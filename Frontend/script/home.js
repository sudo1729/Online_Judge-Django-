var editor = ace.edit("editor");
editor.setTheme("ace/theme/dracula");
editor.session.setMode("ace/mode/javascript");

var languageInput = $('input[name="language"]');

function capitalize(s)
{
    return s && s[0].toUpperCase() + s.slice(1);
}

function langaugeSelector(language){
    languageInput.val(capitalize(language))
    //console.log(languageInput.val());
    $("#dropdownMenu2 span").text(capitalize(language));
    if(language ==='c++'){
        language = "c_cpp";
    }
    editor.session.setMode("ace/mode/"+language)
}

function questionSelector(question){
    $('input[name="question]').val(question);
    $("#dropdownMenu1 span").text(question);
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

editor.setOptions({
    enableBasicAutocompletion: true,
    enableSnippets: true,
    enableLiveAutocompletion: true
});


var input = $('input[name="code"]');

editor.getSession().on("change", function () {
    input.val(editor.getSession().getValue());
});