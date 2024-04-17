console.log('JavaScript está funcionando!');
var stripe = Stripe('YOUR_STRIPE_PUBLIC_KEY');
var elements = stripe.elements();
var cardElement = elements.create('card');
cardElement.mount('#card-element');

document.getElementById('tipo_doacao').addEventListener('change', function() {
    var valorDoacao = document.getElementById('valor_doacao');
    var mensagemApadrinhar = document.getElementById('mensagem_apadrinhar');
    var cestaBasicaOptions = document.querySelector('.cesta_basica_options');

    valorDoacao.style.display = (this.value === 'doacao') ? 'block' : 'none';
    mensagemApadrinhar.style.display = (this.value === 'apadrinhar') ? 'block' : 'none';
    cestaBasicaOptions.style.display = (this.value === 'cesta_basica') ? 'block' : 'none';
});

document.getElementById('metodo_pagamento').addEventListener('change', function() {
    var detalhesCartao = document.getElementById('detalhes_cartao');
    detalhesCartao.style.display = (this.value === 'cartao') ? 'block' : 'none';
});

var form = document.getElementById('payment-form');
form.addEventListener('submit', function(event) {
    event.preventDefault();
    stripe.createToken(cardElement).then(function(result) {
        if (result.error) {
            // Exibir erros ao usuário
            console.error(result.error.message);
        } else {
            // Enviar token para o servidor para processar o pagamento
            console.log(result.token);
            // Implemente a lógica do servidor para processar o pagamento
        }
    });
});

document.addEventListener('DOMContentLoaded', function() {
    var tags = document.querySelectorAll('.tags__tag');

    tags.forEach(function(tag) {
        tag.addEventListener('click', function() {
            // Remove a classe 'active' de todas as tags
            tags.forEach(function(innerTag) {
                innerTag.classList.remove('active');
            });

            // Adiciona a classe 'active' à tag clicada
            this.classList.add('active');
        });
    });
});