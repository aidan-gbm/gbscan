function addTarget(ip, success, fail) {
    $.ajax({
        type: 'POST',
        url: '/api/tester/target/add',
        dataType: 'json',
        contentType: 'application/json; charset=utf-8',
        data: JSON.stringify({ ip: ip }),
    }).done(success).fail(fail)
}

function delTarget(id, success, fail) {
    $.get('/api/tester/target/del/' + id)
    .done(success)
    .fail(fail)
}

function getTargets(success, fail) {
    $.getJSON('/api/tester/target')
    .done(success)
    .fail(fail)
}

function updateTargets() {
    $('#targets').empty()
    getTargets(function(data) {
        data.forEach(tgt => {
            $('#targets').append(`<option value="${tgt.id}">${tgt.ip}</option>`)
        })
    }, function() { alert('Error communicating with the backend.') })
}

$(document).ready(function() {
    updateTargets()

    $('button#new-target').click(function() {
        var ip = $('input#new-target').val()
        addTarget(ip, function(data) {
            if (data.success) {
                updateTargets()
            } else { alert('Invalid IP Address') }
        }, function() { alert('Error communicating with the backend.') })
    })

    $('button#del-target').click(function() {
        var id = $('select#targets').val()
        delTarget(id, function(data) {
            if (data.success) {
                updateTargets()
            } else { alert('Invalid IP Address') }
        }, function() { alert('Error communicating with the backend.') })
    })
})