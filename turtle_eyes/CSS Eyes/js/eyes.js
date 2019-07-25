function AngryEyes(){
    setTimeout(function(){
        document.getElementById("circleLeft").classList.remove('errorGlowLeft');
        document.getElementById("circleRight").classList.remove('errorGlowRight');
    }, 6000);
    document.getElementById("circleLeft").classList.add('errorGlowLeft');
    document.getElementById("circleRight").classList.add('errorGlowRight');
}