var configurationOptionFunc = function (configurationOption, configurations) {
    for (var i = 0; i < configurations.length; i++) {
        if (configurations[i] == configurationOption) {
            return i;
        }
    }
    return null;
};
var workspaceOption = function (character, letter, configurationOption) {
    var workspace = document.getElementById('workspace');
    var configurations = ['セリフ', 'ト書き', '柱'];
    var configurationOptionNum = configurationOptionFunc(configurationOption, configurations);
    var $pTag = document.createElement('p');
    var lines;
    if (configurations[configurationOptionNum] == configurations[0]) {
        lines = character + '「' + letter + '」';
    }
    else if (configurations[configurationOptionNum] == configurations[1]) {
        lines = letter;
    }
    $pTag.appendChild(document.createTextNode(lines));
    $pTag.className = 'text';
    workspace.append($pTag);
    return character;
};
function workSpace() {
    var cell_letter = document.getElementById('cell-letter');
    cell_letter.addEventListener('keydown', function (event) {
        if (event.key === 'Enter') {
            if (event.shiftKey) {
                var characterObj = document.getElementById('characters');
                var character = characterObj.value;
                var cellContentObj = document.getElementById('cell-letter');
                var letter = cellContentObj.value;
                var configurationOptionObj = document.getElementById('configuration');
                var configurationOption = configurationOptionObj.value;
                workspaceOption(character, letter, configurationOption);
                cellContentObj.value = '';
            }
        }
    });
}
var writingMode = function () {
    var writingModeButton = document.getElementById('write-mode-button');
    writingModeButton.addEventListener('click', function () {
        var writingModeObj = document.getElementById('writing-mode');
        var writingMode = writingModeObj.value;
        var workspace = document.getElementById('workspace');
        if (writingMode === '縦書き') {
            workspace.className = 'workspace-freshly';
        }
        else if (writingMode === '横書き') {
            workspace.className = 'workspace-side';
        }
    });
};
function addCharacter() {
    var $addCharacter = document.getElementById('add-character');
    var $character = document.getElementById('characters');
    $addCharacter.addEventListener('click', function () {
        var characterNameObj = document.getElementById('character-name');
        var characterName = characterNameObj.value;
        var $obj = document.createElement('option');
        $obj.appendChild(document.createTextNode(characterName));
        $character.appendChild($obj);
    });
}
function newCharacter() {
    var $newCharacter = document.getElementById('new_character');
    $newCharacter.style.display = 'none';
    var $createCharacterBtn = document.getElementById('create_character');
    $createCharacterBtn.addEventListener('click', function () {
        if ($newCharacter.style.display == 'none') {
            $newCharacter.style.display = 'block';
        }
        else {
            $newCharacter.style.display = 'none';
        }
    });
}
var deleteCharacter = function () {
    var $deleteCharacter = document.getElementById('delete_characters');
    $deleteCharacter.addEventListener('click', function () {
        var $now_characters = document.getElementById('characters');
        var characters = $now_characters.children;
        var $characterArea = document.getElementById('delete_characters_area');
        for (var i = 0; i < characters.length; i++) {
            var $divElm = document.createElement('div');
            $divElm.setAttribute('id', 'character' + i);
            $divElm.appendChild(document.createTextNode(characters.item(i).textContent));
            $characterArea.appendChild($divElm);
        }
    });
};
var sendJsonObject = function () {
    var sendButton = document.getElementById('send-button');
    sendButton.addEventListener('click', function () {
        var sendCharacter = {};
        var characters = document.getElementById('characters');
        var letterBody = document.getElementById('workspace');
        for (var i = 0; i < characters.children.length; i++) {
            sendCharacter[i] = characters.children.item(i).textContent;
        }
        var resultObjects = {
            'title': document.getElementById('title').innerText,
            'characters': JSON.stringify(sendCharacter),
            'letterBody': letterBody.innerHTML,
            'page_num': 0
        };
        sendJson(resultObjects);
    });
};
var sendJson = function (content) {
    var ajax = new XMLHttpRequest();
    ajax.open('POST', location.pathname, true);
    ajax.setRequestHeader('content-type', 'application/json');
    ajax.setRequestHeader('data-type', 'json');
    ajax.send(JSON.stringify(content));
};
var sendCharacter = function () {
    var sendCharacter = document.getElementById('send_character');
    var title = document.getElementById('title');
    var title_text = title.textContent;
    sendCharacter.addEventListener('click', function () {
        var sendCharacters = {};
        var characters = document.getElementById('characters');
        for (var i = 0; i < characters.children.length; i++) {
            sendCharacters[i] = characters.children.item(i).textContent;
        }
        var newObj = {
            'title': title_text,
            'characters': JSON.stringify(sendCharacters)
        };
        sendJson(newObj);
    });
};
function main() {
    workSpace();
    writingMode();
    addCharacter();
    newCharacter();
    sendJsonObject();
    deleteCharacter();
}
main();
