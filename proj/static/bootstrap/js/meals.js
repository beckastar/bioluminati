

$('.color').draggable({
    revert: true
});

$('.grey').droppable({
    drop: function(event, ui) {
        var $drag = $(ui.draggable),
            $drop = $(this);

        $('#r').html($drag.text() + " onto " + $drop.text());
    },
    tolerance: 'touch'
});