nome = prompt('Qual o seu nome? ');
altura = prompt('Qual a sua altura em centímetros? ');
peso = prompt('Qual o seu peso? ');

alturaFloat = parseFloat(altura);
pesoFloat = parseFloat(peso);

alturaM = alturaFloat / 100;
altura2 = altura**2
indice = (peso / altura2);

// document.write(alturaM);
document.write(indice);