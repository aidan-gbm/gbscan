$(document).ready(function() {
    $('button#runCmd').click(function() {
        opts = { cmd: $('#cmd').val() }

        $.ajax({
            type: 'POST',
            url: '/api/cmd',
            dataType: 'json',
            contentType: 'application/json; charset=utf-8',
            data: JSON.stringify({ cmd: $('#cmd').val() })
        })

        .done(function(data) {
            $('#cmdWindow').text(data.ret)
        })

        .fail(function() {
            alert('Command failed.')
        })
    })
})