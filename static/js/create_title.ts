const $createButton = document.getElementById('create');

const checkTitle = (event) => {
    const $title: HTMLInputElement = <HTMLInputElement>document.getElementById('title');
    const $author: HTMLInputElement = <HTMLInputElement>document.getElementById('author');
    if ($title.value === '' || $author.value === '') {
        event.preventDefault();
        alert('タイトルか作者が記述されてません')
    }
}

function main(){
    $createButton.addEventListener('click', (event) => {
        checkTitle(event);
    })
}


main();