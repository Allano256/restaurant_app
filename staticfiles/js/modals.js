'use strict';

const modal = document.querySelector('.modal');
const btnCloseModal = document.querySelector('.close-modal');
const btnOpenModal = document.querySelector('.show-modal');

const openModal = function (){

        modal.classList.remove('hidden');

}

btnOpenModal.addEventListener('click', openModal 
)

const closeModal = function(){
    modal.classList.add('hidden');

}

btnCloseModal.addEventListener('click', closeModal );
