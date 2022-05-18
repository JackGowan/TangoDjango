$(document).ready(function() {


$("strong").hover( function() {
$(this).css('color', 'red');
},
function() {
$(this).css('color', 'black');
});


$('#likes').click(function(){
var catid;
catid = $(this).attr("data-catid");
$.get('/rango/like/', {category_id: catid}, function(data){
$('#like_count').html(data);
$('#likes').hide();
});
});

$('#suggestion').keyup(function(){
	var query;
	query = $(this).val();
	$.get('/rango/suggest/', {suggestion: query}, function(data){
	$('#cats').html(data);
	});
});



});
