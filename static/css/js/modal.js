'use strict';
// Delete reservation 
const modal = document.querySelector('.modal');
const btnCloseModal = document.querySelector('.close-modal');
const btnOpenModal = document.querySelector('.show-modal');
const cancelConfirm = document.getElementById("cancelConfirm");
const deleteButtons = document.getElementsByClassName("btn-delete");

// Edit Reservation
// const editButtons = document.getElementsByClassName("btn-edit");
// const reserveText = document.getElementById("id_body");
// const reserveForm = document.getElementById("updateForm");
// const submitButton = document.getElementById("submitButton");
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
      let reservationId = e.target.getAttribute("data-id");
      cancelConfirm.href = `/booking/cancel/${reservationId}`;
      // closeModal.add();
    });
  }


  // for (let button of editButtons) {
  //   button.addEventListener("click", (e) => {
  //     let reservationId = e.target.getAttribute("data-id");
  //     let reserveContent = document.getElementById(`form-control${reservationId}`).innerText;
  //     reserveText.value = reserveContent;
  //     submitButton.innerText = "Update";
  //     reserveForm.setAttribute("action", `/booking/edit/${reservationId}`);
  //   });
  // }