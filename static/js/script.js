$(document).ready(function () {
    $('.navbar-toggler').on('click', function () {
        $('#sidebar').toggleClass('active');
        $('#content').toggleClass('active');
    });
});

function submitData() {
    let data = {
        "Hostname": document.getElementById('Hostname').value,
        "ManagementIP": document.getElementById('ManagementIP').value,
        "Netmask": document.getElementById('Netmask').value,
        "DefaultGateway": document.getElementById('DefaultGateway').value,
        "EnablePassword": document.getElementById('EnablePassword').value,
        "SecretPassword": document.getElementById('SecretPassword').value,      
    };

    // サーバーエンドポイントにJSONデータを送信します。
    fetch(window.location.href + 'submit', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
    .then(response => response.json())
    .then(data => {
        // サーバーから得られた結果に基づいて新しいページに遷移します。
        window.location.href = window.location.href + 'results/' + data.result_id;
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}

