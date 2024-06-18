const btnsOpenModal = document.querySelectorAll('.show-modal');
const overlay = document.querySelector('.overlay');
const btnCloseModal = document.querySelector('.close-modal');
const modal = document.querySelector('.modal');

addModal = function () {
  modal.classList.remove('hidden');
  overlay.classList.remove('hidden');
}

  //Alternatively
//   modal.classList.toggle('hidden');
//   overlay.classList.toggle('hidden');

  btnsOpenModal.addEventListener('click', addModal);


removeModal = function () {
  modal.classList.add('hidden');
  overlay.classList.add('hidden');
};

btnCloseModal.addEventListener('click', removeModal);

overlay.addEventListener('click', removeModal);

document.addEventListener('keydown', function (e) {
  if (e.key === 'Escape' &&  !modal.classList.contains('hidden')) 
    {
      removeModal();
    }
 
})
