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