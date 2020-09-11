//triggerUpdate defined in the covid data file


window.addEventListener('DOMContentLoaded', (event) => {
    getData('/api/registration/general/', triggerUpdate.value)
    .then(data => {
        document.querySelector('#reg-in-person .card-body > p').innerText = data.inPerson;
        document.querySelector('#reg-by-mail .card-body > p').innerText = data.byMail;
        document.querySelector('#reg-online .card-body > p').innerText = data.online;

        if (data.onlineRegistration.length > 1) {
            document.getElementById('vote-online-btn').style.display="inline";
            document.getElementById('vote-online-btn').innerText = "Register to vote online in " + triggerUpdate.value
            document.getElementById('vote-online-btn').href = data.onlineRegistration;
        } else {
            document.getElementById('vote-online-btn').style.display="none"; 
        }
    })
})

triggerUpdate.addEventListener('change', (event) => {
    getData('/api/registration/general/', event.target.value)
    .then(data => {
        document.querySelector('#reg-in-person .card-body > p').innerText = data.inPerson;
        document.querySelector('#reg-by-mail .card-body > p').innerText = data.byMail;
        document.querySelector('#reg-online .card-body > p').innerText = data.online;
        
        if (data.onlineRegistration.length > 1) {
            document.getElementById('vote-online-btn').style.display="inline";
            document.getElementById('vote-online-btn').innerText = "Register to vote online in " + event.target.value
            document.getElementById('vote-online-btn').href = data.onlineRegistration;
        } else {
            document.getElementById('vote-online-btn').style.display="none";
        }
    })
});

async function getData(url, state) {
    const response = await fetch(url + state);
    const data = await response.json();
    return data
};


