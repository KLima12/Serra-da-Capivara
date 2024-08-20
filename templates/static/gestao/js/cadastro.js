// cadastro.js

document.addEventListener('DOMContentLoaded', function() {
    const photoFields = document.getElementById('photo-fields');
    
    function addPhotoField() {
        // Cria um novo campo de input para upload de fotos
        const newInput = document.createElement('input');
        newInput.type = 'file';
        newInput.name = 'photos[]'; // Define o nome como array de fotos
        newInput.accept = 'image/*'; // Apenas arquivos de imagem

        // Adiciona o novo campo ao contêiner de fotos
        photoFields.appendChild(newInput);
    }

    // Torna a função addPhotoField global para que possa ser chamada a partir do HTML
    window.addPhotoField = addPhotoField;
});

function clique(){
    console.log("Clicado")
}