var eventEdit = function () {
    var $editArea = document.getElementById('edit');
    var classNameIsText = document.getElementsByClassName('text');
    var _loop_1 = function (i) {
        classNameIsText[i].addEventListener('click', function () {
            $editArea.value = classNameIsText[i].textContent;
        });
    };
    for (var i = 0; i < classNameIsText.length; i++) {
        _loop_1(i);
    }
};
function main() {
    eventEdit();
}
main();
