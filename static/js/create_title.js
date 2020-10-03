var $createButton = document.getElementById('create');
var checkTitle = function (event) {
    var $title = document.getElementById('title');
    var $author = document.getElementById('author');
    if ($title.value === '' || $author.value === '') {
        event.preventDefault();
        alert('タイトルか作者が記述されてません');
    }
};
function main() {
    $createButton.addEventListener('click', function (event) {
        checkTitle(event);
    });
}
main();
