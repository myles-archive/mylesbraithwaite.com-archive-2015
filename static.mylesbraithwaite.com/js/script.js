$(document).ready(function() {
	$("section").fitVids();
	$('.form-comment').scrollToFixed({marginTop: 60});
});

$(document).delegate('*[data-toggle="lightbox"]', 'click', function(event) {
	event.preventDefault();
	$(this).ekkoLightbox();
});