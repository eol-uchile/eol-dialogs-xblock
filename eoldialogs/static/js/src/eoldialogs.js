/*
        .-"-.
       /|6 6|\
      {/(_0_)\}
       _/ ^ \_
      (/ /^\ \)-'
       ""' '""
*/


function EolDialogsXBlock(runtime, element,settings) {
    $(function ($) {
        var dialogid = "dialog_" + settings.location;
		renderMathForSpecificElements(dialogid);
    });

    function renderMathForSpecificElements(id) {
        if (typeof MathJax !== "undefined") {
            var $dialog = $('#' + id);
            if ($dialog.length) {
                $dialog.find('.dialogo').each(function (index, diagelem) {
                    MathJax.Hub.Queue(["Typeset", MathJax.Hub, diagelem]);
                });
            }
        } else {
            console.warn("MathJax no está cargado.");
        }
    }
}
