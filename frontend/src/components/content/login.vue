<template>
  <section>
      Działa! {{logged}}
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
    if(this.logged) window.location.href = "http://localhost:8080/#/";
  },
}
</script>

<style>
body {
  margin: 0px;
  background: #663EFF;
}
</style>
