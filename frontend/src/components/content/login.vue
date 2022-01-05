<template>
  <section>
      <form action="http://127.0.0.1:5000/login" method="POST">
        <input type="text" name="username">
        <input type="text" name="password">
        <input type="submit"/>
      </form>
  </section>
</template>

<script>
export default {
  name: 'Login',
  components: {
  },
  props: ['logged'],
  data: function() {
    return{
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
