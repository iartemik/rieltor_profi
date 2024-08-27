
document.getElementById('flip-register').addEventListener('click', function() { 
    document.querySelector('.container').classList.add('flip'); 
}); 
 
document.getElementById('flip-login').addEventListener('click', function() { 
    document.querySelector('.container').classList.remove('flip'); 
});


document.addEventListener('DOMContentLoaded', () => {
    const flashes = document.querySelectorAll('.flashes li');
    if (flashes) {
        setTimeout(() => {
            flashes.forEach(flash => {
                flash.style.display = 'none';
            });
        }, 5000); // 5 секунд
    }
});

// let is_show_rieltor_info=0;

// document.getElementById('show_info_for_rieltor').addEventListener('click', function() { 
//     if( is_show_rieltor_info == 0 )
//        {  
//         document.getElementById('rieltor-info').classList.add('show-info'); 
//         is_show_rieltor_info=1;
//     }
//     else {
//         document.getElementById('rieltor-info').classList.remove('show-info'); 
//         is_show_rieltor_info=0;
//         }

// });
document.getElementById('toggle-button').addEventListener('click', function() {  
    var infoDiv = document.getElementById('rieltor-info');  
    if (infoDiv.style.display === 'none' || infoDiv.style.display === '') {  
        this.textContent = 'Скрыть';
        infoDiv.style.display="block";
    } else {   
        infoDiv.style.display='none';
        this.textContent = 'Информация для риелтора';  
    }  
});  
