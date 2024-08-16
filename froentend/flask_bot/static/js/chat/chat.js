document.addEventListener('DOMContentLoaded', function() {
    const sendButton = document.querySelector('.send-button');
    const fileUploadButton = document.querySelector('.file-upload-button');
    const chatInput = document.querySelector('.chat-input');
    const messages = document.querySelector('.messages');

    sendButton.addEventListener('click', sendMessage);
    fileUploadButton.addEventListener('click', uploadFile);
    chatInput.addEventListener('keypress', function(event) {
        if (event.key === 'Enter') {
            sendMessage();
        }
    });

    function sendMessage() {
        const messageText = chatInput.value.trim();
        if (messageText) {
            const messageElement = document.createElement('div');
            messageElement.classList.add('message', 'user-message');
            messageElement.textContent = messageText;
            messages.appendChild(messageElement);
            chatInput.value = '';
            messages.scrollTop = messages.scrollHeight;
        }
    }

    function uploadFile() {
        // Implement file upload logic here
        alert('File upload clicked!');
    }
});
