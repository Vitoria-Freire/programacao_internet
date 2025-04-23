function criar() {
    console.log('ola mundo')
    var linhas = parseInt(document.getElementById('linha').value);
    var colunas = parseInt(document.getElementById('coluna').value);

    var table = document.createElement('table');
    table.border = 1;

    for (var i = 0; i < linhas; i++) {
        var tr = document.createElement('tr');

        for (var j = 0; j < colunas; j++) {
            var td = document.createElement('td');
            td.textContent = `texto`;
            tr.appendChild(td);
        }
        table.appendChild(tr);
    }

    document.body.appendChild(table);
}

function apagar() {
    console.log('tchau mundo');

    var table = document.querySelectorAll('table')
    table.remove()
}