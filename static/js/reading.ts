const getJson = () => {
    const workspace = document.getElementById('workspace')
    let url = '/model'+location.pathname.replace('/workspace', '');
    let request = new XMLHttpRequest();
    request.open('GET', url, true);
    request.setRequestHeader('content-type', 'application/json');
    request.addEventListener('load', () => {
        let result = request.responseText;
        let characters: object = JSON.parse(JSON.parse(result)['characters']['character'])
        for (let key of Object.keys(characters)){
            console.log(characters[key])
        }
        addCharacter(characters);
        workspace.innerHTML = JSON.parse(result)['letter_body']
        //workspace.innerHTML = JSON.parse(result)['letter_body']
    });
    request.send();
}

const addCharacter = (object: object) => {
    let $character = document.getElementById('characters');
    for (let key of Object.keys(object)){
        let $obj: HTMLOptionElement = document.createElement('option');
        $obj.appendChild(document.createTextNode(object[key]));
        $character.appendChild($obj);
        }
}

window.addEventListener('load', () => {
    getJson();
})