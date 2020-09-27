let fractions = function (rem1, rem2, html, _this) {
    let text = _this.siblings('input[id*="new-"]').val();

    if (text.indexOf('.') > -1) {
        let val = text.split('.');
        let quo;
        let rem;

        if (val[1].length === 1) {
            val[1] += '00';
        } else if (val[1].length === 2) {
            val[1] += '0';
        }

        quo = parseInt(val[0]);
        rem = parseInt(val[1]);

        if (rem > rem1 && rem <= rem2) {
            if (quo === 0) {
                _this.html(html)
            } else {
                _this.html(quo + html);
            }
        }
    }
};

let fractorize = function () {
    $('span[id*="init-"]').each(function () {
        let measure = $(this).siblings('input[id*="measure-"]').val();

        if (measure === 'cup' || measure === 'tbsp' || measure === 'tsp' || measure === 'pc') {
            fractions(0, 188, ' &frac18;', $(this));
            fractions(188, 290, ' &frac14;', $(this));
            fractions(290, 415, ' &frac13;', $(this));
            fractions(415, 585, ' &frac12;', $(this));
            fractions(585, 710, ' &frac23;', $(this));
            fractions(710, 875, ' &frac34;', $(this));
            fractions(875, 9999, 1, $(this));
        }
    });
};