function searchSubmit() {
    altStyle();

    console.log(document.querySelector('#query').value);

    return false;
}


function altStyle() {
    document.querySelector('.center').style.display = 'block';
    document.querySelector('#site-title').style.display = 'none';
}
