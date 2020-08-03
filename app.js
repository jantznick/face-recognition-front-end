const express = require('express')
const app = express()
const port = 3000
const formidable = require('formidable');

app.set('view engine', 'ejs');

app.use(express.static('public'))

app.get('/', (req, res) => {
	res.render('index')
})

app.post('/submit-photo', (req, res) => {
	const form = formidable({
		multiples: true
	});

	form.parse(req, (err, fields, files) => {
		if (err) {
		  next(err);
		  return;
		}
		res.json({ fields, files });
	  });
	// res.redirect('/')
})

app.listen(port, () => {
	console.log(`Example app listening at http://localhost:${port}`)
})