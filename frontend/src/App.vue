<template>
  <section id="app">
    <navBar 
    :logged="logged"
    @logOut="loggOut()"
    > </navBar>
    <router-view
    :logged="logged"
    @logIn="loggIn($emit)"
    ></router-view>
    {{tokken}}
  </section>
</template>

<script>
import navBar from './components/navBar.vue';
export default {
  name: 'App',
  components: {
    navBar: navBar,
  },
  data: function() {
    return{
      logged: false,
      tokken: "",
    }
  },
  methods:{
    loggOut: function() {
      this.logged = false;
      this.tokken = "";
      this.$router.push('/log');
    },
    loggIn: function(tokken) {
      this.logged = true;
      this.tokken = tokken.tokken;
      this.$router.push('/');
    },
    // testMet: function() {
    //   console.log("Bump")
    // }
  },
  // watch:{
  //   logged: (val) => { 
  //     console.log("watch method")
  //     // window.location.href="https://www.google.com/"
  //     if(val) this.$router.push('/');
  //     if(!val) this.$router.push('/log')
  //   }
  // }
}
</script>

<style>
body {
  margin: 0px;
  background: #663EFF;
}
</style>
