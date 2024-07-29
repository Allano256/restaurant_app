'use strict';
// Delete reservation 
const modal = document.querySelector('.modal');
const btnCloseModal = document.querySelector('.close-modal');
const btnOpenModal = document.querySelector('.show-modal');
const cancelConfirm = document.getElementById("cancelConfirm");
const deleteButtons = document.getElementsByClassName("btn-delete");
const overlay = document.querySelector('.overlay');


const openModal = function (){
  
        modal.classList.remove('hidden');
        overlay.classList.remove('hidden');
      
}

btnOpenModal.addEventListener('click', openModal 
)

const closeModal = function(){
    modal.classList.add('hidden'); 
    overlay.classList.add('hidden'); 
}

btnCloseModal.addEventListener('click', closeModal );

btnCloseModal.addEventListener('click',closeModal);

overlay.addEventListener('click', closeModal);

document.addEventListener('keydown', function (e) {
  if (e.key === 'Escape' &&  !modal.classList.contains('hidden')) 
    {
      closeModal();
    }
 
})

for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
      let reservationId = e.target.getAttribute("data-id");
      cancelConfirm.href = `/cancel/${reservationId}`;
      // closeModal.add();
    });
  }

