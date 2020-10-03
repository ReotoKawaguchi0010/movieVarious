var getJson = function () {
    var workspace = document.getElementById('workspace');
    var url = '/model' + location.pathname.replace('/workspace', '');
    var request = new XMLHttpRequest();
    request.open('GET', url, true);
    request.setRequestHeader('content-type', 'application/json');
    request.addEventListener('load', function () {
        var result = request.responseText;
        var characters = JSON.parse(JSON.parse(result)['characters']['character']);
        for (var _i = 0, _a = Object.keys(characters); _i < _a.length; _i++) {
            var key = _a[_i];
            console.log(characters[key]);
        }
        addCharacter(characters);
        workspace.innerHTML = JSON.parse(result)['letter_body'];
        //workspace.innerHTML = JSON.parse(result)['letter_body']
    });
    request.send();
};
var addCharacter = function (object) {
    var $character = document.getElementById('characters');
    for (var _i = 0, _a = Object.keys(object); _i < _a.length; _i++) {
        var key = _a[_i];
        var $obj = document.createElement('option');
        $obj.appendChild(document.createTextNode(object[key]));
        $character.appendChild($obj);
    }
};
window.addEventListener('load', function () {
    getJson();
});
