axios.defaults.xsrfHeaderName = "X-CSRFToken";
axios.defaults.xsrfCookieName = "csrftoken";

window.API = {
    list_tarefas: function(){
        return get('/api/list_tarefas');
    },
    add_tarefa: function(tarefa){
        return post('/api/add_tarefa', {tarefa: JSON.stringify(tarefa)})
    }
}

function get(url, params){
    return axios.get(url, {params: params});
}

function post(url, params){
    var fd = new FormData();
    params = params || {}
    Object.keys(params).map((k) => {
        fd.append(k, params[k]);
    })
    return axios.post(url, fd);
}