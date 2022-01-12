<template>
  <section>
      <form>
        <input type="text" name="username" v-model="login">
        <input type="text" name="password" v-model="password">
        <input type="button"  value="Zaloguj!" @click="postMethod"/>
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
        response: [],
      }
    },
    methods: {
      async postMethod(){
        // console.log("Posłano zapytanie post do servera!")
        await axios.post(
        'http://127.0.0.1:5000/login',
        { username: this.login, password: this.password},
        { headers: {'Content-Type': 'application/json'}}
        )
        .then(response => (
          this.response = response,
          this.loginProc(response.status, response.data.access_token)
          ))
        .catch(error => (
          this.response = error.response,
          this.loginProc(error.response.status, "")
          ))
        // this.loginProc(this.logedStatus)
       },
      loginProc(val, tokken){
        console.log("Zmiana statusu logowania!")
        if(val == 200) this.$emit('logIn',tokken);
        else alert(val);
      },
      // testMet: function() {
      //   this.$router.push('/')
      // }
    },
    beforeMount(){
      if(this.logged == true) this.$router.push('/')
    },
  }
</script>

<style>
body {
  margin: 0px;
  background: #663EFF;
}
</style>
