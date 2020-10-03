const eventEdit = () => {
    const $editArea: HTMLTextAreaElement = <HTMLTextAreaElement>document.getElementById('edit');
    let classNameIsText = document.getElementsByClassName('text');

    for (let i=0; i<classNameIsText.length; i++){
        classNameIsText[i].addEventListener('click', () => {
            $editArea.value = classNameIsText[i].textContent
        })
    }
}

function main(){
    eventEdit()
}

main();