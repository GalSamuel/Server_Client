const message = 'Hello from JavaScript!';

fetch('', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/x-www-form-urlencoded',
  },
  body: `message=${message}`,
})
  .then(response => response.json())
  .then(data => console.log(data.response));
  
