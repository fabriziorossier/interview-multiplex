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

    let submitButton = document.querySelector('#receta');
    submitButton.addEventListener('submit', function() {
        loadingModal = document.querySelector('#loadingModal');
        loadingModal = new bootstrap.Modal(document.getElementById('loadingModal'));
        loadingModal.show();
    });
});