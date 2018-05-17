const cepinfo = document.querySelector('#id_cep')
const logradouro = document.querySelector('#id_logradouro')
const bairro = document.querySelector('#id_bairro')
const cidade = document.querySelector('#id_cidade')
const estado = document.querySelector('#id_estado')
const apikey ='FnM13uK1TWD1sleMUI7T3InJNdQ='

if(cepinfo) {
    cepinfo.addEventListener('blur', function() {
        let cep = cepinfo.value
        cep = cep.replace(/\.|\-/g, '');
        let url = `https://viacep.com.br/ws/${cep}/json/`
        fetch(url)
            .then(response => response.json())
            .then(data => {
                logradouro.value = data.logradouro
                bairro.value = data.bairro
                estado.value = data.uf
                cidade.value = data.localidade
            })
    })
}