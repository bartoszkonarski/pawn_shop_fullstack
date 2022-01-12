<template>
  <section>
      <form>
        <input type="text" name="username" v-model="login">
        <input type="text" name="password" v-model="password">
        <input type="button" @click="postMethod"/>
      </form>
      {{response}}
      {{logedStatus}}
  </section>
</template>

<script>
  import axios from 'axios';
  export default {
    
    name: 'Login',
    components: {
    },
    props: ['logged'],
    data: function() {
      return{
        login:"",
        password:"",
        response: [],
        logedStatus: 0,
      }
    },
    methods: {
      postMethod(){
        axios.post(
        'http://127.0.0.1:5000/login',
        { username: this.login, password: this.password},
        { headers: {'Content-Type': 'application/json'}}
        )
        .then(response => (
          this.response = response,
          this.logedStatus = response.status          
          ))
        .catch(error => console.log(error))
        console.log(this.response)
        alert("bump");
      }
    },
    watch: {
      logedStatus: () => {
        if(this.logedStatus == 200) this.logged = true; 
        // $emit("logStatus",this.logged)
      }
    },
    beforeMount(){
      if(this.logged == true) window.location.href = "http://localhost:8080/#/";
    },
  }
</script>

<style>
body {
  margin: 0px;
  background: #663EFF;
}
</style>
