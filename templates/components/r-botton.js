$('.show-desc').click(function () {
    $(this).addClass('hidden');
    $(this).next().removeClass('hidden')
})
$('.show-all').click(function () {
    $(this).addClass('hidden');
    $(this).prev().removeClass('hidden')
})