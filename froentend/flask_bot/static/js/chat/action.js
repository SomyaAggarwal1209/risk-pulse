document.addEventListener("DOMContentLoaded", function () {
    const sendButton = document.querySelector('.send-button');
    const fileUploadButton = document.querySelector('.file-upload-button');
    const chatInput = document.querySelector('.chat-input');
    const messagesContainer = document.querySelector('.messages');

    sendButton.addEventListener('click', () => {
        sendMessage(chatInput.value);
    });

    chatInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            const data_up=chatInput.value;
            const messageText = chatInput.value.trim();
        if (messageText) {
            const messageElement = document.createElement('div');
            messageElement.classList.add('message', 'user-message');
            messageElement.textContent = messageText;
            messagesContainer.appendChild(messageElement);
            chatInput.value = '';
            messagesContainer.scrollTop = messagesContainer.scrollHeight;
        }
            sendMessage(data_up);
        }
    });

    fileUploadButton.addEventListener('click', () => {
        const fileInput = document.createElement('input');
        fileInput.type = 'file';
        fileInput.style.display = 'none';
        fileInput.addEventListener('change', () => {
            uploadFile(fileInput.files[0]);
        });
        document.body.appendChild(fileInput);
        fileInput.click();
    });

    function sendMessage(message) {


        fetch('/api/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ message: message })
        })
            .then(response => response.json())
            .then(data => {
                displayMessage(data.response, 'bot');
            })
            .catch(error => console.error('Error:', error));
    }

    function uploadFile(file) {
        const formData = new FormData();
        formData.append('file', file);

        fetch('/api/upload', {
            method: 'POST',
            body: formData
        })
            .then(response => response.json())
            .then(data => {
                displayMessage(data.response, 'bot');
            })
            .catch(error => console.error('Error:', error));
    }

    function displayMessage(message, sender) {
        const messageElement = document.createElement('div');
        messageElement.classList.add('message', sender);
        messageElement.innerText = message;
        messagesContainer.appendChild(messageElement);
        chatInput.value = '';
    }
});
