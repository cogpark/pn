//triggerUpdate defined in the covid data file

window.addEventListener('DOMContentLoaded', (event)=> {
    getData('/api/absentee/',triggerUpdate.value)
    .then(data => {
        let mailInstructions = data.mail_instructions;
        let inPersonInstructions = data.in_person_instructions;

        document.querySelector('#ab-mail-instructions .card-body > p').innerHTML  = mailInstructions;
        document.querySelector('#ab-person-instructions .card-body > p').innerHTML = inPersonInstructions;
        document.querySelector('#deadline-mail-request .card-body > p').innerHTML = data.mail_request_deadline;
        document.querySelector('#deadline-ballot-submissions .card-body > p').innerHTML = data.ballot_delivery; 
        document.querySelector('#ab-requirements .card-body > p').innerHTML = data.requirements;
        document.querySelector('a#learn-more').href = data.source;
    });
})

triggerUpdate.addEventListener('change', (event) => {
    getData('/api/absentee/', event.target.value)
    .then(data => {
        let mailInstructions = data.mail_instructions;
        let inPersonInstructions = data.in_person_instructions;

        document.querySelector('#ab-mail-instructions .card-body > p').innerHTML  = mailInstructions;
        document.querySelector('#ab-person-instructions .card-body > p').innerHTML = inPersonInstructions;
        document.querySelector('#deadline-mail-request .card-body > p').innerHTML = data.mail_request_deadline;
        document.querySelector('#deadline-ballot-submissions .card-body > p').innerHTML = data.ballot_delivery; 
        document.querySelector('#ab-requirements .card-body > p').innerHTML = data.requirements;
        document.querySelector('a#learn-more').href = data.source;
    })
});

async function getData(url, state) {
    const response = await fetch(url + state);
    const data = await response.json();
    return data
};


//at_polls
//other_options
//no_id
