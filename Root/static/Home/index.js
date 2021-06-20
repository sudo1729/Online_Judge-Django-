let editor = ace.edit("editor");
editor.setTheme("ace/theme/dracula");
let language = $('input[name="language"]');
let code = $('input[name="code"]');
let customInput = $('#customInput');
let expectedOutput = $('#expectedOutput');

function loginContainerToggle(){
    window.location.href="../Login/login.html";
}

function languageSelector(inputLanguage){
    language.val(inputLanguage);
    editor.getSession().setMode("ace/mode/"+inputLanguage);
    $('#onScreenLanguage').text(inputLanguage)
}




editor.getSession().on("change", function () {
    code.val(editor.getSession().getValue());
});