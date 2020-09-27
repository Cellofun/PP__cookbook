$(document).ready(function () {
    let value_block = $('td[id*="block-"]');

    let generalize = function () {
        value_block.each(function () {
            $(this).find('.form-control').addClass('d-none');
            $(this).children().show();
        });
    }

    $('span[id*="init-"]').each(function () {
        $(this).html($(this).html().replace(/\.0$/,''));
    });

    fractorize();

    $(document).click(function() {
        generalize();
    });

    value_block
        .click(function (e) {
            generalize();

            $(this).children().hide();
            $(this).find('.form-control').removeClass('d-none').show();

            e.stopPropagation();
        })
        .on('keypress',function(e) {
            if (e.which === 13) {
                let input = $(this).find('input[id*="new-"]').val();
                let value = $(this).find('input[id*="anchor-"]').val();
                let pivot = input / value;

                $('span[id*="init-"]').each(function() {
                    let that = $(this);

                    setTimeout(function() {
                        let calculated = (Math.round( (that.siblings('input[id*="value-"]').val() * pivot) * 1000 ) / 1000 );
                        let measure = that.siblings('input[id*="measure-"]').val();

                        if (measure === 'gr' || measure === 'ml') {
                            that.siblings('input[id*="new-"]').val(Math.round(calculated));
                            that.hide().html(Math.round(calculated)).fadeIn(500);
                        } else if (measure === 'kg' || measure === 'l') {
                            that.siblings('input[id*="new-"]').val(Math.round( calculated * 100 ) / 100);
                            that.hide().html(Math.round( calculated * 100 ) / 100).fadeIn(500);
                        } else {
                            that.siblings('input[id*="new-"]').val(calculated);
                            that.hide().html(calculated).fadeIn(500);
                        }

                        fractorize();
                        }, 250)
                });

                generalize();
            }
        });
});