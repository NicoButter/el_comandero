document.addEventListener("DOMContentLoaded", function () {
    const formsetContainer = document.getElementById("formset-container");
    const addButton = document.getElementById("add-form");
    const totalForms = document.querySelector("#id_form-TOTAL_FORMS");

    addButton.addEventListener("click", function () {
        const formNum = parseInt(totalForms.value);
        const newForm = formsetContainer.children[0].cloneNode(true); // Copia el primer form

        // Reemplaza los índices en los nuevos inputs
        newForm.innerHTML = newForm.innerHTML.replace(/form-\d+/g, `form-${formNum}`);
        formsetContainer.appendChild(newForm);

        // Actualiza el TOTAL_FORMS
        totalForms.value = formNum + 1;

        // Agrega funcionalidad para eliminar
        attachRemoveHandlers();
    });

    function attachRemoveHandlers() {
        document.querySelectorAll(".btn-remove").forEach((button) => {
            button.addEventListener("click", function () {
                this.parentElement.remove();

                // Recalcula el TOTAL_FORMS
                totalForms.value = formsetContainer.children.length;
            });
        });
    }

    // Llamamos a la función para los elementos ya existentes
    attachRemoveHandlers();
});
