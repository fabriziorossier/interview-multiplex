document.addEventListener('DOMContentLoaded', function() {
    let buttons = document.querySelectorAll('.btn');
    buttons.forEach(function(button) {
        button.addEventListener('click', function(e) {
            if (e.target.classList.contains('active')) {
                e.target.classList.remove('active');
            } else {
                e.target.classList.add('active');
            }
        });
    });

    let recipeForm = document.querySelector('#recipeForm');
    recipeForm.addEventListener('submit', function(event) {
        let checkboxes = recipeForm.querySelectorAll('input[type="checkbox"]');
        let isChecked = Array.from(checkboxes).some(checkbox => checkbox.checked);
        
        if (!isChecked) {
            event.preventDefault();
            let validationModal = new bootstrap.Modal(document.querySelector('#validationModal'));
            validationModal.show();
        } else {
            let loadingModal = document.querySelector('#loadingModal');
            loadingModal = new bootstrap.Modal(document.querySelector('#loadingModal'));
            loadingModal.show();
        }
    });    
});