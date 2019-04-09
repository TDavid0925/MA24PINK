$(document).ready(function () {
    $('.nav-item').on('click', function () {
        console.log("obtain event");
        changeActivateItem($(this));
    })
})

function changeActivateItem(item){
    item.parent().children($('.nav-item')).each(function () {
        $(this).children($(".nav-link")).removeClass("active");
    })

    item.children($(".nav-link")).addClass("active");
}