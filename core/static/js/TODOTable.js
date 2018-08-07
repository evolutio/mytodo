Vue.component('todo-table', {
  props: ['todotarefas'],
   data: function(){
     return {};
   },
  methods: {
    remove: function(tarefa){
      var self = this
      // tarefa.removing = true
      Vue.set(tarefa, 'removing', true)
      API.remove_tarefa(tarefa.id).then(function(response){
        var idx = self.todotarefas.indexOf(tarefa);
        self.todotarefas.splice(idx, 1);
      })
    }
  },
  template:`
    <table class="table">
      <thead>
        <tr>
          <th></th>
          <th>To-do</th>
          <th></th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="tarefa in todotarefas">
          <td><input type="checkbox" v-model="tarefa.feita"></td>
          <td :class="{risca: tarefa.feita}">{{tarefa.tarefa}}</td>
          <td>
            <button class="button is-warning" :class="{'is-loading': tarefa.removing}" @click="remove(tarefa)">
              <span class="icon has-text-info" v-if="!tarefa.removing"><i class="fa fa-trash-o"></i></span>
            </button>
          </td>
        </tr>
      </tbody>
    </table>
  `,
})