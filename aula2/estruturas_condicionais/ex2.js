nome = prompt('Qual o seu nome? ');
altura = prompt('Qual a sua altura em centímetros? ');
peso = prompt('Qual o seu peso? ');

alturaFloat = parseFloat(altura);
pesoFloat = parseFloat(peso);

alturaM = alturaFloat / 100;
indice = (peso / (alturaM*alturaM));

document.write(indice);