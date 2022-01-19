<template>
  <section id="app">
    <navBar 
    :logged="logged"
    @logOut="loggOut()"
    > </navBar>
    <router-view
    :logged="logged"
    @logIn="loggIn($event)"
    ></router-view>
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
      this.$session.destroy();
      this.$router.push('/log');
    },
    loggIn: function(tokken) {
      this.$session.start();
      this.logged = true;
      this.$session.set('tokken',tokken)
      console.log("Próba sesji: ", this.$session.get('tokken'));
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
