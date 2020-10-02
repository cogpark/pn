//triggerUpdate defined in the covid data file
window.addEventListener('DOMContentLoaded', (event) => {
    getData('/api/id/', triggerUpdate.value)
    .then(data => {
        let atPolls = data.at_polls;
        let otherOptions = data.other_options;
        let noId = data.no_id;
        document.querySelector('#at-polls .card-body > p').innerHTML  = atPolls;
        document.querySelector('#at-polls h4').innerHTML  = "Voter ID requirements in " + triggerUpdate.value;
        document.querySelector('#other-options .card-body > p').innerHTML = otherOptions;
        document.querySelector('#no-id .card-body > p').innerHTML = noId;
        document.getElementById('learn-more-id').href = data.source;
        document.getElementById('learn-more-id').innerText = "Learn more about voter ID requirements in " + triggerUpdate.value;
        document.getElementById('last-updated-id').innerText=triggerUpdate.value + " voter ID info last updated: " + data.last_checked;
    }) 
})

triggerUpdate.addEventListener('change', (event) => {
    getData('/api/id/', event.target.value)
    .then(data => {
        let atPolls = data.at_polls;
        let otherOptions = data.other_options;
        let noId = data.no_id;
        document.querySelector('#at-polls .card-body > p').innerHTML  = atPolls;
        document.querySelector('#at-polls h4').innerHTML  = "Voter ID requirements in " + event.target.value
        document.querySelector('#other-options .card-body > p').innerHTML = otherOptions;
        document.querySelector('#no-id .card-body > p').innerHTML = noId;
        document.getElementById('learn-more-id').href = data.source;
        document.getElementById('learn-more-id').innerText = "Learn more about voter ID requirements in " + event.target.value;
        document.getElementById('last-updated-id').innerText=event.target.value + " voter ID info last updated: " + data.last_checked;
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
