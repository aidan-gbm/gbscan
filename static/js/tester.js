// ***** TARGETS *****

function addTarget(name, ip, success, fail) {
    $.ajax({
        type: 'POST',
        url: '/api/tester/target?name=' + name,
        dataType: 'json',
        contentType: 'application/json; charset=utf-8',
        data: JSON.stringify({ ip: ip }),
    }).done(success).fail(fail)
}

function delTarget(name, success, fail) {
    $.ajax({
        type: 'DELETE',
        url: '/api/tester/target?name=' + name,
    }).done(success).fail(fail)
}

function getTargets(name, success, fail) {
    var url = (name) ? '/api/tester/target?name=' + name : '/api/tester/target' 
    $.getJSON(url)
    .done(success)
    .fail(fail)
}

function updateTargets() {
    $('#targets').empty()
    getTargets(false, function(data) {
        if (Object.keys(data).length < 1) {
            $('#targets').append(`<option value selected disabled>-- add a target --</option>`)
        } else {
            for (name in data) {
                $('#targets').append(`<option value selected disabled>-- select a target --</option>`)
                $('#targets').append(`<option value="${name}">${name}</option>`)
            }
        }
    }, function() { alert('Error communicating with the backend.') })
}

// ***** ACTIONS *****
function nmap(type) {
    var tgt = $('#targets').val()
    if (typeof tgt !== 'undefined') {
        alert('Please select a target first.')
    } else if (type == 0) {
        $.ajax({
            type: 'POST',
            url: '/api/tester/actions/run',
            dataType: 'json',
            contentType: 'application/json; charset=utf-8',
            data: JSON.stringify({ cmd: `nmap -F -oX ^DIR^/nmap/quick.xml ${tgt}`})
        }).done(function() { alert('Complete')}).fail(function(){ alert('Error communicating with the backend.')})
    }
}

// ***** DOCUMENT READY *****

$(document).ready(function() {
    updateTargets()

    $('select#targets').change(function() {
        $('#del-target').prop('disabled', false)
        getTargets($('select#targets option:selected').val(), function(data) {
            $('#info').empty()
            $('#info').append(`<li>IP: ${data['ip']}</li>`)
        }, function() { alert('Error communicating with the backend.') })
    })

    $('button#new-target').click(function() {
        var ip = $('input#ip').val()
        var name = $('input#name').val()
        addTarget(name, ip, function(data) {
            if (data.success) {
                updateTargets()
            } else { alert('Invalid IP Address') }
        }, function() { alert('Error communicating with the backend.') })
    })

    $('button#del-target').click(function() {
        var name = $('#targets').val()
        delTarget(name, function(data) {
            if (data.success) {
                updateTargets()
            } else { alert('Invalid Target') }
        }, function() { alert('Error communicating with the backend.') })
    })
})