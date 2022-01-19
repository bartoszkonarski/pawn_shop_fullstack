<template>
  <section>
      <form>
        <input type="text" name="username" class="login-input-text" placeholder="Login" v-model="login">
        <input type="text" name="password" class="login-input-text" placeholder="Hasło" v-model="password">
        <input type="button"  value="Zaloguj!" class="login-input-button" @click="postMethod"/>
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
        if(val == 200)
        {
          this.$emit('logIn',tokken);
        } 
        else alert("Błąd logowania! Upewnij się że wpisałeś poprawne dane!");
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
input {
  display: block;
  margin-left: auto;
  margin-right: auto;
}
.login-input-text{
  border-radius: 4px;
  height: 3vh;
  width: 10vw;
  margin-bottom: 15px;
  margin-top: 5px;
  transition: .3s;
}
.login-input-text:focus{
  width: 15vw;

}
.login-input-button{
  border-radius: 4px;
  height: 3vh;
  width: 5vw;
}
</style>
