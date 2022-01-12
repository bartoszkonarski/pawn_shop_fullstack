<template>
  <section>
      <form @submit="postMethod">
        <input type="text" name="username" v-model="login">
        <input type="text" name="password" v-model="password">
        <input type="submit"/>
      </form>
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
      }
    },
    methods: {
      postMethod(){
        axios.post(
        'http://127.0.0.1:5000/login',
        { username: this.login, password: this.password},
        { headers: {'Content-Type': 'application/json'}}
        );
        alert("bump");
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
