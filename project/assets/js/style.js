var openNav = document.querySelector('.mobi-bars-wrap a');
var mobiNavDrawer = document.querySelector('.mobi-nav-drawer');
var closeNav = document.querySelector('#btnclose');
openNav.addEventListener('click',open);
closeNav.addEventListener('click',close);
function open(){
    mobiNavDrawer.style.display ='block';
    mobiNavDrawer.style.transform = 'translateX(0%)';
}
function close(){
    mobiNavDrawer.style.transform = 'translateX(100%)';
}
