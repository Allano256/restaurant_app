'use strict';

const modal = document.querySelector('.modal');
const btnCloseModal = document.querySelector('.close-modal');
const btnOpenModal = document.querySelector('.show-modal');
const cancelConfirm = document.getElementById("cancelConfirm");
const deleteButtons = document.getElementsByClassName("btn-delete");

const openModal = function (){
    
        modal.classList.remove('hidden');
       
}
 
btnOpenModal.addEventListener('click', openModal 
)

const closeModal = function(){
    modal.classList.add('hidden');
   
}

btnCloseModal.addEventListener('click', closeModal );

for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
      let reservationId = e.target.getAttribute("reservation_id");
      cancelConfirm.href = `/booking/cancel/${reservationId}`;
      closeModal.add();
    });
  }