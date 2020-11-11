/** csrftoken */
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const csrftoken = getCookie('csrftoken');
const request = new XMLHttpRequest();


/** generate doc */

let btnSubmit = document.getElementById('btnSubmit');
let formCreateDoc = document.getElementById('formCreateDoc');
const response = document.getElementById('response');
const loading = document.getElementById('loading');

btnSubmit.addEventListener('click', function (e) {
    e.preventDefault();
    createDocument(formCreateDoc);
});

function createDocument(form) {
    loading.classList.add('show');
    request.open(form.method, form.action, true);
    request.setRequestHeader("X-CSRFToken", csrftoken);
    request.onreadystatechange = function () {
        if (request.readyState === 4) {
            if (request.status === 200) {
                console.log(JSON.parse(request.response))
                response.innerHTML = JSON.parse(request.response).renderhtml;
            } else {
                response.innerHTML = JSON.parse(request.response).message;
                console.log('Error', JSON.parse(request.response).message);
            }
        }
        loading.classList.remove('show');
    };
    request.onerror = e => {
        console.log("Error " + e);
        loading.classList.remove('show');
    };
    request.send(new FormData(form));
}