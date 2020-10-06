
document.getElementById("submit-button").addEventListener('click', (event) => {
	event.preventDefault();

	const fileInput = document.querySelector('#photo-upload') ;
	const formData = new FormData();

	formData.append('file', fileInput.files[0]);

	const options = {
		method: 'POST',
		body: formData,
	};

	fetch('/submit-photo', options)
});