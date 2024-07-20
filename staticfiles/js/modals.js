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

for(let button of deleteButtons){
    button.addEventListener('click', (e) => {
        let reservationId = e.target.getAttribute('data-id');
        cancelConfirm.href = `/cancel/${reservationId}`;
    })
}
