const triggerUpdate = document.querySelector('select[name="pick-state');

window.addEventListener('DOMContentLoaded', (event) => {
    getData('/api/covid/', triggerUpdate.value)
    .then(data =>{
        const list = document.querySelector('#c19-entrypoint');
        list.innerHTML='';
        for (let [key, value] of Object.entries(data)) {
            let li = document.createElement('li');
            li.appendChild(document.createTextNode(value));
            list.appendChild(li);
        }
        document.querySelector('.to-update').innerText = "How COVID-19 affects voting in " + triggerUpdate.value;
    })
})

triggerUpdate.addEventListener('change', (event) => {
    //getData('/api/covid/', event.target.value)
    getData('/api/covid/', event.target.value)
    .then(data => {
        const list = document.querySelector('#c19-entrypoint');
        list.innerHTML='';
        for (let [key, value] of Object.entries(data)) {
            let li = document.createElement('li');
            li.appendChild(document.createTextNode(value));
            list.appendChild(li);
        }

        document.querySelector('.to-update').innerText = "How COVID-19 affects voting in " + event.target.value;
    })
});

async function getData(url, state) {
    const response = await fetch(url + state);
    const data = await response.json();
    return data
};


