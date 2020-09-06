//triggerUpdate defined in the covid data file


window.addEventListener('DOMContentLoaded', (event) => {
    getData('/api/registration/general/', triggerUpdate.value)
    .then(data => {
        document.querySelector('#reg-in-person .card-body > p').innerText = data.inPerson;
        document.querySelector('#reg-by-mail .card-body > p').innerText = data.byMail;
        document.querySelector('#reg-online .card-body > p').innerText = data.online;
    })

})

triggerUpdate.addEventListener('change', (event) => {
    getData('/api/registration/general/', event.target.value)
    .then(data => {
        document.querySelector('#reg-in-person .card-body > p').innerText = data.inPerson;
        document.querySelector('#reg-by-mail .card-body > p').innerText = data.byMail;
        document.querySelector('#reg-online .card-body > p').innerText = data.online;
    })
});

async function getData(url, state) {
    const response = await fetch(url + state);
    const data = await response.json();
    return data
};


