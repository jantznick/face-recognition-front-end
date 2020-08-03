Array.from(document.getElementsByClassName('tab')).forEach(elem => {
	elem.addEventListener('click', event => {
		if (event.path[0].classList.contains('active')) {
			console.log(event.path[0].classList)
			event.path[0].classList.remove('active');
		} else {
			event.path[0].classList.add('active');
		}
	});
})