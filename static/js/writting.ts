const configurationOptionFunc = (configurationOption: string, configurations: string[]): number => {
    for (let i=0; i<configurations.length; i++){
        if (configurations[i] == configurationOption){
            return i
        }
    }
    return null
}

const workspaceOption = (character: string, letter: string, configurationOption:string): string => {
    const workspace: HTMLDivElement = <HTMLDivElement>document.getElementById('workspace')
    const configurations: string[] = ['セリフ', 'ト書き', '柱'];
    const configurationOptionNum: number = configurationOptionFunc(configurationOption, configurations)
    let $pTag = document.createElement('p')
    let lines: string
    if (configurations[configurationOptionNum] == configurations[0]){
        lines = character + '「' + letter + '」';
    }else if (configurations[configurationOptionNum] == configurations[1]){
        lines = letter
    }
    $pTag.appendChild(document.createTextNode(lines))
    $pTag.className = 'text';
    workspace.append($pTag);

    return character
}


function workSpace(){
    let cell_letter = document.getElementById('cell-letter');

    cell_letter.addEventListener('keydown', (event) => {
        if (event.key === 'Enter') {
            if (event.shiftKey) {
                let characterObj: HTMLSelectElement = <HTMLSelectElement>document.getElementById('characters');
                let character: string = characterObj.value;
                let cellContentObj: HTMLTextAreaElement = <HTMLTextAreaElement>document.getElementById('cell-letter');
                let letter: string = cellContentObj.value
                let configurationOptionObj: HTMLSelectElement = <HTMLSelectElement>document.getElementById('configuration')
                let configurationOption: string = configurationOptionObj.value
                workspaceOption(character, letter, configurationOption);
                cellContentObj.value = ''
            }
        }
    });
}

const writingMode = () => {
    let writingModeButton: HTMLInputElement = <HTMLInputElement>document.getElementById('write-mode-button');
    writingModeButton.addEventListener('click', () => {
        let writingModeObj: HTMLSelectElement = <HTMLSelectElement>document.getElementById('writing-mode');
        let writingMode = writingModeObj.value
        let workspace: HTMLDivElement = <HTMLDivElement>document.getElementById('workspace')
        if (writingMode === '縦書き'){
            workspace.className = 'workspace-freshly';
        }else if (writingMode === '横書き'){
            workspace.className = 'workspace-side';
        }
    });
}

function addCharacter(){
    let $addCharacter = document.getElementById('add-character');
    let $character = document.getElementById('characters');
    $addCharacter.addEventListener('click', () => {
        let characterNameObj: HTMLInputElement = <HTMLInputElement>document.getElementById('character-name')
        let characterName: string = characterNameObj.value;
        let $obj: HTMLOptionElement = document.createElement('option');
        $obj.appendChild(document.createTextNode(characterName));
        $character.appendChild($obj);
    });
}

function newCharacter(){
    let $newCharacter = document.getElementById('new_character');
    $newCharacter.style.display = 'none';
    let $createCharacterBtn = document.getElementById('create_character');
    $createCharacterBtn.addEventListener('click', () => {
        if ($newCharacter.style.display == 'none') {
            $newCharacter.style.display = 'block';
        }else {
            $newCharacter.style.display = 'none';
        }
    });
}

const deleteCharacter = () => {
    let $deleteCharacter = document.getElementById('delete_characters');
    $deleteCharacter.addEventListener('click', () => {
        let $now_characters: HTMLSelectElement = <HTMLSelectElement>document.getElementById('characters');
        let characters = $now_characters.children
        let $characterArea: HTMLDivElement = <HTMLDivElement>document.getElementById('delete_characters_area');
        for (let i=0; i<characters.length; i++){
            let $divElm: HTMLDivElement = <HTMLDivElement>document.createElement('div');
            $divElm.setAttribute('id', 'character'+i);
            $divElm.appendChild(document.createTextNode(characters.item(i).textContent));
            $characterArea.appendChild($divElm)
        }
    })
}


const sendJsonObject = () => {
    const sendButton = document.getElementById('send-button')
    sendButton.addEventListener('click', () => {
        let sendCharacter: object = {};
        const characters: HTMLSelectElement = <HTMLSelectElement>document.getElementById('characters');
        const letterBody: HTMLDivElement = <HTMLDivElement>document.getElementById('workspace');
        for (let i=0; i<characters.children.length; i++) {
            sendCharacter[i] = characters.children.item(i).textContent;
        }
        let resultObjects: object = {
            'title': document.getElementById('title').innerText,
            'characters': JSON.stringify(sendCharacter),
            'letterBody': letterBody.innerHTML,
            'page_num': 0
        }
        sendJson(resultObjects);
    })
}

const sendJson = (content: object) => {
    const ajax = new XMLHttpRequest();
    ajax.open('POST', location.pathname, true);
    ajax.setRequestHeader('content-type', 'application/json');
    ajax.setRequestHeader('data-type', 'json');
    ajax.send(JSON.stringify(content));
};

const sendCharacter = () => {
    const sendCharacter = document.getElementById('send_character');
    let title: HTMLHeadElement = <HTMLHeadElement>document.getElementById('title');
    let title_text: string = title.textContent
    sendCharacter.addEventListener('click', () => {
        let sendCharacters: object = {};
        let characters: HTMLSelectElement = <HTMLSelectElement>document.getElementById('characters');
        for (let i=0; i<characters.children.length; i++) {
            sendCharacters[i] = characters.children.item(i).textContent;
        }
        let newObj: object = {
            'title': title_text,
            'characters': JSON.stringify(sendCharacters)
        }
        sendJson(newObj);
    })
}



function main(){
    workSpace();
    writingMode();
    addCharacter();
    newCharacter();
    sendJsonObject();
    deleteCharacter();
}

main();