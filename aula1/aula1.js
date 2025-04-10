// function message(){
//     alert('Quer saber o teu valor? Olha para a cruz, tu vales um Deus crucificado')
// }
function mudou(){
    var image = document.getElementById('img');
    if (image.src == 'https://www.w3schools.com/js/pic_bulboff.gif'){
        image.src = 'https://www.w3schools.com/js/pic_bulbon.gif';
    }
    else {
        image.src = 'https://www.w3schools.com/js/pic_bulboff.gif'
    }
}