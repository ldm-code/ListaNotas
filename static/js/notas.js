document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.toggle-editar').forEach(btn => {
        btn.addEventListener('click', () => {
            const id = btn.getAttribute('data-id');

            const spanNome = document.getElementById(`nome-${id}`);
            const spanNota = document.getElementById(`nota-${id}`);

            const inputNome = document.getElementById(`input-nome-${id}`);
            const inputNota = document.getElementById(`input-nota-${id}`);

            const hiddenNome = document.getElementById(`hidden-nome-${id}`);
            const hiddenNota = document.getElementById(`hidden-nota-${id}`);

            const submitBtn = document.querySelector(`#form-edit-${id} input[type="submit"]`);

            if (!spanNome || !spanNota || !inputNome || !inputNota || !hiddenNome || !hiddenNota || !submitBtn) return;

            inputNome.style.display = 'inline-block';
            inputNota.style.display = 'inline-block';
            submitBtn.style.display = 'inline-block';
            spanNome.style.display = 'none';
            spanNota.style.display = 'none';

            inputNome.value = spanNome.textContent.trim();
            inputNota.value = spanNota.textContent.trim();
            hiddenNome.value = inputNome.value;
            hiddenNota.value = inputNota.value;

            inputNome.oninput = () => hiddenNome.value = inputNome.value.trim();
            inputNota.oninput = () => hiddenNota.value = inputNota.value;
        });
    });

    document.querySelectorAll('form[id^="form-edit-"] input[type="submit"]').forEach(submitBtn => {
        submitBtn.addEventListener('click', e => {
            const form = submitBtn.closest('form');
            const id = form.id.replace('form-edit-', '');
            const notaInput = document.getElementById(`input-nota-${id}`);
            const hiddenNota = document.getElementById(`hidden-nota-${id}`);
            const nota = Number(notaInput.value);
            if (isNaN(nota) || nota < 0 || nota > 10 || !Number.isInteger(nota)) {
                    e.preventDefault();
                    alert("Erro: a nota deve ser um número inteiro entre 0 e 10!");
                    notaInput.focus();
                    } else {
                         hiddenNota.value = nota;
                    }


        });
    });
});
