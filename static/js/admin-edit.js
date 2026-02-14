let currentTargetInput = null;

function showAddSection() {
    document.getElementById('addSectionForm').classList.remove('hidden');
}

function hideAddSection() {
    document.getElementById('addSectionForm').classList.add('hidden');
}

function openImagePicker(inputId) {
    currentTargetInput = inputId;
    document.getElementById('imagePickerModal').classList.remove('hidden');
}

function closeImagePicker(event) {
    if (!event || event.target === event.currentTarget) {
        document.getElementById('imagePickerModal').classList.add('hidden');
        currentTargetInput = null;
    }
}

function selectImage(url) {
    if (currentTargetInput) {
        document.getElementById(currentTargetInput).value = url;
        closeImagePicker();
    }
}

function quickUploadImage() {
    const fileInput = document.getElementById('quickUploadInput');
    const file = fileInput.files[0];

    if (!file) return;

    const formData = new FormData();
    formData.append('file', file);

    const progressDiv = document.getElementById('quickUploadProgress');
    const progressBar = document.getElementById('quickUploadBar');
    progressDiv.classList.remove('hidden');
    progressBar.style.width = '30%';

    // Read CSRF token from global config or meta tag
    const csrfToken = window.bellariAdminConfig
        ? window.bellariAdminConfig.csrfToken
        : document.querySelector('meta[name="csrf-token"]').getAttribute('content');

    // Read messages from global config
    const messages = window.bellariAdminConfig && window.bellariAdminConfig.messages ? window.bellariAdminConfig.messages : {
        error: 'Error',
        uploadError: 'Upload error'
    };

    fetch('/admin/upload', {
        method: 'POST',
        headers: {
            'X-CSRFToken': csrfToken
        },
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        progressBar.style.width = '100%';
        if (data.success) {
            if (currentTargetInput) {
                document.getElementById(currentTargetInput).value = data.image.url;
            }
            setTimeout(() => {
                location.reload();
            }, 500);
        } else {
            alert(messages.error + ': ' + (data.error || 'Upload failed'));
            progressDiv.classList.add('hidden');
        }
    })
    .catch(error => {
        alert(messages.uploadError + ': ' + error);
        progressDiv.classList.add('hidden');
    })
    .finally(() => {
        fileInput.value = '';
    });
}
