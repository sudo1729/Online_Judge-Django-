let editor = ace.edit("editor");
editor.setTheme("ace/theme/dracula");
editor.session.setMode("ace/mode/c_cpp");




var input = $('input[name="code"]');

editor.getSession().on("change", function () {
    input.val(editor.getSession().getValue());
});