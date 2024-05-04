import axios from 'axios';

axios.get('http://localhost:3000/api/sua-rota')
 .then(response => {
    console.log(response.data);
  })
 .catch(error => {
    console.error(error);
  });