function runCmd(cmd, success, fail) {
    return $.ajax({
        type: 'POST',
        url: '/api/cmd',
        dataType: 'json',
        contentType: 'application/json; charset=utf-8',
        data: JSON.stringify({ cmd: cmd }),
    }).done(success).fail(fail)
}