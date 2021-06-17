let editor = ace.edit("editor");
editor.setTheme("ace/theme/dracula");
let language = $('input[name="language"]');
let code = $('input[name="code"]');
let customInput = $('textarea[name="customInput"]');
let expectedOutput = $('textarea[name="expectedOutput"]');


function languageSelector(inputLanguage){
    language.val(inputLanguage);
    alert(language.val());
    alert(customInput.val());
}





editor.getSession().on("change", function () {
    code.val(editor.getSession().getValue());
});