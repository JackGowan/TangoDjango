$(document).ready(function() {
	$("#about-btn").click( function(event) {
		alert("You clicked the button using JQuery!");
	});
	
	$("#about-btn").click( function(event) {
msgstr = $("#msg").html()
msgstr = msgstr + "ooo"
$("#msg").html(msgstr)
$("#about-btn").removeClass('btn-primary').addClass('btn-success');
});


	
});


