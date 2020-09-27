$(document).ready(function () {
    let cat_array = [];
    let cat_value;
    let cat_object = {};

    $('.card').each(function () {
        cat_value = $(this).attr('class').split(' ')[0];

        if (!cat_array.some(e => e.slug === cat_value)) {
            cat_object = {
                slug: cat_value,
                url: $(this).find('.url-hidden').val()
            }
            cat_array.push(cat_object);
        }
    });

    $.each(cat_array, function( key, value ) {
        let multiple = new Multiple({
            selector: '.' + value.slug,
            background: 'linear-gradient(45deg, rgba(255, 137, 233, 0.2) 0%, rgba(105, 147, 255, 0.2) 100%), url(' + value.url + ')'
        });
    });

    $('.recipe-link')
        .mouseover(function () {
            let url = cat_array.find(e => e.slug === $(this).find('.card-recipe').attr('class').split(' ')[0]).url;
            $(this).find('.card-recipe').css('background-image', 'url(' + url + ')');
        })
        .mouseout(function () {
            let url = cat_array.find(e => e.slug === $(this).find('.card-recipe').attr('class').split(' ')[0]).url;
            $(this).find('.card-recipe').css('background-image', 'linear-gradient(45deg, rgba(255, 137, 233, 0.2) 0%, rgba(105, 147, 255, 0.2) 100%), url(' + url + ')');
        });
});