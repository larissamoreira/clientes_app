const cepinfo = document.querySelector('#id_cep')
const logradouro = document.querySelector('#id_logradouro')
const bairro = document.querySelector('#id_bairro')
const cidade = document.querySelector('#id_cidade')
const estado = document.querySelector('#id_estado')
const numero = document.querySelector('#id_numero')

var rua = 'oi'
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
    
                let url2 = `https://maps.googleapis.com/maps/api/geocode/json?address=rua+${logradouro.value.replace(/ /g, "+")},${cidade.value.replace(/ /g, "+")}&key=AIzaSyB2uPawOPYriT7y7vdd0OeNp_JButueuvE`
                fetch(url2)
                    .then(response => response.json())
                    .then(data => {
                        console.log(data["results"][0].geometry.location)
                })
    })
}
//

// class MapView{
//     static generateMap( tag, coords, nome, desc) {
//         let map = new google.maps.Map(tag, {
//             zoom: 19,
//             center: coords
//         });
//         let marker = new google.maps.Marker({
//             position: coords,
//             map: map
//         })
//         marker.addListener('click', function(){
//             MapView._generateInfoWindow(nome, desc)
//         })
//         return map
//     }
//     static _generateInfoWindow(nome, descricao) {
//         return `<div id="content">
//             <div id="siteNotice">
//             </div>
//             <h1 id="firstHeading" class="firstHeading">${nome}</h1>
//             <div id="bodyContent">
//             <p>${descricao}</p>
//             </div>
//             </div>`
//     }  
// }