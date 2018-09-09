function searchSubmit() {
    altStyle();

    var baseURI = '/search/';
    var query = document.querySelector('#query').value;
    document.querySelector('#results-frame').src = baseURI + query;
}


function altStyle() {
    document.querySelector('.center').style.display = 'block';
    document.querySelector('#site-title').style.display = 'none';
    document.querySelector('#results-frame').style.display = 'block';
}
