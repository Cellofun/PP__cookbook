$(document).ready(function (){
    $('.django-ckeditor-widget').each(function (){
        $(this).css('width', '100%');
    });

    $('.djn-model-recipes-ingredient').each(function () {
        $(this).removeClass('btn-outline-success');
    });

    $('.djn-model-recipes-method').each(function () {
        $(this).removeClass('btn-outline-success');
    });
});