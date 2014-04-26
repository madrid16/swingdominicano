$(document).on('ready', function(){
	$('.img_play').on('click', function(){
		var secondary_src = $(this).parent().find('iframe').attr('src');
		var principal_src = $('#principal_video').find('iframe').attr('src');
		$(this).parent().find('iframe').attr('src', principal_src);
		$('#principal_video').find('iframe').attr('src', secondary_src);
	});

	var resize_principal_video = function(){
		$('#principal_video').find('iframe').attr({ 'width': 560, 'height': 315 })
	}

	var resize_secondary_video = function(){
		$('.video_content').each(function(){
			$(this).find('iframe').attr({ 'width': 300, 'height': 139 })
		});
	}

	if(!!$('#principal_video').length){
		resize_principal_video();
	}

	if(!!$('#video_list').length){
		resize_secondary_video();
	}
});