//triggerUpdate defined in the covid data file
window.addEventListener('DOMContentLoaded', (event) => {
    getData('/api/id/', triggerUpdate.value)
    .then(data => {
        let atPolls = data.at_polls;
        let otherOptions = data.other_options;
        let noId = data.no_id;
        document.querySelector('#at-polls .card-body > p').innerHTML  = atPolls;
        document.querySelector('#other-options .card-body > p').innerHTML = otherOptions;
        document.querySelector('#no-id .card-body > p').innerHTML = noId;
    }) 
})

triggerUpdate.addEventListener('change', (event) => {
    getData('/api/id/', event.target.value)
    .then(data => {
        let atPolls = data.at_polls;
        let otherOptions = data.other_options;
        let noId = data.no_id;
        document.querySelector('#at-polls .card-body > p').innerHTML  = atPolls;
        document.querySelector('#other-options .card-body > p').innerHTML = otherOptions;
        document.querySelector('#no-id .card-body > p').innerHTML = noId;
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
