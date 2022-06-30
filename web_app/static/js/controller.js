document.querySelector('#show-or-hide').addEventListener('click', function(){


    if(document.querySelector('.comentConteiner').style.display === 'block'){
        document.querySelector('.comentConteiner').style.display = 'none';
    }
    else {
        document.querySelector('.comentConteiner').style.display = 'block';
    }
})