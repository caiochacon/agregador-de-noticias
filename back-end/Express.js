const express = require('express');
const cors = require('cors');

const app = express();

// Habilita o CORS para todas as origens
app.use(cors());

// Suas rotas e lógicas de servidor vão aqui

app.listen(3000, () => {
  console.log('Servidor rodando na porta 3000');
});